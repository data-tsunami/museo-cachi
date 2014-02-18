# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class PiezaConjunto(models.Model):
    """
    Una pieza o conjunto de piezas del museo.

    Ej:
    - numero_inventario = 212313
    - nombre = Jarra negra pulida
    """
    numero_inventario = models.PositiveIntegerField()
    nombre_descriptivo = models.CharField(
        max_length=128,
    )
    forma = models.TextField(
        max_length=128,
    )
    tecnica_manufactura = models.TextField(
        max_length=128,
    )
    fecha_hallazgo = models.DateField()
    condicion_hallazgo = models.TextField(
        max_length=128,
    )
    fragmentos = models.BooleanField(
        default=False,
    )
    procedencia = models.ForeignKey(
        'Procedencia',
        null=True,
        blank=True,
    )
    ubicacion = models.ForeignKey(
        'Ubicacion',
        null=True,
        blank=True,
    )
    tipo_adquisicion = models.ForeignKey(
        'TipoAdquisicion',
        null=True,
        blank=True,
    )
    tipo_condicion_hallazgo = models.ForeignKey(
        'TipoCondicionHallazgo',
        null=True,
        blank=True,
    )
    naturaleza = models.ForeignKey(
        'Naturaleza',
    )
    persona_colectora = models.ForeignKey(
        'Persona',
        null=True,
        blank=True,
    )
    adjuntos = models.ForeignKey(
        'Adjunto',
        null=True,
        blank=True,
    )

    def __unicode__(self):
        return u'{0}, {1}'.format(
            self.numero_inventario,
            self.nombre_descriptivo,
        )


class Adjunto(models.Model):
    """
    Adjuntos que puedan contener alguno
    de los objetos.

    Ej: fotos, pdf
    """
    nombre_archivo = models.CharField(
        max_length=128,
    )
    content_type = models.CharField(
        max_length=64,
    )
    ubicacion_filesystem = models.CharField(
        max_length=64,
    )
    tipo = models.CharField(
        max_length=64,
    )
    adjunto = models.FileField(
        upload_to='pieza/photo/%Y/%m/%d',
        max_length=768,
    )
    pieza_conjunto = models.ForeignKey(
        'PiezaConjunto',
        null=True,
        blank=True,
    )
    ficha_tecnica = models.ForeignKey(
        'FichaTecnica',
        null=True,
        blank=True,
    )
    diagnostico_estado_conservacion = models.ForeignKey(
        'DiagnosticoEstadoConservacion',
        null=True,
        blank=True,
    )
    ficha_relevamiento_sitio = models.ForeignKey(
        'FichaRelevamientoSitio',
        null=True,
        blank=True,
    )
    informe_campo = models.ForeignKey(
        'InformeCampo',
        null=True,
        blank=True,
    )


class TipoAdquisicion(models.Model):
    """
    Tipo de Adquisición de la pieza.

    Ej: Donación.
    """
    nombre = models.CharField(
        max_length=64,
    )

    def __unicode__(self):
        return self.nombre


class TipoCondicionHallazgo(models.Model):
    """
    Tipo de condición de condicion_de_hallazgo
    de la pieza.

    Ej: ??.
    """
    nombre = models.CharField(
        max_length=64,
    )

    def __unicode__(self):
        return self.nombre


class Naturaleza(models.Model):
    """
    Naturaleza de la pieza.

    Ej: vasija de cerámica
    """
    nombre = models.CharField(
        max_length=64,
    )

    def __unicode__(self):
        return self.nombre


class Persona(models.Model):
    """
    Personas involucradas de alguna
    manera en algún dato.

    Ej: Pio Pablo Dias
    """
    nombre = models.CharField(
        max_length=64
    )
    apellido = models.CharField(
        max_length=64
    )
    user = models.OneToOneField(
        User,
        unique=True,
    )

    def __unicode__(self):
        return self.nombre


class Ubicacion(models.Model):
    """
    Ubicación actual de la pieza.

    Ej: Area de Reserva, Area de Investigación
    En Préstamo, Exposición.
    """
    nombre = models.CharField(max_length=64)

    def __unicode__(self):
        return self.nombre


