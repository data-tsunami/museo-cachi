# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from cachi.forms import SearchForm
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from cachi.models import Pieza


def index(request):
    return render_to_response('cachi/index.html')


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        qs = Pieza.objects.all()
        if form.is_valid():
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
        else:
            raise(Exception("Invalid form")) # FIXME: remove this
    else:
        form = SearchForm()
        qs = None

    ctx = {
        'form': form,
        'result': qs,
    }
    return render_to_response('cachi/search.html', RequestContext(request, ctx))
