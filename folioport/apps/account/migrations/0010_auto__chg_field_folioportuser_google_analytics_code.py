# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'FolioportUser.google_analytics_code'
        db.alter_column(u'account_folioportuser', 'google_analytics_code', self.gf('django.db.models.fields.CharField')(max_length=30))

    def backwards(self, orm):

        # Changing field 'FolioportUser.google_analytics_code'
        db.alter_column(u'account_folioportuser', 'google_analytics_code', self.gf('django.db.models.fields.CharField')(max_length=10))

    models = {
        u'account.folioportuser': {
            'Meta': {'object_name': 'FolioportUser'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75', 'blank': 'True'}),
            'google_analytics_code': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'logo_width': ('django.db.models.fields.IntegerField', [], {'default': '120', 'blank': 'True'}),
            'own_blog_link': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'site_catch_phrase': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'blank': 'True'}),
            'site_logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'site_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'blank': 'True'}),
            'social_media': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['account.SocialMedia']", 'symmetrical': 'False', 'blank': 'True'}),
            'subdomain': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'use_system_blog': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'account.socialmedia': {
            'Meta': {'object_name': 'SocialMedia'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            'html_code': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'script_code': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['account']