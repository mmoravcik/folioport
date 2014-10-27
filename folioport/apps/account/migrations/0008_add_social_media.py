# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        SocialMedia = orm['account.SocialMedia']
        facebook, created= SocialMedia.objects.get_or_create(code='FB')
        if not facebook.title:
            facebook.title = 'Facebook'
        facebook.script_code = """
            <div id="fb-root"></div>
            <script>(function(d, s, id) {
              var js, fjs = d.getElementsByTagName(s)[0];
              if (d.getElementById(id)) return;
              js = d.createElement(s); js.id = id;
              js.src = "//connect.facebook.net/en_GB/sdk.js#xfbml=1&version=v2.0";
              fjs.parentNode.insertBefore(js, fjs);
            }(document, 'script', 'facebook-jssdk'));</script>
            """
        facebook.html_code = '<div class="fb-like" data-layout="button" data-action="like" data-show-faces="false" data-share="false"></div>'
        facebook.save()

        twitter, created= SocialMedia.objects.get_or_create(code='TW')
        if not twitter.title:
            twitter.title = 'Twitter'
        twitter.script_code = "<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script>"

        twitter.html_code = '<a href="https://twitter.com/share" class="twitter-share-button" data-count="none">Tweet</a>'
        twitter.save()

        pinterest, created= SocialMedia.objects.get_or_create(code='PI')
        if not pinterest.title:
            pinterest.title = 'Pinterest'
        pinterest.script_code = '<script type="text/javascript" async  data-pin-color="red" data-pin-hover="true" src="//assets.pinterest.com/js/pinit.js"></script>'

        pinterest.html_code = ''
        pinterest.save()

    def backwards(self, orm):
        "Write your backwards methods here."

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
            'social_media': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['account.SocialMedia']", 'symmetrical': 'False', 'blank': 'True'}),
            'subdomain': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'use_social_media': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'use_system_blog': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'account.socialmedia': {
            'Meta': {'object_name': 'SocialMedia'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            'html_code': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'script_code': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['account']
    symmetrical = True
