# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MyCSS'
        db.create_table(u'mycss_mycss', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('css', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal(u'mycss', ['MyCSS'])


    def backwards(self, orm):
        # Deleting model 'MyCSS'
        db.delete_table(u'mycss_mycss')


    models = {
        u'mycss.mycss': {
            'Meta': {'object_name': 'MyCSS'},
            'css': ('django.db.models.fields.TextField', [], {'default': "''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['mycss']