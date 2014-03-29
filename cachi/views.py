# -*- coding: utf-8 -*-
#======================================================================
#    This file is part of "Museo-Cachi".
#
#    Museo-Cachi is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Museo-Cachi is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Museo-Cachi.  If not, see <http://www.gnu.org/licenses/>.
#======================================================================

from __future__ import unicode_literals

from datetime import date, datetime

#from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views.generic import (
    CreateView, ListView, UpdateView)
from django.shortcuts import (
    get_object_or_404, redirect)

from braces.views import LoginRequiredMixin

from cachi.forms import (
    AdjuntoForm, FichaTecnicaForm, PiezaConjuntoForm,
    ProcedenciaForm, BusquedaPiezaForm)

from cachi.models import (
    Adjunto, Fragmento, PiezaConjunto)

from cachi.models import (
    RAZON_ACTUALIZACION_CREACION,
    RAZON_ACTUALIZACION_ACTUALIZACION,
    RAZON_ACTUALIZACION_DIAGNOSTICO)

from cachi.utils import (
    render_html_dinamico, bytes_2_mb)


@login_required(redirect_field_name=None)
def index(request):
    #TODO: Implementar.
    return redirect('busca_pieza')


class PiezasListView(ListView):

    template_name = 'cachi/pieza/busca_pieza_conjunto.html'
    context_object_name = 'piezas'
    form_class = BusquedaPiezaForm
    model = PiezaConjunto

    @method_decorator(login_required(redirect_field_name=None))
    def dispatch(self, *args, **kwargs):
        return super(PiezasListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        response = super(PiezasListView, self).get(request, **kwargs)
        self.form = self.form_class()
        return response

    def get_context_data(self, **kwargs):
        context = super(PiezasListView, self).get_context_data(**kwargs)
        context['form'] = self.form

        context['mostrar_ayuda_busqueda'] = self.mostrar_ayuda_busqueda
        return context

    def get_queryset(self):
        self.form = self.form_class(self.request.GET)

        self.mostrar_ayuda_busqueda = False
        if not self.request.GET.items():
            self.mostrar_ayuda_busqueda = True

        if not self.form.is_valid():
            self.mostrar_ayuda_busqueda = True
            return None

        data = self.form.cleaned_data

        queryset = PiezaConjunto.objects.buscar_piezas(
            data['nro_inventario'],
            data['naturaleza'],
            data['sitio_arqueologico'],
            data['ubicacion']
        )
        return queryset


class PiezaCreateUpdateView(UpdateView):

    template_name = 'cachi/pieza/nueva_pieza_conjunto.html'
    model = PiezaConjunto
    context_object_name = 'pieza_conjunto'
    form_class = PiezaConjuntoForm
    form_procedencia = ProcedenciaForm
    form_adjunto = AdjuntoForm

    @method_decorator(login_required(redirect_field_name=None))
    def dispatch(self, *args, **kwargs):
        return super(PiezaCreateUpdateView, self).dispatch(*args, **kwargs)

    def get_object(self, queryset=None):
        self.cantidad_fragmentos_invalido = False
        self.procedencia = None

        self.creating = not 'pk' in self.kwargs
        if not self.creating:
            pieza_conjunto = super(
                PiezaCreateUpdateView, self).get_object(queryset)

            self.procedencia = pieza_conjunto.obtiene_procedencia()
            self.pieza_conjunto_adjuntos = pieza_conjunto.obtiene_adjuntos()
            self.pieza_conjunto_fragmentos = pieza_conjunto.obtiene_fragmentos()

            self.cantidad_instancias_fragmentos = self.pieza_conjunto_fragmentos.count()
            if pieza_conjunto.cantidad_fragmentos != self.cantidad_instancias_fragmentos:
                self.cantidad_fragmentos_invalido = True

            return pieza_conjunto

    def get_context_data(self, **kwargs):
        context = super(PiezaCreateUpdateView, self).get_context_data(**kwargs)

        if 'form_procedencia' not in context:
            context['form_procedencia'] = self.form_procedencia(
                instance=self.procedencia,
            )

        if 'form_adjunto' not in context:
            context['form_adjunto'] = self.form_adjunto

        if not self.creating:
            context['pieza_conjunto_adjuntos'] = self.pieza_conjunto_adjuntos
            context['pieza_conjunto_fragmentos'] = self.pieza_conjunto_fragmentos
            context['cantidad_fragmentos_invalido'] = self.cantidad_fragmentos_invalido,
            context['cantidad_instancias_fragmentos'] = self.cantidad_instancias_fragmentos
        return context

    def form_valid(self, form):
        return self.process_all_forms(form)

    def form_invalid(self, form):
        return self.process_all_forms(form)

    def process_all_forms(self, form):
        if form.is_valid():
            self.object = form.save()

        form_procedencia = self.form_procedencia(
            self.request.POST, instance=self.procedencia,
        )
        form_adjunto = self.form_adjunto(
            self.request.POST,
            self.request.FILES,
        )

        is_valid = all([
            form.is_valid(),
            form_procedencia.is_valid(),
            form_adjunto.is_valid(),
        ])
        if is_valid:
            return self.forms_valid(
                form_procedencia, form_adjunto)
        else:
            if form.is_valid():
                self.object.delete()
                self.object = None

            return self.forms_invalid(
                form, form_procedencia, form_adjunto)

    def forms_valid(self, form_procedencia, form_adjunto):
        procedencia = form_procedencia.save(
            commit=False,
        )
        if self.creating:
            procedencia.pieza_conjunto = self.object
        procedencia.save()

        adjuntos = form_adjunto.cleaned_data['adjuntos']
        for adjunto in adjuntos:
            if adjunto:
                tipo = adjunto.content_type.split('/')[1]
                Adjunto.objects.create(
                    nombre_archivo=adjunto.name,
                    content_type=adjunto.content_type,
                    size="{0:.2f} MB".format(bytes_2_mb(adjunto.size)),
                    tipo=tipo,
                    adjunto=adjunto,
                    pieza_conjunto=self.object,
                )
        return redirect(self.get_success_url())

    def forms_invalid(self, form, form_procedencia, form_adjunto):
        messages.add_message(
            self.request,
            messages.ERROR,
            '<strong>Operación Errónea!</strong>\
            Revise y complete todos los campos obligatorios\
            para la creación de una nueva pieza o conjunto.',
        )
        context = self.get_context_data(
            form=form,
            form_procedencia=form_procedencia,
            form_adjunto=form_adjunto,
        )

        return self.render_to_response(context)

    def get_success_url(self):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            '<strong>Operación Exitosa!</strong>\
            Se llevó a cabo con éxito la creación de la\
            nueva pieza o conjunto.',
        )
        return reverse(
            'edita_pieza_conjunto',
            args=(self.object.pk,))


