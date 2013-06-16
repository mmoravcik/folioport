# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Category'
        db.create_table('project_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['project.Category'])),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('project', ['Category'])

        # Adding model 'Project'
        db.create_table('project_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=128, db_index=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('summary', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('release_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('tags', self.gf('tagging.fields.TagField')()),
        ))
        db.send_create_signal('project', ['Project'])

        # Adding M2M table for field category on 'Project'
        db.create_table('project_project_category', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['project.project'], null=False)),
            ('category', models.ForeignKey(orm['project.category'], null=False))
        ))
        db.create_unique('project_project_category', ['project_id', 'category_id'])

        # Adding model 'Image'
        db.create_table('project_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.Project'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('is_main', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('caption', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('project', ['Image'])


    def backwards(self, orm):
        
        # Deleting model 'Category'
        db.delete_table('project_category')

        # Deleting model 'Project'
        db.delete_table('project_project')

        # Removing M2M table for field category on 'Project'
        db.delete_table('project_project_category')

        # Deleting model 'Image'
        db.delete_table('project_image')


    models = {
        'project.category': {
            'Meta': {'object_name': 'Category'},
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
            'is_main': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['project.Project']"})
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
            'release_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128', 'db_index': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'tags': ('tagging.fields.TagField', [], {})
        }
    }

    complete_apps = ['project']
