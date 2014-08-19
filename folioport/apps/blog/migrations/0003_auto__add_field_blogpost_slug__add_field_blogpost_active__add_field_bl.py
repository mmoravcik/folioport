# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BlogPost.slug'
        db.add_column(u'blog_blogpost', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='slug', max_length=128),
                      keep_default=False)

        # Adding field 'BlogPost.active'
        db.add_column(u'blog_blogpost', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'BlogPost.content'
        db.add_column(u'blog_blogpost', 'content',
                      self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True),
                      keep_default=False)

        # Adding field 'BlogPost.release_date'
        db.add_column(u'blog_blogpost', 'release_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'BlogPost.order'
        db.add_column(u'blog_blogpost', 'order',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BlogPost.slug'
        db.delete_column(u'blog_blogpost', 'slug')

        # Deleting field 'BlogPost.active'
        db.delete_column(u'blog_blogpost', 'active')

        # Deleting field 'BlogPost.content'
        db.delete_column(u'blog_blogpost', 'content')

        # Deleting field 'BlogPost.release_date'
        db.delete_column(u'blog_blogpost', 'release_date')

        # Deleting field 'BlogPost.order'
        db.delete_column(u'blog_blogpost', 'order')


    models = {
        u'blog.blogpost': {
            'Meta': {'object_name': 'BlogPost'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'container': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cms.Container']"}),
            'content': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'release_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'blog.post': {
            'Meta': {'ordering': "['order']", 'object_name': 'Post'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'release_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'cms.container': {
            'Meta': {'object_name': 'Container'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['blog']