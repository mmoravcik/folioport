from django.db.models import get_model
from django.contrib import admin


News = get_model('news', 'News')
admin.site.register(News)
