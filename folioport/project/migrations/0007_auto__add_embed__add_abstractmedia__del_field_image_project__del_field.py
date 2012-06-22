# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Embed'
        db.create_table('project_embed', (
            ('abstractmedia_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['project.AbstractMedia'], unique=True, primary_key=True)),
            ('embed_code', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('project', ['Embed'])

        # Adding model 'AbstractMedia'
        db.create_table('project_abstractmedia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.Project'])),
            ('caption', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('width', self.gf('django.db.models.fields.IntegerField')(default=300)),
            ('height', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal('project', ['AbstractMedia'])

        # Deleting field 'Image.project'
        db.delete_column('project_image', 'project_id')

        # Deleting field 'Image.caption'
        db.delete_column('project_image', 'caption')

        # Deleting field 'Image.width'
        db.delete_column('project_image', 'width')

        # Deleting field 'Image.date_modified'
        db.delete_column('project_image', 'date_modified')

        # Deleting field 'Image.date_created'
        db.delete_column('project_image', 'date_created')

        # Deleting field 'Image.order'
        db.delete_column('project_image', 'order')

        # Deleting field 'Image.id'
        db.delete_column('project_image', 'id')

        # Deleting field 'Image.height'
        db.delete_column('project_image', 'height')

        # Adding field 'Image.abstractmedia_ptr'
        db.add_column('project_image', 'abstractmedia_ptr', self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['project.AbstractMedia'], unique=True, primary_key=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Embed'
        db.delete_table('project_embed')

        # Deleting model 'AbstractMedia'
        db.delete_table('project_abstractmedia')

        # Adding field 'Image.project'
        db.add_column('project_image', 'project', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['project.Project']), keep_default=False)

        # Adding field 'Image.caption'
        db.add_column('project_image', 'caption', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'Image.width'
        db.add_column('project_image', 'width', self.gf('django.db.models.fields.IntegerField')(default=300), keep_default=False)

        # Adding field 'Image.date_modified'
        db.add_column('project_image', 'date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=1, blank=True), keep_default=False)

        # Adding field 'Image.date_created'
        db.add_column('project_image', 'date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=1, blank=True), keep_default=False)

        # Adding field 'Image.order'
        db.add_column('project_image', 'order', self.gf('django.db.models.fields.IntegerField')(default=1), keep_default=False)

        # Adding field 'Image.id'
        db.add_column('project_image', 'id', self.gf('django.db.models.fields.AutoField')(default=1, primary_key=True), keep_default=False)

        # Adding field 'Image.height'
        db.add_column('project_image', 'height', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Deleting field 'Image.abstractmedia_ptr'
        db.delete_column('project_image', 'abstractmedia_ptr_id')


    models = {
        'project.abstractmedia': {
            'Meta': {'object_name': 'AbstractMedia'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['project.Project']"}),
            'width': ('django.db.models.fields.IntegerField', [], {'default': '300'})
        },
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
            'abstractmedia_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['project.AbstractMedia']", 'unique': 'True', 'primary_key': 'True'}),
            'embed_code': ('django.db.models.fields.TextField', [], {})
        },
        'project.image': {
            'Meta': {'object_name': 'Image'},
            'abstractmedia_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['project.AbstractMedia']", 'unique': 'True', 'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
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
            'order': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'rating_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'rating_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'release_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128', 'db_index': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'tags': ('tagging.fields.TagField', [], {}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'thumbnail_height': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'thumbnail_width': ('django.db.models.fields.IntegerField', [], {'default': '100'})
        }
    }

    complete_apps = ['project']
