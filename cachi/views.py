# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required

from cachi.forms import (
    FichaTecnicaForm,
    PiezaConjuntoForm,
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
        pass
    elif request.method == 'GET':
        form_pieza_conjunto = PiezaConjuntoForm()
        form_ficha_tecnica = FichaTecnicaForm()

        contexto = {
            'form_pieza_conjunto': form_pieza_conjunto,
            'form_ficha_tecnica': form_ficha_tecnica,
        }

    return render_html_dinamico(
        request,
        'cachi/nueva_pieza.html',
        contexto,
    )
