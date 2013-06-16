# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'News.date_modified'
        db.delete_column(u'news_news', 'date_modified')

        # Deleting field 'News.date_created'
        db.delete_column(u'news_news', 'date_created')


    def backwards(self, orm):
        # Adding field 'News.date_modified'
        db.add_column(u'news_news', 'date_modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=2011, blank=True),
                      keep_default=False)

        # Adding field 'News.date_created'
        db.add_column(u'news_news', 'date_created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=2011, blank=True),
                      keep_default=False)


    models = {
        u'news.news': {
            'Meta': {'ordering': "['-release_date']", 'object_name': 'News'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'release_date': ('django.db.models.fields.DateTimeField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '128'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['news']