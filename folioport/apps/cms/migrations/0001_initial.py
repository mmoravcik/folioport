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
            ('item_class', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('template', self.gf('django.db.models.fields.CharField')(default='', max_length=256, blank=True)),
            ('item_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
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

        # Adding model 'Image'
        db.create_table(u'cms_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('caption', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('thumbnail_type', self.gf('django.db.models.fields.CharField')(default='JPEG', max_length=4)),
            ('width', self.gf('django.db.models.fields.IntegerField')(default=300)),
            ('height', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'cms', ['Image'])

        # Adding model 'ItemImage'
        db.create_table(u'cms_itemimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('caption', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('thumbnail_type', self.gf('django.db.models.fields.CharField')(default='JPEG', max_length=4)),
            ('width', self.gf('django.db.models.fields.IntegerField')(default=300)),
            ('height', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'cms', ['ItemImage'])

        # Adding model 'ItemRandomImage'
        db.create_table(u'cms_itemrandomimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'cms', ['ItemRandomImage'])

        # Adding M2M table for field image on 'ItemRandomImage'
        db.create_table(u'cms_itemrandomimage_image', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('itemrandomimage', models.ForeignKey(orm[u'cms.itemrandomimage'], null=False)),
            ('image', models.ForeignKey(orm[u'cms.image'], null=False))
        ))
        db.create_unique(u'cms_itemrandomimage_image', ['itemrandomimage_id', 'image_id'])


    def backwards(self, orm):
        # Deleting model 'Container'
        db.delete_table(u'cms_container')

        # Deleting model 'Item'
        db.delete_table(u'cms_item')

        # Deleting model 'ContainerItems'
        db.delete_table(u'cms_containeritems')

        # Deleting model 'ItemText'
        db.delete_table(u'cms_itemtext')

        # Deleting model 'Image'
        db.delete_table(u'cms_image')

        # Deleting model 'ItemImage'
        db.delete_table(u'cms_itemimage')

        # Deleting model 'ItemRandomImage'
        db.delete_table(u'cms_itemrandomimage')

        # Removing M2M table for field image on 'ItemRandomImage'
        db.delete_table('cms_itemrandomimage_image')


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
        u'cms.itemtext': {
            'Meta': {'object_name': 'ItemText'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"})
        }
    }

    complete_apps = ['cms']