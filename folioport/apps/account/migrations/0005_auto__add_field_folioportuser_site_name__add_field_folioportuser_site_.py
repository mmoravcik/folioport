# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'FolioportUser.site_name'
        db.add_column(u'account_folioportuser', 'site_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=128, blank=True),
                      keep_default=False)

        # Adding field 'FolioportUser.site_catch_phrase'
        db.add_column(u'account_folioportuser', 'site_catch_phrase',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=128, blank=True),
                      keep_default=False)

        # Adding field 'FolioportUser.use_social_media'
        db.add_column(u'account_folioportuser', 'use_social_media',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'FolioportUser.use_system_blog'
        db.add_column(u'account_folioportuser', 'use_system_blog',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'FolioportUser.own_blog_link'
        db.add_column(u'account_folioportuser', 'own_blog_link',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'FolioportUser.site_logo'
        db.add_column(u'account_folioportuser', 'site_logo',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'FolioportUser.logo_width'
        db.add_column(u'account_folioportuser', 'logo_width',
                      self.gf('django.db.models.fields.IntegerField')(default=120, blank=True),
                      keep_default=False)


        # Changing field 'FolioportUser.site'
        db.alter_column(u'account_folioportuser', 'site_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['sites.Site']))

    def backwards(self, orm):
        # Deleting field 'FolioportUser.site_name'
        db.delete_column(u'account_folioportuser', 'site_name')

        # Deleting field 'FolioportUser.site_catch_phrase'
        db.delete_column(u'account_folioportuser', 'site_catch_phrase')

        # Deleting field 'FolioportUser.use_social_media'
        db.delete_column(u'account_folioportuser', 'use_social_media')

        # Deleting field 'FolioportUser.use_system_blog'
        db.delete_column(u'account_folioportuser', 'use_system_blog')

        # Deleting field 'FolioportUser.own_blog_link'
        db.delete_column(u'account_folioportuser', 'own_blog_link')

        # Deleting field 'FolioportUser.site_logo'
        db.delete_column(u'account_folioportuser', 'site_logo')

        # Deleting field 'FolioportUser.logo_width'
        db.delete_column(u'account_folioportuser', 'logo_width')


        # Changing field 'FolioportUser.site'
        db.alter_column(u'account_folioportuser', 'site_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'], null=True))

    models = {
        u'account.folioportuser': {
            'Meta': {'object_name': 'FolioportUser'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'logo_width': ('django.db.models.fields.IntegerField', [], {'default': '120', 'blank': 'True'}),
            'own_blog_link': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'site_catch_phrase': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'blank': 'True'}),
            'site_logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'site_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'blank': 'True'}),
            'subdomain': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'use_social_media': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'use_system_blog': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['account']