# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Image.width'
        db.delete_column(u'cms_image', 'width')

        # Deleting field 'Image.height'
        db.delete_column(u'cms_image', 'height')

        # Adding field 'Image.max_width'
        db.add_column(u'cms_image', 'max_width',
                      self.gf('django.db.models.fields.IntegerField')(default=1000),
                      keep_default=False)

        # Adding field 'Image.min_width'
        db.add_column(u'cms_image', 'min_width',
                      self.gf('django.db.models.fields.IntegerField')(default=150),
                      keep_default=False)


        # Changing field 'Image.caption'
        db.alter_column(u'cms_image', 'caption', self.gf('django.db.models.fields.CharField')(max_length=128))
        # Deleting field 'ItemImage.width'
        db.delete_column(u'cms_itemimage', 'width')

        # Deleting field 'ItemImage.height'
        db.delete_column(u'cms_itemimage', 'height')

        # Adding field 'ItemImage.max_width'
        db.add_column(u'cms_itemimage', 'max_width',
                      self.gf('django.db.models.fields.IntegerField')(default=1000),
                      keep_default=False)

        # Adding field 'ItemImage.min_width'
        db.add_column(u'cms_itemimage', 'min_width',
                      self.gf('django.db.models.fields.IntegerField')(default=150),
                      keep_default=False)


        # Changing field 'ItemImage.caption'
        db.alter_column(u'cms_itemimage', 'caption', self.gf('django.db.models.fields.CharField')(max_length=128))

        # Changing field 'ItemEmbed.caption'
        db.alter_column(u'cms_itemembed', 'caption', self.gf('django.db.models.fields.CharField')(max_length=128))
        # Deleting field 'GalleryImage.width'
        db.delete_column(u'cms_galleryimage', 'width')

        # Deleting field 'GalleryImage.height'
        db.delete_column(u'cms_galleryimage', 'height')

        # Adding field 'GalleryImage.max_width'
        db.add_column(u'cms_galleryimage', 'max_width',
                      self.gf('django.db.models.fields.IntegerField')(default=1000),
                      keep_default=False)

        # Adding field 'GalleryImage.min_width'
        db.add_column(u'cms_galleryimage', 'min_width',
                      self.gf('django.db.models.fields.IntegerField')(default=150),
                      keep_default=False)


        # Changing field 'GalleryImage.caption'
        db.alter_column(u'cms_galleryimage', 'caption', self.gf('django.db.models.fields.CharField')(max_length=128))

    def backwards(self, orm):
        # Adding field 'Image.width'
        db.add_column(u'cms_image', 'width',
                      self.gf('django.db.models.fields.IntegerField')(default=300),
                      keep_default=False)

        # Adding field 'Image.height'
        db.add_column(u'cms_image', 'height',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Image.max_width'
        db.delete_column(u'cms_image', 'max_width')

        # Deleting field 'Image.min_width'
        db.delete_column(u'cms_image', 'min_width')


        # Changing field 'Image.caption'
        db.alter_column(u'cms_image', 'caption', self.gf('django.db.models.fields.TextField')())
        # Adding field 'ItemImage.width'
        db.add_column(u'cms_itemimage', 'width',
                      self.gf('django.db.models.fields.IntegerField')(default=300),
                      keep_default=False)

        # Adding field 'ItemImage.height'
        db.add_column(u'cms_itemimage', 'height',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'ItemImage.max_width'
        db.delete_column(u'cms_itemimage', 'max_width')

        # Deleting field 'ItemImage.min_width'
        db.delete_column(u'cms_itemimage', 'min_width')


        # Changing field 'ItemImage.caption'
        db.alter_column(u'cms_itemimage', 'caption', self.gf('django.db.models.fields.TextField')())

        # Changing field 'ItemEmbed.caption'
        db.alter_column(u'cms_itemembed', 'caption', self.gf('django.db.models.fields.TextField')())
        # Adding field 'GalleryImage.width'
        db.add_column(u'cms_galleryimage', 'width',
                      self.gf('django.db.models.fields.IntegerField')(default=300),
                      keep_default=False)

        # Adding field 'GalleryImage.height'
        db.add_column(u'cms_galleryimage', 'height',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'GalleryImage.max_width'
        db.delete_column(u'cms_galleryimage', 'max_width')

        # Deleting field 'GalleryImage.min_width'
        db.delete_column(u'cms_galleryimage', 'min_width')


        # Changing field 'GalleryImage.caption'
        db.alter_column(u'cms_galleryimage', 'caption', self.gf('django.db.models.fields.TextField')())

    models = {
        u'account.folioportuser': {
            'Meta': {'object_name': 'FolioportUser'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75', 'blank': 'True'}),
            'google_analytics_code': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10', 'blank': 'True'}),
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
            'subdomain': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'use_social_media': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'use_system_blog': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'cms.container': {
            'Meta': {'object_name': 'Container'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.FolioportUser']"})
        },
        u'cms.containeritems': {
            'Meta': {'object_name': 'ContainerItems'},
            'container': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cms.Container']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cms.Item']"}),
            'position': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        u'cms.galleryimage': {
            'Meta': {'object_name': 'GalleryImage'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'hover_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'max_width': ('django.db.models.fields.IntegerField', [], {'default': '1000'}),
            'min_width': ('django.db.models.fields.IntegerField', [], {'default': '150'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'thumbnail_type': ('django.db.models.fields.CharField', [], {'default': "'JPEG'", 'max_length': '4'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.FolioportUser']"})
        },
        u'cms.image': {
            'Meta': {'object_name': 'Image'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'max_width': ('django.db.models.fields.IntegerField', [], {'default': '1000'}),
            'min_width': ('django.db.models.fields.IntegerField', [], {'default': '150'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'thumbnail_type': ('django.db.models.fields.CharField', [], {'default': "'JPEG'", 'max_length': '4'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.FolioportUser']"})
        },
        u'cms.item': {
            'Meta': {'object_name': 'Item'},
            'container': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cms.Container']", 'through': u"orm['cms.ContainerItems']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_class': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'item_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256', 'blank': 'True'})
        },
        u'cms.itemembed': {
            'Meta': {'object_name': 'ItemEmbed'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'embed_code': ('django.db.models.fields.TextField', [], {}),
            'height': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'type': ('django.db.models.fields.SmallIntegerField', [], {'default': '2'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.FolioportUser']"}),
            'width': ('django.db.models.fields.IntegerField', [], {'default': '300'})
        },
        u'cms.itemgallery': {
            'Meta': {'object_name': 'ItemGallery'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cms.GalleryImage']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.FolioportUser']"})
        },
        u'cms.itemheading': {
            'Meta': {'object_name': 'ItemHeading'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '2'}),
            'text': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.FolioportUser']"})
        },
        u'cms.itemimage': {
            'Meta': {'object_name': 'ItemImage'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'hover_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'max_width': ('django.db.models.fields.IntegerField', [], {'default': '1000'}),
            'min_width': ('django.db.models.fields.IntegerField', [], {'default': '150'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'thumbnail_type': ('django.db.models.fields.CharField', [], {'default': "'JPEG'", 'max_length': '4'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.FolioportUser']"})
        },
        u'cms.itemrandomimage': {
            'Meta': {'object_name': 'ItemRandomImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cms.Image']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.FolioportUser']"})
        },
        u'cms.itemrichtext': {
            'Meta': {'object_name': 'ItemRichText'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.FolioportUser']"})
        },
        u'cms.itemtext': {
            'Meta': {'object_name': 'ItemText'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.FolioportUser']"})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['cms']