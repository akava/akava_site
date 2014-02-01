# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Proxy.method'
        db.alter_column(u'request_proxy_proxy', 'method', self.gf('django.db.models.fields.CharField')(max_length=10))

    def backwards(self, orm):

        # Changing field 'Proxy.method'
        db.alter_column(u'request_proxy_proxy', 'method', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'request_proxy.proxy': {
            'Meta': {'object_name': 'Proxy'},
            'body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'default': "'GET'", 'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['request_proxy']