# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django import forms

from cachi.fields import (
    MultiFileField,
)
from cachi.models import (
    FichaTecnica,
    Fragmento,
    PiezaConjunto,
    Procedencia,
    Naturaleza,
    UbicacionGeografica,
    SitioArqueologico
)


class PiezaConjuntoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PiezaConjuntoForm, self).__init__(*args, **kwargs)
        self.fields['nombre_descriptivo'].widget.attrs['class'] = 'form-control'
        self.fields['nombre_descriptivo'].widget.attrs['title'] = \
        'Ingrese un nombre descriptivo con el que se referencie a la pieza. Ejemplo: Jarra Cuadrada.'

        self.fields['fecha_hallazgo'].widget.attrs['class'] = 'form-control'
        self.fields['fecha_hallazgo'].widget.attrs['type'] = 'date'
        self.fields['fecha_hallazgo'].widget.attrs['title'] = \
        'Ingrese la fecha de hallazgo de la pieza. Ejemplo: 09/06/1984.'

        self.fields['forma'].widget.attrs['class'] = 'form-control'
        self.fields['forma'].widget.attrs['rows'] = '2'
        self.fields['forma'].widget.attrs['title'] = \
        'Ingrese un breve detalle de la forma de la pieza. Ejemplo: Tubo. Fragmento de seccn circular.'

        self.fields['tecnica_manufactura'].widget.attrs['class'] = 'form-control'
        self.fields['tecnica_manufactura'].widget.attrs['rows'] = '2'
        self.fields['tecnica_manufactura'].widget.attrs['title'] = \
        'Ingrese la técnica de manufactura de la pieza.'

        self.fields['naturaleza'].widget.attrs['class'] = 'form-control'
        self.fields['naturaleza'].widget.attrs['title'] = \
        'Ingrese la naturaleza de fabricación de la pieza. Ejemplo: Cerámica.'

        self.fields['tipo_adquisicion'].widget.attrs['class'] = 'form-control'
        self.fields['tipo_adquisicion'].widget.attrs['title'] = \
        'Ingrese el tipo de adquisición de la pieza. Ejemplo: Donación.'

        self.fields['tipo_condicion_hallazgo'].widget.attrs['class'] = 'form-control'
        self.fields['tipo_condicion_hallazgo'].widget.attrs['title'] = \
        'Ingrese la condición de hallazgo de la pieza. Ejemplo: Recolección Superficial.'

        self.fields['persona_colectora'].widget.attrs['class'] = 'form-control'
        self.fields['persona_colectora'].widget.attrs['title'] = \
        'Seleccione la persona que recolecto de la pieza. Ejemplo: Pio Pablo Diaz.'

        self.fields['ubicacion'].widget.attrs['class'] = 'form-control'
        self.fields['ubicacion'].widget.attrs['title'] = \
        'Seleccione la ubicación actual de la pieza. Ejemplo: Almacén - Estantería A5.'

        self.fields['cantidad_fragmentos'].widget.attrs['class'] = 'form-control'
        self.fields['cantidad_fragmentos'].widget.attrs['title'] = \
            'Ingrese la cantidad de fragmentos del conjunto.'

    class Meta():
        model = PiezaConjunto

        fields = (
            'nombre_descriptivo',
            'fecha_hallazgo',
            'naturaleza',
            'forma',
            'tecnica_manufactura',
            'tipo_adquisicion',
            'tipo_condicion_hallazgo',
            'persona_colectora',
            'ubicacion',
            'cantidad_fragmentos',
        )
        labels = {
            'nombre_descriptivo': 'Nombre Descriptivo',
            'fecha_hallazgo': 'Fecha Hallazgo (09/06/1984)',
            'naturaleza': 'Naturaleza',
            'forma': 'Forma',
            'tecnica_manufactura': 'Técnica Manufactura',
            'tipo_adquisicion': 'Tipo Adquisición',
            'tipo_condicion_hallazgo': 'Tipo Condición Hallazgo',
            'persona_colectora': 'Persona Colectora',
            'ubicacion': 'Ubicación Actual',
            'cantidad_fragmentos': 'Cantidad de fragmentos',
        }


class FragmentoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FragmentoForm, self).__init__(*args, **kwargs)
        self.fields['numero_inventario'].widget.attrs['class'] = 'form-control'
        self.fields['numero_inventario'].widget.attrs['title'] = \
        'Especifique el Número de Inventario pieza o fragmento. Ejemplo: 1165.'

    class Meta():
        model = Fragmento

        fields = (
            'numero_inventario',
        )
        labels = {
            'numero_inventario': 'Número Inventario',
        }


class FichaTecnicaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FichaTecnicaForm, self).__init__(*args, **kwargs)
        self.fields['alto'].widget.attrs['class'] = 'form-control'
        self.fields['alto'].widget.attrs['title'] = \
        'Especifique el alto en milímetros (mm) de la pieza o fragmento. Ejemplo: 125.'

        self.fields['peso'].widget.attrs['class'] = 'form-control'
        self.fields['peso'].widget.attrs['title'] = \
        'Especifique el peso en gramos (g) de la pieza o fragmento. Ejemplo: 1050.'

        self.fields['espesor'].widget.attrs['class'] = 'form-control'
        self.fields['espesor'].widget.attrs['title'] = \
        'Especifique el espesor en milímetros (mm) de la pieza o fragmento. Ejemplo: 15.'

        self.fields['diametro_min'].widget.attrs['class'] = 'form-control'
        self.fields['diametro_min'].widget.attrs['title'] = \
        'Especifique el diámetro mínimo en milímetros (mm) de la pieza o fragmento. Ejemplo: 1250.'

        self.fields['diametro_max'].widget.attrs['class'] = 'form-control'
        self.fields['diametro_max'].widget.attrs['title'] = \
        'Especifique el diámetro máximo en milímetros (mm) de la pieza o fragmento. Ejemplo: 1500.'

        self.fields['color'].widget.attrs['class'] = 'form-control'
        self.fields['color'].widget.attrs['title'] = \
        'Especifique el color de la pieza o fragmento. Ejemplo: Negro.'

        self.fields['decoracion'].widget.attrs['class'] = 'form-control'
        self.fields['decoracion'].widget.attrs['rows'] = '2'
        self.fields['decoracion'].widget.attrs['title'] = \
        'Especifique si la pieza o fragmento tiene alguna decoración.'

        self.fields['inscripciones_marcas'].widget.attrs['class'] = 'form-control'
        self.fields['inscripciones_marcas'].widget.attrs['rows'] = '2'
        self.fields['inscripciones_marcas'].widget.attrs['title'] = \
        'Especifique si la pieza o fragmento tiene alguna inscripción o marca que la distinga.'

        self.fields['reparaciones'].widget.attrs['class'] = 'form-control'
        self.fields['reparaciones'].widget.attrs['rows'] = '2'
        self.fields['reparaciones'].widget.attrs['title'] = \
        'Especifique si la pieza o fragmento tiene efectuada alguna reparación.'

        self.fields['desperfectos'].widget.attrs['class'] = 'form-control'
        self.fields['desperfectos'].widget.attrs['rows'] = '2'
        self.fields['desperfectos'].widget.attrs['title'] = \
        'Especifique si la pieza o fragmento tiene algún desperfecto.'

        self.fields['desperfectos_fabricacion'].widget.attrs['class'] = 'form-control'
        self.fields['desperfectos_fabricacion'].widget.attrs['rows'] = '2'
        self.fields['desperfectos_fabricacion'].widget.attrs['title'] = \
        'Especifique si la pieza o fragmento tiene algún desperfecto de fabricación.'

        self.fields['otras_caracteristicas_distintivas'].widget.attrs['class'] = 'form-control'
        self.fields['otras_caracteristicas_distintivas'].widget.attrs['rows'] = '2'
        self.fields['otras_caracteristicas_distintivas'].widget.attrs['title'] = \
        'Especifique alguna otra carcterística distintiva de la pieza o fragmento.'

        self.fields['tratamiento'].widget.attrs['class'] = 'form-control'
        self.fields['tratamiento'].widget.attrs['rows'] = '2'
        self.fields['tratamiento'].widget.attrs['title'] = \
        'Especifique si la pieza o fragmento tiene realizado algún tratamiento en paticular.'

        self.fields['observacion'].widget.attrs['class'] = 'form-control'
        self.fields['observacion'].widget.attrs['rows'] = '2'
        self.fields['observacion'].widget.attrs['title'] = \
        'Especifique alguna otra observación de la pieza o fragmento.'

        self.fields['autor'].widget.attrs['class'] = 'form-control'
        self.fields['autor'].widget.attrs['title'] = \
        'Seleccione el autor de la Ficha Técnica.'

        self.fields['diagnostico_estado'].widget.attrs['class'] = 'form-control'
        self.fields['diagnostico_estado'].widget.attrs['rows'] = '2'
        self.fields['diagnostico_estado'].widget.attrs['title'] = \
        'Especifique detalladamente el Diagnóstico de Estado que se le realizó a la pieza o fragmento.'

    class Meta():
        model = FichaTecnica

        fields = (
            'alto',
            'peso',
            'espesor',
            'diametro_min',
            'diametro_max',
            'color',
            'decoracion',
            'inscripciones_marcas',
            'reparaciones',
            'desperfectos',
            'desperfectos_fabricacion',
            'otras_caracteristicas_distintivas',
            'tratamiento',
            'observacion',
            'diagnostico_estado',
            'autor',
        )
        labels = {
            'alto': 'Alto (mm)',
            'peso': 'Peso (g)',
            'espesor': 'Espesor (mm)',
            'diametro_max': 'Diámetro Mínimo (mm)',
            'diametro_min': 'Diámetro Máximo (mm)',
            'color': 'Color',
            'decoracion': 'Decoración',
            'inscripciones_marcas': 'Inscripciones Marcas',
            'reparaciones': 'Reparaciones',
            'desperfectos': 'Desperfectos',
            'desperfectos_fabricacion': 'Desperfectos Fabricación',
            'otras_caracteristicas_distintivas': 'Otras Característica Distintivas',
            'tratamiento': 'Tratamiento',
            'observacion': 'Observación',
            'diagnostico_estado': 'Diagnóstico Estado',
            'autor': 'Autor',
        }


class ProcedenciaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProcedenciaForm, self).__init__(*args, **kwargs)
        self.fields['otra'].widget.attrs['class'] = 'form-control'
        self.fields['otra'].widget.attrs['rows'] = '2'
        self.fields['otra'].widget.attrs['title'] = \
        'Seleccione Sitio Arqueológico o Ubicacion Geográfica o especifique una procedencia distinta.'

        self.fields['ubicacion_geografica'].widget.attrs['class'] = 'form-control'
        self.fields['ubicacion_geografica'].widget.attrs['title'] = \
        'Seleccione Sitio Arqueológico o Ubicacion Geográfica o especifique una procedencia distinta.'

        self.fields['sitio_arqueologico'].widget.attrs['class'] = 'form-control'
        self.fields['sitio_arqueologico'].widget.attrs['title'] = \
        'Seleccione Sitio Arqueológico o Ubicacion Geográfica o especifique una procedencia distinta.'

    class Meta():
        model = Procedencia

        fields = (
            'sitio_arqueologico',
            'ubicacion_geografica',
            'otra',
        )
        labels = {
            'sitio_arqueologico': 'Sitio Arqueológico',
            'ubicacion_geografica': 'Ubicación Geográfica',
            'otra': 'Otra',
        }

    def clean(self):
        cleaned_data = super(ProcedenciaForm, self).clean()

        validate = False
        for key, value in cleaned_data.items():
            if value:
                validate = True

        if not validate:
            raise forms.ValidationError(
                "Tiene que seleccionar al menos una Procedencia.",
            )

        return cleaned_data


class AdjuntoForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(AdjuntoForm, self).__init__(*args, **kwargs)
        self.fields['adjuntos'].widget.attrs['class'] = 'form-control adjuntos'
        self.fields['adjuntos'].widget.attrs['title'] = \
        'Haga click en el botón Elegir Archivos y búsque en su PC el o los archivo/s que desee adjuntar.\
        Una vez seleccionado/s se previsualizarán en la pantalla del sistema, haciendo click en Guardar\
        se asociarán a la pieza o fragmento y se guardarán en el sistema.'

    adjuntos = MultiFileField(
        max_num=10,
        min_num=1,
        maximum_file_size=1024 * 1024 * 5
    )


class BusquedaPiezaForm(forms.Form):
    # FIXME: no usar objects.all() para obtener queryset. Estos querysets deberian
    # ser devueltos por los managers de los models
    nro_inventario = forms.IntegerField(
        required=False,
        label='Número Inventario',
    )
    naturaleza = forms.ModelChoiceField(
        Naturaleza.objects.all(),
        required=False,
)
    sitio_arqueologico = forms.ModelChoiceField(
        SitioArqueologico.objects.all(),
        required=False,
    )
    ubicacion = forms.ModelChoiceField(
        UbicacionGeografica.objects.all(),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(BusquedaPiezaForm, self).__init__(*args, **kwargs)
        self.fields['nro_inventario'].widget.attrs['class'] = 'form-control'
        self.fields['nro_inventario'].widget.attrs['title'] = \
        'Especifique el número de inventario para realizar la búsqueda de la pieza específica.'

        self.fields['naturaleza'].widget.attrs['class'] = 'form-control'
        self.fields['naturaleza'].label = 'Naturaleza'
        self.fields['naturaleza'].widget.attrs['title'] = \
        'Seleccione la naturaleza para realizar una búsqueda filtrando las piezas con esta carcterística.'

        self.fields['sitio_arqueologico'].widget.attrs['class'] = 'form-control'
        self.fields['sitio_arqueologico'].label = 'Sitio Arqueológico'
        self.fields['sitio_arqueologico'].widget.attrs['title'] = \
        'Seleccione el sitio arqueológico para realizar una búsqueda filtrando las piezas de este lugar.'

        self.fields['ubicacion'].widget.attrs['class'] = 'form-control'
        self.fields['ubicacion'].label = 'Ubicacion Geográfica'
        self.fields['ubicacion'].widget.attrs['title'] = \
        'Seleccione la ubicación geográfica para realizar una búsqueda filtrando las piezas de este lugar.'
