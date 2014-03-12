# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from cachi.validators import validador_cantidad_fragmentos
from django.contrib.auth.models import User
from django.db import models
from django.http import Http404


RAZON_ACTUALIZACION_CREACION = 1
RAZON_ACTUALIZACION_ACTUALIZACION = 2
RAZON_ACTUALIZACION_DIAGNOSTICO = 3
RAZON_ACTUALIZACION = (
    (RAZON_ACTUALIZACION_CREACION, 'Creación'),
    (RAZON_ACTUALIZACION_ACTUALIZACION, 'Actualización Datos'),
    (RAZON_ACTUALIZACION_DIAGNOSTICO, 'Diagnóstico Estado Conservación'),
)


class PiezaConjuntoManager(models.Manager):

    def buscar_piezas(self, nro_inventario, naturaleza, sitio_arqueologico, ubicacion_geografica):
        if nro_inventario:
            try:
                return self.filter(numero_inventario=nro_inventario).distinct()
            except PiezaConjunto.DoesNotExist:
                return self.none()
        qs = self.select_related('fragmentos_pieza_conjunto').all()
        if naturaleza:
            qs = qs.filter(naturaleza=naturaleza)
        if sitio_arqueologico:
            qs = qs.filter(procedencia__sitio_arqueologico=sitio_arqueologico)
        if ubicacion_geografica:
            qs = qs.filter(procedencia__ubicacion_geografica=ubicacion_geografica)
        return qs


