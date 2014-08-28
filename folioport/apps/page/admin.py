from django.db.models import get_model
from django.contrib import admin

Page = get_model('page', 'Page')


admin.site.register(Page)