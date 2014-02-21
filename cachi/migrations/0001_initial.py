# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PiezaConjunto'
        db.create_table(u'cachi_piezaconjunto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_descriptivo', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('forma', self.gf('django.db.models.fields.TextField')(max_length=128)),
            ('tecnica_manufactura', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('fecha_hallazgo', self.gf('django.db.models.fields.DateField')()),
            ('condicion_hallazgo', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('fragmentos', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ubicacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cachi.Ubicacion'], null=True, blank=True)),
            ('tipo_adquisicion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cachi.TipoAdquisicion'], null=True, blank=True)),
            ('tipo_condicion_hallazgo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cachi.TipoCondicionHallazgo'], null=True, blank=True)),
            ('naturaleza', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cachi.Naturaleza'])),
            ('persona_colectora', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cachi.Persona'], null=True, blank=True)),
        ))
        db.send_create_signal(u'cachi', ['PiezaConjunto'])

        # Adding model 'Fragmento'
        db.create_table(u'cachi_fragmento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero_inventario', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('ultima_version', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'ultima_version', to=orm['cachi.FichaTecnica'])),
            ('pieza_conjunto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cachi.PiezaConjunto'])),
        ))
        db.send_create_signal(u'cachi', ['Fragmento'])

        # Adding model 'FichaTecnica'
        db.create_table(u'cachi_fichatecnica', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alto', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('peso', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('espesor', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('diametro_min', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('diametro_max', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('decoracion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('inscripciones_marcas', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('reparaciones', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('desperfectos', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('desperfectos_fabricacion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('otras_caracteristicas_distintivas', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tratamiento', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('observacion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('razon_actualizacion', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('autor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cachi.Persona'], null=True, blank=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('fragmento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cachi.Fragmento'])),
        ))
        db.send_create_signal(u'cachi', ['FichaTecnica'])

        # Adding model 'Adjunto'
        db.create_table(u'cachi_adjunto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_archivo', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('content_type', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('ubicacion_filesystem', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('adjunto', self.gf('django.db.models.fields.files.FileField')(max_length=768)),
            ('pieza_conjunto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cachi.PiezaConjunto'], null=True, blank=True)),
            ('fragmento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cachi.Fragmento'], null=True, blank=True)),
            ('ficha_tecnica', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cachi.FichaTecnica'], null=True, blank=True)),
            ('ficha_relevamiento_sitio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cachi.FichaRelevamientoSitio'], null=True, blank=True)),
            ('informe_campo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cachi.InformeCampo'], null=True, blank=True)),
        ))
        db.send_create_signal(u'cachi', ['Adjunto'])

        # Adding model 'TipoAdquisicion'
        db.create_table(u'cachi_tipoadquisicion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'cachi', ['TipoAdquisicion'])

        # Adding model 'TipoCondicionHallazgo'
        db.create_table(u'cachi_tipocondicionhallazgo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'cachi', ['TipoCondicionHallazgo'])

        # Adding model 'Naturaleza'
        db.create_table(u'cachi_naturaleza', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'cachi', ['Naturaleza'])

        # Adding model 'Persona'
        db.create_table(u'cachi_persona', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal(u'cachi', ['Persona'])

        # Adding model 'Ubicacion'
        db.create_table(u'cachi_ubicacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'cachi', ['Ubicacion'])

        # Adding model 'InformeCampo'
        db.create_table(u'cachi_informecampo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('sitio_aqueologico', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cachi.SitioArqueologico'], null=True, blank=True)),
            ('autor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cachi.Persona'])),
            ('adjuntos', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cachi.Adjunto'], null=True, blank=True)),
        ))
        db.send_create_signal(u'cachi', ['InformeCampo'])

        # Adding model 'UbicacionGeografica'
        db.create_table(u'cachi_ubicaciongeografica', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('padre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cachi.UbicacionGeografica'], null=True, blank=True)),
        ))
        db.send_create_signal(u'cachi', ['UbicacionGeografica'])

        # Adding model 'Procedencia'
        db.create_table(u'cachi_procedencia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('otra', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('sitio_arqueologico', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cachi.SitioArqueologico'], null=True, blank=True)),
            ('ubicacion_geografica', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cachi.UbicacionGeografica'], null=True, blank=True)),
            ('pieza_conjunto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cachi.PiezaConjunto'])),
        ))
        db.send_create_signal(u'cachi', ['Procedencia'])

        # Adding model 'SitioArqueologico'
        db.create_table(u'cachi_sitioarqueologico', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('coordenada_x', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('coordenada_y', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('ubicacion_geografica', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cachi.UbicacionGeografica'])),
        ))
        db.send_create_signal(u'cachi', ['SitioArqueologico'])

        # Adding model 'FichaRelevamientoSitio'
        db.create_table(u'cachi_ficharelevamientositio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('autor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cachi.Persona'])),
            ('adjuntos', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cachi.Adjunto'], null=True, blank=True)),
        ))
        db.send_create_signal(u'cachi', ['FichaRelevamientoSitio'])

        # Adding model 'Modificacion'
        db.create_table(u'cachi_modificacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('atributo', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('valor_viejo', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('valor_nuevo', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('pieza_conjunto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cachi.PiezaConjunto'], null=True, blank=True)),
            ('ficha_tecnica', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cachi.FichaTecnica'], null=True, blank=True)),
            ('sitio_aqueologico', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cachi.SitioArqueologico'], null=True, blank=True)),
        ))
        db.send_create_signal(u'cachi', ['Modificacion'])


    def backwards(self, orm):
        # Deleting model 'PiezaConjunto'
        db.delete_table(u'cachi_piezaconjunto')

        # Deleting model 'Fragmento'
        db.delete_table(u'cachi_fragmento')

        # Deleting model 'FichaTecnica'
        db.delete_table(u'cachi_fichatecnica')

        # Deleting model 'Adjunto'
        db.delete_table(u'cachi_adjunto')

        # Deleting model 'TipoAdquisicion'
        db.delete_table(u'cachi_tipoadquisicion')

        # Deleting model 'TipoCondicionHallazgo'
        db.delete_table(u'cachi_tipocondicionhallazgo')

        # Deleting model 'Naturaleza'
        db.delete_table(u'cachi_naturaleza')

        # Deleting model 'Persona'
        db.delete_table(u'cachi_persona')

        # Deleting model 'Ubicacion'
        db.delete_table(u'cachi_ubicacion')

        # Deleting model 'InformeCampo'
        db.delete_table(u'cachi_informecampo')

        # Deleting model 'UbicacionGeografica'
        db.delete_table(u'cachi_ubicaciongeografica')

        # Deleting model 'Procedencia'
        db.delete_table(u'cachi_procedencia')

        # Deleting model 'SitioArqueologico'
        db.delete_table(u'cachi_sitioarqueologico')

        # Deleting model 'FichaRelevamientoSitio'
        db.delete_table(u'cachi_ficharelevamientositio')

        # Deleting model 'Modificacion'
        db.delete_table(u'cachi_modificacion')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'cachi.adjunto': {
            'Meta': {'object_name': 'Adjunto'},
            'adjunto': ('django.db.models.fields.files.FileField', [], {'max_length': '768'}),
            'content_type': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'ficha_relevamiento_sitio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cachi.FichaRelevamientoSitio']", 'null': 'True', 'blank': 'True'}),
            'ficha_tecnica': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cachi.FichaTecnica']", 'null': 'True', 'blank': 'True'}),
            'fragmento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cachi.Fragmento']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informe_campo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cachi.InformeCampo']", 'null': 'True', 'blank': 'True'}),
            'nombre_archivo': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'pieza_conjunto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cachi.PiezaConjunto']", 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'ubicacion_filesystem': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'cachi.ficharelevamientositio': {
            'Meta': {'object_name': 'FichaRelevamientoSitio'},
            'adjuntos': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cachi.Adjunto']", 'null': 'True', 'blank': 'True'}),
            'autor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cachi.Persona']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'cachi.fichatecnica': {
            'Meta': {'object_name': 'FichaTecnica'},
            'alto': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'autor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cachi.Persona']", 'null': 'True', 'blank': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'decoracion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'desperfectos': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'desperfectos_fabricacion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'diametro_max': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'diametro_min': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'espesor': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'fragmento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cachi.Fragmento']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inscripciones_marcas': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'observacion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'otras_caracteristicas_distintivas': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'peso': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'razon_actualizacion': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'reparaciones': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'tratamiento': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'cachi.fragmento': {
            'Meta': {'object_name': 'Fragmento'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero_inventario': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'pieza_conjunto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cachi.PiezaConjunto']"}),
            'ultima_version': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'ultima_version'", 'to': u"orm['cachi.FichaTecnica']"})
        },
        u'cachi.informecampo': {
            'Meta': {'object_name': 'InformeCampo'},
            'adjuntos': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cachi.Adjunto']", 'null': 'True', 'blank': 'True'}),
            'autor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cachi.Persona']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sitio_aqueologico': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cachi.SitioArqueologico']", 'null': 'True', 'blank': 'True'})
        },
        u'cachi.modificacion': {
            'Meta': {'object_name': 'Modificacion'},
            'atributo': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'ficha_tecnica': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cachi.FichaTecnica']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pieza_conjunto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cachi.PiezaConjunto']", 'null': 'True', 'blank': 'True'}),
            'sitio_aqueologico': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cachi.SitioArqueologico']", 'null': 'True', 'blank': 'True'}),
            'valor_nuevo': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'valor_viejo': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'cachi.naturaleza': {
            'Meta': {'object_name': 'Naturaleza'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'cachi.persona': {
            'Meta': {'object_name': 'Persona'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'cachi.piezaconjunto': {
            'Meta': {'object_name': 'PiezaConjunto'},
            'condicion_hallazgo': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_hallazgo': ('django.db.models.fields.DateField', [], {}),
            'forma': ('django.db.models.fields.TextField', [], {'max_length': '128'}),
            'fragmentos': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naturaleza': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cachi.Naturaleza']"}),
            'nombre_descriptivo': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'persona_colectora': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cachi.Persona']", 'null': 'True', 'blank': 'True'}),
            'tecnica_manufactura': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'tipo_adquisicion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cachi.TipoAdquisicion']", 'null': 'True', 'blank': 'True'}),
            'tipo_condicion_hallazgo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cachi.TipoCondicionHallazgo']", 'null': 'True', 'blank': 'True'}),
            'ubicacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cachi.Ubicacion']", 'null': 'True', 'blank': 'True'})
        },
        u'cachi.procedencia': {
            'Meta': {'object_name': 'Procedencia'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otra': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'pieza_conjunto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cachi.PiezaConjunto']"}),
            'sitio_arqueologico': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cachi.SitioArqueologico']", 'null': 'True', 'blank': 'True'}),
            'ubicacion_geografica': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cachi.UbicacionGeografica']", 'null': 'True', 'blank': 'True'})
        },
        u'cachi.sitioarqueologico': {
            'Meta': {'object_name': 'SitioArqueologico'},
            'coordenada_x': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'coordenada_y': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'ubicacion_geografica': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cachi.UbicacionGeografica']"})
        },
        u'cachi.tipoadquisicion': {
            'Meta': {'object_name': 'TipoAdquisicion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'cachi.tipocondicionhallazgo': {
            'Meta': {'object_name': 'TipoCondicionHallazgo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'cachi.ubicacion': {
            'Meta': {'object_name': 'Ubicacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'cachi.ubicaciongeografica': {
            'Meta': {'object_name': 'UbicacionGeografica'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'padre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cachi.UbicacionGeografica']", 'null': 'True', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['cachi']