class PiezaConjunto(models.Model):
    """
    Una pieza o conjunto de piezas del museo.
    """
    numero_inventario = models.PositiveIntegerField()
    nombre_descriptivo = models.CharField(
        max_length=128,
    )
    forma = models.TextField(
        max_length=128,
    )
    tecnica_manufactura = models.TextField(
        null=True,
        blank=True,
    )
    fecha_hallazgo = models.DateField()
    condicion_hallazgo = models.TextField(
        null=True,
        blank=True,
    )
    cantidad_fragmentos = models.PositiveIntegerField(
        default=1,
        validators=[validador_cantidad_fragmentos]
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

    objects = PiezaConjuntoManager()

    def __unicode__(self):
        if self.cantidad_fragmentos == 1:
            return u"Pieza '{0}'".format(
                self.nombre_descriptivo,
            )
        else:
            return u"Conjunto '{0}' ({1} fragmentos)".format(
                self.nombre_descriptivo,
                self.cantidad_fragmentos
            )

    def obtiene_procedencia(self):
        try:
            return self.procedencia
        except Procedencia.DoesNotExist:
            raise Http404

    def obtiene_adjuntos(self):
        return self.adjunto_pieza_conjunto.all()

    def obtiene_fragmentos(self):
        return self.fragmentos_pieza_conjunto.all()

    def get_pieza_o_conjunto(self):
        if type(self.cantidad_fragmentos) == int:
            if self.cantidad_fragmentos == 1:
                return u"Pieza"
            else:
                return u"Conjunto"
        return u"Pieza o conjunto"


class Fragmento(models.Model):
    """
    Fragmentos de una pieza en caso de tenerlos, o,
    fragmento único, en caso de pieza entera.
    """
    ultima_version = models.ForeignKey(
        'FichaTecnica',
        null=True,
        blank=True,
        related_name='ultima_version',
    )
    pieza_conjunto = models.ForeignKey(
        'PiezaConjunto',
        related_name='fragmentos_pieza_conjunto'
    )

    def __unicode__(self):
        return u'Frag@{0}'.format(
            self.id,
        )

    def get_identificador(self):
        return u'#{0}#'.format(
            self.id,
        )

    def obtiene_ficha_tecnica(self):
        return self.ultima_version

    def obtiene_ficha_tecnica_diagnostico(self, ficha_tecnica_pk):
        return self.fichas_tecnicas.get(
            pk=ficha_tecnica_pk,
        )

    def obtiene_fichas_tecnicas_diagnosticos(self):
        return self.fichas_tecnicas.filter(
            razon_actualizacion=RAZON_ACTUALIZACION_DIAGNOSTICO,
        ).order_by('-fecha')

    def obtiene_ficha_tecnica_ultimo_diagnostico(self):
        return self.fichas_tecnicas.filter(
            razon_actualizacion=RAZON_ACTUALIZACION_DIAGNOSTICO,
        ).order_by('fecha').last()


class FichaTecnica(models.Model):
    """
    La ficha de características técnicas
    de una pieza o parte de un conjunto.
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
    decoracion = models.TextField(
        null=True,
        blank=True,
    )
    inscripciones_marcas = models.TextField(
        null=True,
        blank=True,
    )
    reparaciones = models.TextField(
        null=True,
        blank=True,
    )
    desperfectos = models.TextField(
        null=True,
        blank=True,
    )
    desperfectos_fabricacion = models.TextField(
        null=True,
        blank=True,
    )
    otras_caracteristicas_distintivas = models.TextField(
        null=True,
        blank=True,
    )
    tratamiento = models.TextField(
        null=True,
        blank=True,
    )
    observacion = models.TextField(
        null=True,
        blank=True,
    )
    diagnostico_estado = models.TextField(
        null=True,
        blank=True,
    )
    razon_actualizacion = models.PositiveIntegerField(
        choices=RAZON_ACTUALIZACION,
    )
    fecha = models.DateField()
    autor = models.ForeignKey(
        'Persona',
        null=True,
        blank=True,
    )
    usuario = models.ForeignKey(
        User,
    )
    fragmento = models.ForeignKey(
        'Fragmento',
        related_name='fichas_tecnicas'
    )

    def __unicode__(self):
        return u'{0}'.format(
            self.color,
        )

    def obtiene_adjuntos(self):
        return self.adjunto_ficha_tecnica.all()


class Adjunto(models.Model):
    """
    Adjuntos que puedan contener alguno
    de los objetos.
    """
    nombre_archivo = models.CharField(
        max_length=128,
    )
    content_type = models.CharField(
        max_length=64,
    )
    size = models.CharField(
        max_length=64,
        null=True,
        blank=True,
    )
    tipo = models.CharField(
        max_length=64,
    )
    adjunto = models.FileField(
        upload_to='pieza/adjunto/%Y/%m/%d',
        max_length=768,
    )
    pieza_conjunto = models.ForeignKey(
        'PiezaConjunto',
        related_name='adjunto_pieza_conjunto',
        null=True,
        blank=True,
    )
    fragmento = models.ForeignKey(
        'Fragmento',
        related_name='adjunto_fragmento',
        null=True,
        blank=True,
    )
    ficha_tecnica = models.ForeignKey(
        'FichaTecnica',
        related_name='adjunto_ficha_tecnica',
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

    def __unicode__(self):
        return u'{0}'.format(
            self.nombre_archivo,
        )


class TipoAdquisicion(models.Model):
    """
    Tipo de Adquisición de la pieza.
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
    """
    nombre = models.CharField(
        max_length=64,
    )

    def __unicode__(self):
        return self.nombre


class Naturaleza(models.Model):
    """
    Naturaleza de la pieza.
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
        null=True,
        blank=True,
    )

    def __unicode__(self):
        return self.nombre


class Ubicacion(models.Model):
    """
    Ubicación actual de la pieza.
    Podría ser Area de Reserva,
    Area de Investigación,
    En Préstamo, Exposición.
    """
    nombre = models.CharField(max_length=64)

    def __unicode__(self):
        return self.nombre


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
        if self.padre:
            return "{0} ({1})".format(
                self.nombre,
                self.padre.nombre,
            )
        else:
            return self.nombre


class Procedencia(models.Model):
    """
    Procedencia de una pieza.
    """
    otra = models.CharField(
        max_length=64,
        null=True,
        blank=True,
    )
    sitio_arqueologico = models.ForeignKey(
        "SitioArqueologico",
        null=True,
        blank=True,
    )
    ubicacion_geografica = models.ForeignKey(
        "UbicacionGeografica",
        null=True,
        blank=True,
    )
    pieza_conjunto = models.OneToOneField(
        'PiezaConjunto',
        related_name='procedencia',
    )

    def __unicode__(self):
        if self.sitio_arqueologico:
            return "Sitio: {0}".format(self.sitio_arqueologico.nombre)
        elif self.ubicacion_geografica:
            return "Ubicacion: {0}".format(self.ubicacion_geografica.nombre)
        else:
            return "Otra: {0}".format(self.otra)


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
    sitio_aqueologico = models.ForeignKey(
        'SitioArqueologico',
        null=True,
        blank=True,
    )
