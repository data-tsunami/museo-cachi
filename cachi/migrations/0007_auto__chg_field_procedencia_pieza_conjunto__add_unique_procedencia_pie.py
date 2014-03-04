# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Procedencia.pieza_conjunto'
        db.alter_column(u'cachi_procedencia', 'pieza_conjunto_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['cachi.PiezaConjunto']))
        # Adding unique constraint on 'Procedencia', fields ['pieza_conjunto']
        db.create_unique(u'cachi_procedencia', ['pieza_conjunto_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Procedencia', fields ['pieza_conjunto']
        db.delete_unique(u'cachi_procedencia', ['pieza_conjunto_id'])


        # Changing field 'Procedencia.pieza_conjunto'
        db.alter_column(u'cachi_procedencia', 'pieza_conjunto_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cachi.PiezaConjunto']))

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
            'ficha_tecnica': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'adjunto_ficha_tecnica'", 'null': 'True', 'to': u"orm['cachi.FichaTecnica']"}),
            'fragmento': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'adjunto_fragmento'", 'null': 'True', 'to': u"orm['cachi.Fragmento']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informe_campo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cachi.InformeCampo']", 'null': 'True', 'blank': 'True'}),
            'nombre_archivo': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'pieza_conjunto': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'adjunto_pieza_conjunto'", 'null': 'True', 'to': u"orm['cachi.PiezaConjunto']"}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '64'})
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
            'diagnostico_estado': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'diametro_max': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'diametro_min': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'espesor': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'fragmento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'fichas_tecnicas'", 'to': u"orm['cachi.Fragmento']"}),
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
            'pieza_conjunto': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'fragmentos_pieza_conjunto'", 'to': u"orm['cachi.PiezaConjunto']"}),
            'ultima_version': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ultima_version'", 'null': 'True', 'to': u"orm['cachi.FichaTecnica']"})
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
            'otra': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'pieza_conjunto': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'procedencia'", 'unique': 'True', 'to': u"orm['cachi.PiezaConjunto']"}),
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