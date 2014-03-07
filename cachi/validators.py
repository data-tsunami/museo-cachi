from django.core.exceptions import ValidationError


def validador_cantidad_fragmentos(cantidad_fragmentos):
    if not cantidad_fragmentos >= 1:
        raise ValidationError(u'La cantidad de fragmentos debe ser mayor o igual a 1')