@login_required(redirect_field_name=None)
def nueva_edita_fragmento(request, pieza_conjunto_pk, fragmento_pk=None, ficha_tecnica_pk=None, fecha=None):
    if pieza_conjunto_pk:
        pieza_conjunto = get_object_or_404(
            PiezaConjunto,
            pk=pieza_conjunto_pk,
        )

        fragmento = None
        ficha_tecnica = None
        ficha_tecnica_adjuntos = None
        fichas_tecnicas_diagnosticos = None
        fecha_diagnostico = None
        if fragmento_pk:
            fragmento = pieza_conjunto.obtiene_fragmento(fragmento_pk)

            ficha_tecnica = fragmento.obtiene_ultima_ficha_tecnica()
            if ficha_tecnica_pk:
                ficha_tecnica = fragmento.obtiene_ficha_tecnica_diagnostico(
                    ficha_tecnica_pk,
                    datetime.strptime(fecha, '%Y-%m-%d').date()
                )
                fecha_diagnostico = ficha_tecnica.fecha

            ficha_tecnica_adjuntos = ficha_tecnica.obtiene_adjuntos()
            fichas_tecnicas_diagnosticos = \
            fragmento.obtiene_fichas_tecnicas_diagnosticos()

        if request.method == 'POST':
            mensaje = ''

            if pieza_conjunto_pk == request.POST['pieza_conjunto_pk']:

                form_ficha_tecnica = FichaTecnicaForm(
                    request.POST,
                    instance=ficha_tecnica,
                )
                form_adjunto = AdjuntoForm(
                    request.POST,
                    request.FILES,
                )

                if (form_ficha_tecnica.is_valid() and
                    form_adjunto.is_valid()):

                    if not fragmento and not ficha_tecnica:
                        fragmento = Fragmento.objects.create(
                            pieza_conjunto=pieza_conjunto,
                        )

                    ficha_tecnica = form_ficha_tecnica.save(
                        commit=False,
                    )
                    ficha_tecnica.pk = None

                    if 'guardar' in request.POST:
                        ficha_tecnica.razon_actualizacion = \
                        RAZON_ACTUALIZACION_CREACION

                        mensaje = 'Se llevó a cabo con éxito la\
                        creación de la nueva ficha técnica.'

                    elif 'edita_ficha_tecnica' in request.POST:
                        ficha_tecnica.razon_actualizacion = \
                        RAZON_ACTUALIZACION_ACTUALIZACION

                        mensaje = 'Se llevó a cabo con éxito la\
                        actualización de la ficha técnica.'

                    elif 'nuevo_diagnostico_estado' in request.POST:
                        ficha_tecnica.razon_actualizacion = \
                        RAZON_ACTUALIZACION_DIAGNOSTICO

                        mensaje = 'Se llevó a cabo con éxito la\
                        creación del nuevo diagnóstico de estado\
                        de la ficha técnica.'

                    ficha_tecnica.fecha = date.today()
                    ficha_tecnica.usuario = request.user
                    ficha_tecnica.fragmento = fragmento
                    ficha_tecnica.save()

                    fragmento.ultima_version = ficha_tecnica
                    fragmento.save()

                    adjuntos = form_adjunto.cleaned_data['adjuntos']

                    if 'edita_ficha_tecnica' in request.POST:
                        for ficha_tecnica_adjunto in ficha_tecnica_adjuntos or []:
                            adjuntos.append(ficha_tecnica_adjunto)

                    for archivo_adjunto in adjuntos:
                        if archivo_adjunto:
                            if isinstance(archivo_adjunto, Adjunto):
                                nombre = archivo_adjunto.nombre_archivo
                                tipo = archivo_adjunto.tipo
                                size = archivo_adjunto.size
                                replica_adjunto = ContentFile(archivo_adjunto.adjunto.read())
                                replica_adjunto.name = archivo_adjunto.adjunto.name
                                adjunto = replica_adjunto
                            else:
                                nombre = archivo_adjunto.name
                                tipo = archivo_adjunto.content_type.split('/')[1]
                                adjunto = archivo_adjunto
                                size = "{0:.2f} MB".format(bytes_2_mb(archivo_adjunto.size))

                            Adjunto.objects.create(
                                nombre_archivo=nombre,
                                content_type=archivo_adjunto.content_type,
                                size=size,
                                tipo=tipo,
                                adjunto=adjunto,
                                ficha_tecnica=ficha_tecnica,
                            )

                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        '<strong>Operación Exitosa!</strong> {0}'.format(mensaje),
                    )

                    return redirect(
                        'edita_fragmento',
                        pieza_conjunto.pk,
                        fragmento.pk,
                    )
            messages.add_message(
                request,
                messages.ERROR,
                '<strong>Operación Errónea!</strong>\
                Revise y complete todos los campos obligatorios\
                para realizar la operación requerida.',
            )

        elif request.method == 'GET':

            form_ficha_tecnica = FichaTecnicaForm(
                instance=ficha_tecnica,
            )
            form_adjunto = AdjuntoForm()

        contexto = {
            'pieza_conjunto': pieza_conjunto,
            'fragmento': fragmento,
            'ficha_tecnica_pk': ficha_tecnica_pk,
            'form_ficha_tecnica': form_ficha_tecnica,
            'form_adjunto': form_adjunto,
            'ficha_tecnica_adjuntos': ficha_tecnica_adjuntos,
            'fichas_tecnicas_diagnosticos': fichas_tecnicas_diagnosticos,
            'fecha_diagnostico': fecha_diagnostico
        }
        return render_html_dinamico(
            request,
            'cachi/pieza/nuevo_fragmento.html',
            contexto,
        )
