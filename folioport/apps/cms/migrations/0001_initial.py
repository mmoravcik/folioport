# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Container'
        db.create_table(u'cms_container', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'cms', ['Container'])

        # Adding model 'Item'
        db.create_table(u'cms_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item_class', self.gf('django.db.models.fields.TextField')(max_length=128)),
            ('template', self.gf('django.db.models.fields.TextField')(default='', max_length=256)),
            ('item_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'cms', ['Item'])

        # Adding model 'ContainerItems'
        db.create_table(u'cms_containeritems', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('container', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Container'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Item'])),
            ('position', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal(u'cms', ['ContainerItems'])

        # Adding model 'ItemText'
        db.create_table(u'cms_itemtext', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal(u'cms', ['ItemText'])


    def backwards(self, orm):
        # Deleting model 'Container'
        db.delete_table(u'cms_container')

        # Deleting model 'Item'
        db.delete_table(u'cms_item')

        # Deleting model 'ContainerItems'
        db.delete_table(u'cms_containeritems')

        # Deleting model 'ItemText'
        db.delete_table(u'cms_itemtext')


    models = {
        u'cms.container': {
            'Meta': {'object_name': 'Container'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'cms.containeritems': {
            'Meta': {'object_name': 'ContainerItems'},
            'container': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cms.Container']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cms.Item']"}),
            'position': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        u'cms.item': {
            'Meta': {'object_name': 'Item'},
            'container': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cms.Container']", 'through': u"orm['cms.ContainerItems']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_class': ('django.db.models.fields.TextField', [], {'max_length': '128'}),
            'item_id': ('django.db.models.fields.IntegerField', [], {}),
            'template': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '256'})
        },
        u'cms.itemtext': {
            'Meta': {'object_name': 'ItemText'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"})
        }
    }

    complete_apps = ['cms']