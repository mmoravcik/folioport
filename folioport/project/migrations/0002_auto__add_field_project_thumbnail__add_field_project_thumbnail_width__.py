# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Project.thumbnail'
        db.add_column('project_project', 'thumbnail', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100), keep_default=False)

        # Adding field 'Project.thumbnail_width'
        db.add_column('project_project', 'thumbnail_width', self.gf('django.db.models.fields.IntegerField')(default=200), keep_default=False)

        # Adding field 'Project.order'
        db.add_column('project_project', 'order', self.gf('django.db.models.fields.IntegerField')(default=1), keep_default=False)

        # Adding field 'Category.active'
        db.add_column('project_category', 'active', self.gf('django.db.models.fields.BooleanField')(default=True), keep_default=False)

        # Deleting field 'Image.is_main'
        db.delete_column('project_image', 'is_main')

        # Adding field 'Image.width'
        db.add_column('project_image', 'width', self.gf('django.db.models.fields.IntegerField')(default=300), keep_default=False)

        # Adding field 'Image.order'
        db.add_column('project_image', 'order', self.gf('django.db.models.fields.IntegerField')(default=1), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Project.thumbnail'
        db.delete_column('project_project', 'thumbnail')

        # Deleting field 'Project.thumbnail_width'
        db.delete_column('project_project', 'thumbnail_width')

        # Deleting field 'Project.order'
        db.delete_column('project_project', 'order')

        # Deleting field 'Category.active'
        db.delete_column('project_category', 'active')

        # Adding field 'Image.is_main'
        db.add_column('project_image', 'is_main', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Deleting field 'Image.width'
        db.delete_column('project_image', 'width')

        # Deleting field 'Image.order'
        db.delete_column('project_image', 'order')


    models = {
        'project.category': {
            'Meta': {'object_name': 'Category'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['project.Category']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'project.image': {
            'Meta': {'object_name': 'Image'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['project.Project']"}),
            'width': ('django.db.models.fields.IntegerField', [], {'default': '300'})
        },
        'project.project': {
            'Meta': {'object_name': 'Project'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['project.Category']", 'symmetrical': 'False'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'release_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128', 'db_index': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'tags': ('tagging.fields.TagField', [], {}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'thumbnail_width': ('django.db.models.fields.IntegerField', [], {'default': '200'})
        }
    }

    complete_apps = ['project']
