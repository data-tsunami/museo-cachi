# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from cachi.forms import SearchForm
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from cachi.models import Pieza
from django.http.response import HttpResponse
from cachi.tests import get_test_image


def index(request):
    return render_to_response('cachi/index.html')


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        qs = Pieza.objects.all()
        if not form.is_valid():
            raise(Exception("Invalid form")) # FIXME: remove this

        if form.cleaned_data['color']:
            qs = qs.filter(color=form.cleaned_data['color'])

        if form.cleaned_data['forma']:
            qs = qs.filter(forma=form.cleaned_data['forma'])

        if form.cleaned_data['naturaleza']:
            qs = qs.filter(naturaleza=form.cleaned_data['naturaleza'])

        if form.cleaned_data['periodo']:
            qs = qs.filter(periodo=form.cleaned_data['periodo'])

        if form.cleaned_data['sitio_arqueologico']:
            qs = qs.filter(sitio_arqueologico=form.cleaned_data['sitio_arqueologico'])

        mostrar_imagenes = form.cleaned_data['mostrar_imagenes']

    else:
        form = SearchForm()
        qs = None
        mostrar_imagenes = False

    ctx = {
        'form': form,
        'result': qs,
        'mostrar_imagenes': mostrar_imagenes,
    }
    return render_to_response('cachi/search.html', RequestContext(request, ctx))


def imagen_de_pieza(request, pk):
    response = HttpResponse(content_type='image/jpeg')
    img_data = get_test_image()
    response['Content-Length'] = len(img_data)
    response.write(img_data)

    # full_filename = default_storage.path(doc.document_file.path)
    # filesize = os.path.getsize(full_filename)
    # response['Content-Length'] = filesize

    # with open(full_filename) as f:
    #     response.write(f.read())
    return response
