# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Embed'
        db.delete_table(u'project_embed')

        # Deleting model 'HoverOnImage'
        db.delete_table(u'project_hoveronimage')

        # Deleting model 'Image'
        db.delete_table(u'project_image')

        # Deleting field 'Project.description'
        db.delete_column(u'project_project', 'description')

        # Deleting field 'Project.summary'
        db.delete_column(u'project_project', 'summary')

        # Adding field 'Project.container'
        db.add_column(u'project_project', 'container',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Container'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Embed'
        db.create_table(u'project_embed', (
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.Project'])),
            ('caption', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('width', self.gf('django.db.models.fields.IntegerField')(default=300)),
            ('embed_code', self.gf('django.db.models.fields.TextField')()),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('type', self.gf('django.db.models.fields.SmallIntegerField')(default=2)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'project', ['Embed'])

        # Adding model 'HoverOnImage'
        db.create_table(u'project_hoveronimage', (
            ('caption', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('thumbnail_type', self.gf('django.db.models.fields.CharField')(default='JPEG', max_length=4)),
            ('width', self.gf('django.db.models.fields.IntegerField')(default=300)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=1)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'project', ['HoverOnImage'])

        # Adding model 'Image'
        db.create_table(u'project_image', (
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.Project'])),
            ('caption', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('thumbnail_type', self.gf('django.db.models.fields.CharField')(default='JPEG', max_length=4)),
            ('width', self.gf('django.db.models.fields.IntegerField')(default=300)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=1)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hover_on', self.gf('django.db.models.fields.related.ForeignKey')(related_name='hover_on_image', null=True, to=orm['project.HoverOnImage'], blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'project', ['Image'])

        # Adding field 'Project.description'
        db.add_column(u'project_project', 'description',
                      self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True),
                      keep_default=False)

        # Adding field 'Project.summary'
        db.add_column(u'project_project', 'summary',
                      self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Project.container'
        db.delete_column(u'project_project', 'container_id')


    models = {
        u'cms.container': {
            'Meta': {'object_name': 'Container'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'project.category': {
            'Meta': {'object_name': 'Category'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['project.Category']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'project.project': {
            'Meta': {'ordering': "['order']", 'object_name': 'Project'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['project.Category']", 'symmetrical': 'False'}),
            'container': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cms.Container']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rating_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'rating_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'release_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'thumbnail_height': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'thumbnail_type': ('django.db.models.fields.CharField', [], {'default': "'JPEG'", 'max_length': '4'}),
            'thumbnail_width': ('django.db.models.fields.IntegerField', [], {'default': '100'})
        }
    }

    complete_apps = ['project']