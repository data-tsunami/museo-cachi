# encoding: utf-8

from django.shortcuts import render_to_response
from django.template import RequestContext


def render_html_dinamico(request, html, contexto=None):
    if contexto == None:
        contexto = {}
    return render_to_response(
        html,
        contexto,
        context_instance=RequestContext(request)
    )


def bytes_2_mb(bytes):
    return float(bytes) / (1024 * 1024)