class FichaTecnica(models.Model):
    """
    La ficha de características técnicas
    de una pieza o parte de un conjunto.

    Ej: color, peso.
    """

    alto = models.PositiveIntegerField()
    peso = models.PositiveIntegerField()
    espesor = models.PositiveIntegerField()
    diametro_min = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    diametro_max = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    color = models.CharField(
        max_length=64,
    )
    decoracion = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )
    inscripciones_marcas = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )
    reparaciones = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )
    desperfectos = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )
    desperfectos_fabricacion = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )
    otras_caracteristicas_distintivas = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )
    tratamiento = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )
    observacion = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )
    adjuntos = models.ForeignKey(
        'Adjunto',
        null=True,
        blank=True,
    )
    pieza_conjunto = models.ForeignKey(
        'PiezaConjunto',
    )

    def __unicode__(self):
        return u'{0}, {1}'.format(
            self.numero_inventario,
            self.nombre_descriptivo,
        )


class DiagnosticoEstadoConservacion(models.Model):
    fecha = models.DateField()
    descripcion = models.TextField(
        null=True,
        blank=True,
    )
    autor = models.ForeignKey(
       'Persona',
        null=True,
        blank=True,
    )
    adjuntos = models.ForeignKey(
        'Adjunto',
        null=True,
        blank=True,
    )


class InformeCampo(models.Model):
    """
    Informe de Campo.
    """
    fecha = models.DateField()
    sitio_aqueologico = models.ForeignKey(
        "SitioArqueologico",
        null=True,
        blank=True,
    )
    autor = models.ForeignKey(
        'Persona',
    )
    adjuntos = models.ForeignKey(
        'Adjunto',
        null=True,
        blank=True,
    )


class UbicacionGeografica(models.Model):
    """
    Ubicación geográfica.

    Ej: Pais, Provincia
    """
    nombre = models.CharField(
        max_length=64,
    )
    padre = models.ForeignKey(
        'self',
        null=True,
        blank=True,
    )

    def __unicode__(self):
        return self.nombre


class Procedencia(models.Model):
    """
    Procedencia de una pieza.
    """
    otra = models.CharField(
        max_length=64,
    )
    sitio_aqueologico = models.ForeignKey(
        "SitioArqueologico",
        null=True,
        blank=True,
    )
    ubicacion_geografica = models.ForeignKey(
        "UbicacionGeografica",
        null=True,
        blank=True,
    )


class SitioArqueologico(models.Model):
    """
    Un sitio arqueológico.

    Ej: SSalCac 91 Salvatierra
    """
    nombre = models.CharField(
        max_length=64,
    )
    coordenada_x = models.FloatField(
        null=True,
        blank=True,
    )
    coordenada_y = models.FloatField(
        null=True,
        blank=True,
    )
    ubicacion_geografica = models.ForeignKey(
        "UbicacionGeografica",
    )

    def __unicode__(self):
        return self.nombre


class FichaRelevamientoSitio(models.Model):
    """
    Relevamiento de sitio arqueológico.
    """
    fecha = models.DateField()
    autor = models.ForeignKey(
        'Persona',
    )
    adjuntos = models.ForeignKey(
        'Adjunto',
        null=True,
        blank=True,
    )


class Modificacion(models.Model):
    """
    Modificaciones que se haya realizado
    en algunos de los objetos.

    Ej: cambio del numero_de_inventario,
    alta de nueva FichaTecnica,
    alta de nuevo SitioArqueologico.
    """
    fecha = models.DateField()
    atributo = models.CharField(
        max_length=128,
    )
    valor_viejo = models.CharField(
        max_length=128,
    )
    valor_nuevo = models.CharField(
        max_length=128,
    )
    pieza_conjunto = models.ForeignKey(
        'PiezaConjunto',
        null=True,
        blank=True,
    )
    ficha_tecnica = models.ForeignKey(
        'FichaTecnica',
        null=True,
        blank=True,
    )
    diagnostico_estado_conservacion = models.ForeignKey(
        'DiagnosticoEstadoConservacion',
        null=True,
        blank=True,
    )
    sitio_aqueologico = models.ForeignKey(
        'SitioArqueologico',
        null=True,
        blank=True,
    )
