# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Deudor'
        db.create_table(u'deudores_deudor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('apepat', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('apemat', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('fecha_nacimiento', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('institucion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('fecha_ingreso', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('CURP', self.gf('django.db.models.fields.CharField')(max_length=18, unique=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'deudores', ['Deudor'])


    def backwards(self, orm):
        # Deleting model 'Deudor'
        db.delete_table(u'deudores_deudor')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'deudores.deudor': {
            'CURP': ('django.db.models.fields.CharField', [], {'max_length': '18', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Deudor'},
            'apemat': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'apepat': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'fecha_ingreso': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        }
    }

    complete_apps = ['deudores']