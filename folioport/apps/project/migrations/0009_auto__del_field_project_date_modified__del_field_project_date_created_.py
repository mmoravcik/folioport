# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Project.date_modified'
        db.delete_column(u'project_project', 'date_modified')

        # Deleting field 'Project.date_created'
        db.delete_column(u'project_project', 'date_created')


        # Changing field 'Project.thumbnail'
        db.alter_column(u'project_project', 'thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'Project.order'
        db.alter_column(u'project_project', 'order', self.gf('django.db.models.fields.IntegerField')(null=True))
        # Deleting field 'Embed.date_modified'
        db.delete_column(u'project_embed', 'date_modified')

        # Deleting field 'Embed.date_created'
        db.delete_column(u'project_embed', 'date_created')

        # Deleting field 'Image.date_modified'
        db.delete_column(u'project_image', 'date_modified')

        # Deleting field 'Image.date_created'
        db.delete_column(u'project_image', 'date_created')


    def backwards(self, orm):
        # Adding field 'Project.date_modified'
        db.add_column(u'project_project', 'date_modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=None, blank=True),
                      keep_default=False)

        # Adding field 'Project.date_created'
        db.add_column(u'project_project', 'date_created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=None, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Project.thumbnail'
        raise RuntimeError("Cannot reverse this migration. 'Project.thumbnail' and its values cannot be restored.")

        # Changing field 'Project.order'
        db.alter_column(u'project_project', 'order', self.gf('django.db.models.fields.IntegerField')())

        # User chose to not deal with backwards NULL issues for 'Embed.date_modified'
        raise RuntimeError("Cannot reverse this migration. 'Embed.date_modified' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Embed.date_created'
        raise RuntimeError("Cannot reverse this migration. 'Embed.date_created' and its values cannot be restored.")
        # Adding field 'Image.date_modified'
        db.add_column(u'project_image', 'date_modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=2011, blank=True),
                      keep_default=False)

        # Adding field 'Image.date_created'
        db.add_column(u'project_image', 'date_created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=2011, blank=True),
                      keep_default=False)


    models = {
        u'project.category': {
            'Meta': {'object_name': 'Category'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['project.Category']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'project.embed': {
            'Meta': {'object_name': 'Embed'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'embed_code': ('django.db.models.fields.TextField', [], {}),
            'height': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.Project']"}),
            'width': ('django.db.models.fields.IntegerField', [], {'default': '300'})
        },
        u'project.image': {
            'Meta': {'object_name': 'Image'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.Project']"}),
            'thumbnail_type': ('django.db.models.fields.CharField', [], {'default': "'JPEG'", 'max_length': '4'}),
            'width': ('django.db.models.fields.IntegerField', [], {'default': '300'})
        },
        u'project.project': {
            'Meta': {'ordering': "['order']", 'object_name': 'Project'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['project.Category']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rating_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'rating_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'release_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128'}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'thumbnail_height': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'thumbnail_type': ('django.db.models.fields.CharField', [], {'default': "'JPEG'", 'max_length': '4'}),
            'thumbnail_width': ('django.db.models.fields.IntegerField', [], {'default': '100'})
        }
    }

    complete_apps = ['project']