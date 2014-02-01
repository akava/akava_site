# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Proxy.body'
        db.delete_column(u'request_proxy_proxy', 'body')

        # Deleting field 'Proxy.method'
        db.delete_column(u'request_proxy_proxy', 'method')


    def backwards(self, orm):
        # Adding field 'Proxy.body'
        db.add_column(u'request_proxy_proxy', 'body',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Proxy.method'
        db.add_column(u'request_proxy_proxy', 'method',
                      self.gf('django.db.models.fields.CharField')(default='GET', max_length=10),
                      keep_default=False)


    models = {
        u'request_proxy.proxy': {
            'Meta': {'object_name': 'Proxy'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['request_proxy']