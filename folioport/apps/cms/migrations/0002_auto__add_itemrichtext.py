# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ItemRichText'
        db.create_table(u'cms_itemrichtext', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal(u'cms', ['ItemRichText'])


    def backwards(self, orm):
        # Deleting model 'ItemRichText'
        db.delete_table(u'cms_itemrichtext')


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
        u'cms.image': {
            'Meta': {'object_name': 'Image'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'thumbnail_type': ('django.db.models.fields.CharField', [], {'default': "'JPEG'", 'max_length': '4'}),
            'width': ('django.db.models.fields.IntegerField', [], {'default': '300'})
        },
        u'cms.item': {
            'Meta': {'object_name': 'Item'},
            'container': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cms.Container']", 'through': u"orm['cms.ContainerItems']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_class': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'item_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256', 'blank': 'True'})
        },
        u'cms.itemimage': {
            'Meta': {'object_name': 'ItemImage'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'thumbnail_type': ('django.db.models.fields.CharField', [], {'default': "'JPEG'", 'max_length': '4'}),
            'width': ('django.db.models.fields.IntegerField', [], {'default': '300'})
        },
        u'cms.itemrandomimage': {
            'Meta': {'object_name': 'ItemRandomImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cms.Image']", 'symmetrical': 'False'})
        },
        u'cms.itemrichtext': {
            'Meta': {'object_name': 'ItemRichText'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"})
        },
        u'cms.itemtext': {
            'Meta': {'object_name': 'ItemText'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"})
        }
    }

    complete_apps = ['cms']