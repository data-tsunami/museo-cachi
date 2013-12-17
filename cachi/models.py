# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Pieza(models.Model):
    """
    Una pieza del museo

    Ej:
    - numero_inventario = 212313
    - nombre = Jarra negra pulida
    """
    numero_inventario = models.PositiveIntegerField()
    nombre = models.CharField(max_length=64)
    naturaleza = models.ForeignKey('Naturaleza', null=True, blank=True)
    forma = models.ForeignKey('Forma', null=True, blank=True)
    color = models.ForeignKey('Color', null=True, blank=True)
    procedencia = models.ForeignKey('Procedencia', null=True, blank=True)

    # fotografias -> FotografiasDePieza

    def __str__(self):
        return "{} - {}".format(self.id, self.nombre)


class FotografiasDePieza(models.Model):
    pieza = models.ForeignKey(Pieza, related_name='fotografias')
    foto = models.FileField(upload_to='pieza/photo/%Y/%m/%d', max_length=768)


class Naturaleza(models.Model):
    """
    Naturaleza de la pieza

    Ej: vasija de cerámica
    """
    nombre = models.CharField(max_length=64)

    def __str__(self):
        return self.nombre


class Forma(models.Model):
    """
    Forma de la pieza

    Ej: jarra
    """
    nombre = models.CharField(max_length=64)

    def __str__(self):
        return self.nombre


class Color(models.Model):
    """
    Color de la pieza

    Ej: negro
    """
    nombre = models.CharField(max_length=64)

    def __str__(self):
        return self.nombre


class Procedencia(models.Model):
    """
    Procedencia de la pieza
    """
    sitio_arqueologico = models.ForeignKey('SitioArqueologico', null=True, blank=True)
    periodo = models.ForeignKey('Periodo', null=True, blank=True)

    def __str__(self):
        return self.nombre


class SitioArqueologico(models.Model):
    """
    Un sitio arqueológico
    """
    nombre = models.CharField(max_length=64)
    sitio_arqueologico = models.ForeignKey('SitioArqueologico', null=True, blank=True)
    coordenada_x = models.FloatField(null=True, blank=True)
    coordenada_y = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class Periodo(models.Model):
    """
    Periodo, fecha, era, etc. (TIEMPO) de la pieza

    Ej: Inca
    """
    nombre = models.CharField(max_length=64)

    def __str__(self):
        return self.nombre
