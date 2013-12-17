# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from cachi.models import Naturaleza, SitioArqueologico, Forma, Color, Periodo
from django import forms


class SearchForm(forms.Form):
    """A form to search piezas"""
    naturaleza = forms.ModelChoiceField(queryset=Naturaleza.objects.all(),
        empty_label="(Todas)", required=False)
    forma = forms.ModelChoiceField(queryset=Forma.objects.all(),
        empty_label="(Todas)", required=False)
    color = forms.ModelChoiceField(queryset=Color.objects.all(),
        empty_label="(Todos)", required=False)
    periodo = forms.ModelChoiceField(queryset=Periodo.objects.all(),
        empty_label="(Todos)", required=False)
    sitio_arqueologico = forms.ModelChoiceField(queryset=SitioArqueologico.objects.all(),
        empty_label="(Todos)", required=False)
