# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from cachi.forms import (
    AdjuntoForm,
    FichaTecnicaForm,
    FichaTecnicaFormSet,
    FragmentoFormSet,
    PiezaConjuntoForm,
    ProcedenciaForm,
)

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
    if request.method == 'POST':
        pass

    return render_html_dinamico(
        request,
        'cachi/pieza/busca_pieza.html',
        {},
    )


@login_required(redirect_field_name=None)
def nueva_pieza(request):
    if request.method == 'POST':
        if 'siguiente' in request.POST:
            form_pieza_conjunto = PiezaConjuntoForm(
                request.POST,
            )
            form_procedencia = ProcedenciaForm(
                    request.POST,
            )
            formset_fragmento = FragmentoFormSet(
                request.POST,
            )
            form_adjunto = AdjuntoForm(
                request.POST,
                request.FILES,
            )

            if (form_pieza_conjunto.is_valid() and
                form_procedencia.is_valid() and
                formset_fragmento.is_valid() and
                form_adjunto.is_valid()):

                pieza_conjunto = form_pieza_conjunto.save()

                procedencia = form_procedencia.save(
                    commit=False,
                )
                procedencia.pieza_conjunto = pieza_conjunto
                procedencia.save()

                #adjuntos = request.FILES.getlist('adjuntos')
                adjuntos = form_adjunto.cleaned_data['adjuntos']
                for adjunto in adjuntos:
                    tipo = adjunto.content_type.split('/')[1]
                    Adjunto.objects.create(
                        nombre_archivo=adjunto.name,
                        content_type=adjunto.content_type,
                        tipo=tipo,
                        adjunto=adjunto,
                        pieza_conjunto=pieza_conjunto,
                    )

                formset_fragmento = FragmentoFormSet(
                    request.POST,
                    instance=pieza_conjunto,
                )
                if formset_fragmento.is_valid():
                    fragmentos = formset_fragmento.save()

                    dic_fichas_tecnicas = {}
                    for fragmento in fragmentos:
                        dic_forms = {}

                        prefix = 'fragmento-{0}'.format(fragmento.pk)

                        form_ficha_tecnica = FichaTecnicaForm(
                            prefix=prefix,
                        )
                        form_adjunto = AdjuntoForm(
                            prefix=prefix,
                        )

                        dic_forms = {
                            'form_ficha_tecnica': form_ficha_tecnica,
                            'form_adjunto': form_adjunto,
                        }
                        dic_fichas_tecnicas[
                            fragmento.numero_inventario
                        ] = dic_forms

                    contexto = {
                        'dic_fichas_tecnicas': dic_fichas_tecnicas,
                        'pieza_conjunto': pieza_conjunto,
                    }
                    return render_html_dinamico(
                        request,
                        'cachi/pieza/nueva_ficha_tecnica.html',
                        contexto,
                    )

        elif 'guardar' in request.POST:
            pieza_conjunto = PiezaConjunto.objects.get(
                pk=request.POST["pk_pieza_conjunto"],
            )
            fragmentos = Fragmento.objects.filter(
                pieza_conjunto=pieza_conjunto,
            )

            valida = True
            dic_fichas_tecnicas = {}
            lista_fichas_tecnicas_adjuntos = []
            for fragmento in fragmentos:
                dic_forms = {}

                prefix = 'fragmento-{0}'.format(fragmento.pk)

                form_ficha_tecnica = FichaTecnicaForm(
                    request.POST,
                    prefix=prefix,
                )
                form_adjunto = AdjuntoForm(
                    request.POST,
                    request.FILES,
                    prefix=prefix,
                )

                dic_forms = {
                    'form_ficha_tecnica': form_ficha_tecnica,
                    'form_adjunto': form_adjunto,
                }

                dic_fichas_tecnicas[
                    fragmento.numero_inventario
                ] = dic_forms

                if (form_ficha_tecnica.is_valid() and
                    form_adjunto.is_valid()):

                    ficha_tecnica = form_ficha_tecnica.save(
                        commit=False,
                    )
                    ficha_tecnica.razon_actualizacion = RAZON_ACTUALIZACION_CREACION
                    ficha_tecnica.fecha = date.today()
                    ficha_tecnica.usuario = request.user
                    ficha_tecnica.fragmento = fragmento

                    lista_fichas_tecnicas_adjuntos.append(
                        {'ficha_tecnica': ficha_tecnica,
                         'form_adjunto': form_adjunto,
                        }
                    )

                else:
                    valida = False

            if not valida:
                contexto = {
                    'dic_fichas_tecnicas': dic_fichas_tecnicas,
                    'pieza_conjunto': pieza_conjunto,
                }
                return render_html_dinamico(
                    request,
                    'cachi/pieza/nueva_ficha_tecnica.html',
                    contexto,
                )

            for dic_ficha_tecnica_adjunto in lista_fichas_tecnicas_adjuntos:
                ficha_tecnica = dic_ficha_tecnica_adjunto['ficha_tecnica']
                ficha_tecnica.save()

                form_adjunto = dic_ficha_tecnica_adjunto['form_adjunto']
                adjuntos = form_adjunto.cleaned_data['adjuntos']
                for adjunto in adjuntos:
                    tipo = adjunto.content_type.split('/')[1]
                    Adjunto.objects.create(
                        nombre_archivo=adjunto.name,
                        content_type=adjunto.content_type,
                        tipo=tipo,
                        adjunto=adjunto,
                        ficha_tecnica=ficha_tecnica,
                    )

            return redirect('nueva_pieza')

    elif request.method == "GET":
        form_pieza_conjunto = PiezaConjuntoForm()
        formset_fragmento = FragmentoFormSet()
        form_procedencia = ProcedenciaForm()
        form_adjunto = AdjuntoForm()

    contexto = {
        'form_pieza_conjunto': form_pieza_conjunto,
        'formset_fragmento': formset_fragmento,
        'form_procedencia': form_procedencia,
        'form_adjunto': form_adjunto,
    }

    return render_html_dinamico(
        request,
        'cachi/pieza/nueva_pieza.html',
        contexto,
    )
