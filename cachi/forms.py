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
        self.fields['nombre_descriptivo'].widget.attrs['placeholder'] = 'Nombre Descriptivo'

        self.fields['fecha_hallazgo'].widget.attrs['class'] = 'form-control'
        self.fields['fecha_hallazgo'].widget.attrs['type'] = 'date'
        self.fields['fecha_hallazgo'].widget.attrs['placeholder'] = 'Fecha Hallazgo'

        self.fields['forma'].widget.attrs['class'] = 'form-control'
        self.fields['forma'].widget.attrs['placeholder'] = 'Forma'
        self.fields['forma'].widget.attrs['rows'] = '2'

        self.fields['tecnica_manufactura'].widget.attrs['class'] = 'form-control'
        self.fields['tecnica_manufactura'].widget.attrs['placeholder'] = 'Técnica Manufactura'
        self.fields['tecnica_manufactura'].widget.attrs['rows'] = '2'

        self.fields['naturaleza'].widget.attrs['class'] = 'form-control'
        self.fields['naturaleza'].empty_label = 'Naturaleza'

        self.fields['tipo_adquisicion'].widget.attrs['class'] = 'form-control'
        self.fields['tipo_adquisicion'].empty_label = 'Tipo Adquisición'

        self.fields['tipo_condicion_hallazgo'].widget.attrs['class'] = 'form-control'
        self.fields['tipo_condicion_hallazgo'].empty_label = 'Tipo Condición Hallazgo'

        self.fields['persona_colectora'].widget.attrs['class'] = 'form-control'
        self.fields['persona_colectora'].empty_label = 'Persona Colectora'

        self.fields['ubicacion'].widget.attrs['class'] = 'form-control'
        self.fields['ubicacion'].empty_label = 'Ubicación Actual'

    class Meta():
        model = PiezaConjunto

        fields = (
            'nombre_descriptivo',
            'fecha_hallazgo',
            'naturaleza',
            'forma',
            'tecnica_manufactura',
            'fragmentos',
            'tipo_adquisicion',
            'tipo_condicion_hallazgo',
            'persona_colectora',
            'ubicacion',
        )


class FragmentoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FragmentoForm, self).__init__(*args, **kwargs)
        self.fields['numero_inventario'].widget.attrs['class'] = 'form-control'
        self.fields['numero_inventario'].widget.attrs['placeholder'] = 'Número Inventario'

    class Meta():
        model = Fragmento

        fields = (
            'numero_inventario',
        )


class FichaTecnicaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FichaTecnicaForm, self).__init__(*args, **kwargs)
        self.fields['alto'].widget.attrs['class'] = 'form-control'
        self.fields['alto'].widget.attrs['placeholder'] = 'Alto'

        self.fields['peso'].widget.attrs['class'] = 'form-control'
        self.fields['peso'].widget.attrs['placeholder'] = 'Peso'

        self.fields['espesor'].widget.attrs['class'] = 'form-control'
        self.fields['espesor'].widget.attrs['placeholder'] = 'Espesor'

        self.fields['diametro_min'].widget.attrs['class'] = 'form-control'
        self.fields['diametro_min'].widget.attrs['placeholder'] = 'Diámetro Mínimo'

        self.fields['diametro_max'].widget.attrs['class'] = 'form-control'
        self.fields['diametro_max'].widget.attrs['placeholder'] = 'Diámetro Máximo'

        self.fields['color'].widget.attrs['class'] = 'form-control'
        self.fields['color'].widget.attrs['placeholder'] = 'Color'

        self.fields['decoracion'].widget.attrs['class'] = 'form-control'
        self.fields['decoracion'].widget.attrs['placeholder'] = 'Decoración'
        self.fields['decoracion'].widget.attrs['rows'] = '2'

        self.fields['inscripciones_marcas'].widget.attrs['class'] = 'form-control'
        self.fields['inscripciones_marcas'].widget.attrs['placeholder'] = 'Inscripciones Marcas'
        self.fields['inscripciones_marcas'].widget.attrs['rows'] = '2'

        self.fields['reparaciones'].widget.attrs['class'] = 'form-control'
        self.fields['reparaciones'].widget.attrs['placeholder'] = 'Reparaciones'
        self.fields['reparaciones'].widget.attrs['rows'] = '2'

        self.fields['desperfectos'].widget.attrs['class'] = 'form-control'
        self.fields['desperfectos'].widget.attrs['placeholder'] = 'Desperfectos'
        self.fields['desperfectos'].widget.attrs['rows'] = '2'

        self.fields['desperfectos_fabricacion'].widget.attrs['class'] = 'form-control'
        self.fields['desperfectos_fabricacion'].widget.attrs['placeholder'] = 'Desperfectos Fabricación'
        self.fields['desperfectos_fabricacion'].widget.attrs['rows'] = '2'

        self.fields['otras_caracteristicas_distintivas'].widget.attrs['class'] = 'form-control'
        self.fields['otras_caracteristicas_distintivas'].widget.attrs['placeholder'] = 'Otra Caracteristica'
        self.fields['otras_caracteristicas_distintivas'].widget.attrs['rows'] = '2'

        self.fields['tratamiento'].widget.attrs['class'] = 'form-control'
        self.fields['tratamiento'].widget.attrs['placeholder'] = 'Tratamiento'
        self.fields['tratamiento'].widget.attrs['rows'] = '2'

        self.fields['observacion'].widget.attrs['class'] = 'form-control'
        self.fields['observacion'].widget.attrs['placeholder'] = 'Observacion'
        self.fields['observacion'].widget.attrs['rows'] = '2'

        self.fields['autor'].widget.attrs['class'] = 'form-control'
        self.fields['autor'].empty_label = 'Autor'

        self.fields['diagnostico_estado'].widget.attrs['class'] = 'form-control'
        self.fields['diagnostico_estado'].widget.attrs['placeholder'] = 'Diagnóstico Estado Conservación'
        self.fields['diagnostico_estado'].widget.attrs['rows'] = '2'

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


class ProcedenciaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProcedenciaForm, self).__init__(*args, **kwargs)
        self.fields['otra'].widget.attrs['class'] = 'form-control'
        self.fields['otra'].widget.attrs['placeholder'] = 'Otra Ubicación'
        self.fields['otra'].widget.attrs['rows'] = '2'

        self.fields['ubicacion_geografica'].widget.attrs['class'] = 'form-control'
        self.fields['ubicacion_geografica'].empty_label = 'Ubicación Geográfica'

        self.fields['sitio_arqueologico'].widget.attrs['class'] = 'form-control'
        self.fields['sitio_arqueologico'].empty_label = 'Sitio Arqueológico'

    class Meta():
        model = Procedencia

        fields = (
            'sitio_arqueologico',
            'ubicacion_geografica',
            'otra',
        )

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

    adjuntos = MultiFileField(
        max_num=10,
        min_num=1,
        maximum_file_size=1024 * 1024 * 5
    )


class BusquedaPiezaForm(forms.Form):
    # FIXME: no usar objects.all() para obtener queryset. Estos querysets deberian
    # ser devueltos por los managers de los models
    nro_inventario = forms.IntegerField(required=False)
    naturaleza = forms.ModelChoiceField(Naturaleza.objects.all(), required=False)
    sitio_arqueologico = forms.ModelChoiceField(SitioArqueologico.objects.all(), required=False)
    ubicacion = forms.ModelChoiceField(UbicacionGeografica.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        super(BusquedaPiezaForm, self).__init__(*args, **kwargs)
        self.fields['nro_inventario'].widget.attrs['class'] = 'form-control'
        self.fields['nro_inventario'].widget.attrs['placeholder'] = 'Número Inventario'

        self.fields['naturaleza'].widget.attrs['class'] = 'form-control'
        self.fields['naturaleza'].empty_label = 'Naturaleza'

        self.fields['sitio_arqueologico'].widget.attrs['class'] = 'form-control'
        self.fields['sitio_arqueologico'].empty_label = 'Sitio Arqueológico'

        self.fields['ubicacion'].widget.attrs['class'] = 'form-control'
        self.fields['ubicacion'].empty_label = 'Ubicacion Geográfica'
