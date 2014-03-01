# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    get_object_or_404,
    redirect,
)

from cachi.forms import (
    AdjuntoForm,
    FichaTecnicaForm,
    FragmentoForm,
    PiezaConjuntoForm,
    ProcedenciaForm,
    BusquedaPiezaForm)

from cachi.models import (
    Adjunto,
    Fragmento,
    PiezaConjunto,
)
from cachi.models import (
    RAZON_ACTUALIZACION_CREACION,
)
from cachi.utils import (
    render_html_dinamico,
    bytes_2_mb,
)


@login_required(redirect_field_name=None)
def index(request):
    return render_html_dinamico(
        request,
        'cachi/index.html',
        {},
    )


@login_required(redirect_field_name=None)
def busca_pieza(request):
    form = BusquedaPiezaForm(request.POST)
    if request.method == 'POST':
        if not form.is_valid():
            return render_html_dinamico(
                request,
                'cachi/pieza/busca_pieza_conjunto.html',
                {
                    'form': form,
                    'piezas': [],
                },
            )

        resultado = PiezaConjunto.objects.buscar_piezas(
            form.cleaned_data['nro_inventario'],
            form.cleaned_data['naturaleza'],
            form.cleaned_data['sitio_arqueologico'],
            form.cleaned_data['ubicacion']
        )

        return render_html_dinamico(
            request,
            'cachi/pieza/busca_pieza_conjunto.html',
            {
                'form': form,
                'piezas': resultado,
            },
        )

    return render_html_dinamico(
        request,
        'cachi/pieza/busca_pieza_conjunto.html',
        {
            'mostrar_ayuda_busqueda': True,
            'form': form
        },
    )


@login_required(redirect_field_name=None)
def ver_pieza(request):
    if request.method == 'POST':
        pass

    return render_html_dinamico(
        request,
        'cachi/pieza/busca_pieza.html',
        {},
    )


@login_required(redirect_field_name=None)
def nueva_edita_pieza_conjunto(request, pieza_conjunto_pk=None):
    pieza_conjunto = None
    procedencia = None
    pieza_conjunto_adjuntos = None
    pieza_conjunto_fragmentos = None
    if pieza_conjunto_pk:
        pieza_conjunto = get_object_or_404(
            PiezaConjunto,
            pk=pieza_conjunto_pk,
        )
        procedencia = pieza_conjunto.obtiene_procedencia()
        pieza_conjunto_adjuntos = pieza_conjunto.obtiene_adjuntos()
        pieza_conjunto_fragmentos = pieza_conjunto.obtiene_fragmentos()

    if request.method == 'POST':
        form_pieza_conjunto = PiezaConjuntoForm(
            request.POST,
        )
        form_procedencia = ProcedenciaForm(
                request.POST,
        )
        form_adjunto = AdjuntoForm(
            request.POST,
            request.FILES,
        )

        if (form_pieza_conjunto.is_valid() and
            form_procedencia.is_valid() and
            form_adjunto.is_valid()):

            pieza_conjunto = form_pieza_conjunto.save()

            procedencia = form_procedencia.save(
                commit=False,
            )
            procedencia.pieza_conjunto = pieza_conjunto
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
                        pieza_conjunto=pieza_conjunto,
                    )
            return redirect('edita_pieza_conjunto', pieza_conjunto.pk)

    elif request.method == "GET":
        form_pieza_conjunto = PiezaConjuntoForm(
            instance=pieza_conjunto,
        )
        form_procedencia = ProcedenciaForm(
            instance=procedencia,
        )
        form_adjunto = AdjuntoForm()

    contexto = {
        'pieza_conjunto': pieza_conjunto,
        'form_pieza_conjunto': form_pieza_conjunto,
        'form_procedencia': form_procedencia,
        'form_adjunto': form_adjunto,
        'pieza_conjunto_adjuntos': pieza_conjunto_adjuntos,
        'pieza_conjunto_fragmentos': pieza_conjunto_fragmentos,
    }

    return render_html_dinamico(
        request,
        'cachi/pieza/nueva_pieza_conjunto.html',
        contexto,
    )


@login_required(redirect_field_name=None)
def nueva_edita_ficha_tecnica(request, pieza_conjunto_pk, fragmento_pk=None):
    if pieza_conjunto_pk:
        pieza_conjunto = get_object_or_404(
            PiezaConjunto,
            pk=pieza_conjunto_pk,
        )

        fragmento = None
        ficha_tecnica = None
        ficha_tecnica_adjuntos = None
        if fragmento_pk:
            fragmento = get_object_or_404(
                Fragmento,
                pk=fragmento_pk,
            )
            ficha_tecnica = fragmento.obtiene_ficha_tecnica()
            ficha_tecnica_adjuntos = ficha_tecnica.obtiene_adjuntos()

        if request.method == 'POST':
            if pieza_conjunto_pk == request.POST['pieza_conjunto_pk']:
                form_fragmento = FragmentoForm(
                    request.POST,
                    instance=fragmento,
                )
                form_ficha_tecnica = FichaTecnicaForm(
                    request.POST,
                    instance=ficha_tecnica,
                )
                form_adjunto = AdjuntoForm(
                    request.POST,
                    request.FILES,
                )
                if (form_fragmento.is_valid() and
                    form_ficha_tecnica.is_valid() and
                    form_adjunto.is_valid()):

                    fragmento = form_fragmento.save(
                        commit=False,
                    )
                    fragmento.pieza_conjunto = pieza_conjunto
                    fragmento.save()

                    ficha_tecnica = form_ficha_tecnica.save(
                        commit=False,
                    )
                    ficha_tecnica.razon_actualizacion = \
                    RAZON_ACTUALIZACION_CREACION
                    ficha_tecnica.fecha = date.today()
                    ficha_tecnica.usuario = request.user
                    ficha_tecnica.fragmento = fragmento
                    ficha_tecnica.save()

                    fragmento.ultima_version = ficha_tecnica
                    fragmento.save()

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
                                ficha_tecnica=ficha_tecnica,
                            )

                    return redirect('edita_pieza_conjunto', pieza_conjunto_pk)
            else:
                #TODO: 404?
                pass

        elif request.method == 'GET':

            form_fragmento = FragmentoForm(
                instance=fragmento,
            )
            form_ficha_tecnica = FichaTecnicaForm(
                instance=ficha_tecnica,
            )
            form_adjunto = AdjuntoForm()

        contexto = {
            'pieza_conjunto': pieza_conjunto,
            'form_fragmento': form_fragmento,
            'form_ficha_tecnica': form_ficha_tecnica,
            'form_adjunto': form_adjunto,
            'ficha_tecnica_adjuntos': ficha_tecnica_adjuntos,
        }
        return render_html_dinamico(
            request,
            'cachi/pieza/nueva_ficha_tecnica.html',
            contexto,
        )
