# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Project.thumbnail_type'
        db.add_column('project_project', 'thumbnail_type', self.gf('django.db.models.fields.CharField')(default='JPEG', max_length=4), keep_default=False)

        # Changing field 'Project.description'
        db.alter_column('project_project', 'description', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Project.summary'
        db.alter_column('project_project', 'summary', self.gf('django.db.models.fields.TextField')(null=True))

        # Adding field 'Image.thumbnail_type'
        db.add_column('project_image', 'thumbnail_type', self.gf('django.db.models.fields.CharField')(default='JPEG', max_length=4), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Project.thumbnail_type'
        db.delete_column('project_project', 'thumbnail_type')

        # Changing field 'Project.description'
        db.alter_column('project_project', 'description', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Project.summary'
        db.alter_column('project_project', 'summary', self.gf('django.db.models.fields.TextField')(default=''))

        # Deleting field 'Image.thumbnail_type'
        db.delete_column('project_image', 'thumbnail_type')


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
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128', 'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'project.embed': {
            'Meta': {'object_name': 'Embed'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'embed_code': ('django.db.models.fields.TextField', [], {}),
            'height': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['project.Project']"}),
            'width': ('django.db.models.fields.IntegerField', [], {'default': '300'})
        },
        'project.image': {
            'Meta': {'object_name': 'Image'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['project.Project']"}),
            'thumbnail_type': ('django.db.models.fields.CharField', [], {'default': "'JPEG'", 'max_length': '4'}),
            'width': ('django.db.models.fields.IntegerField', [], {'default': '300'})
        },
        'project.project': {
            'Meta': {'object_name': 'Project'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['project.Category']", 'symmetrical': 'False'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'rating_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'rating_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'release_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128', 'db_index': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'thumbnail_height': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'thumbnail_type': ('django.db.models.fields.CharField', [], {'default': "'JPEG'", 'max_length': '4'}),
            'thumbnail_width': ('django.db.models.fields.IntegerField', [], {'default': '100'})
        }
    }

    complete_apps = ['project']
