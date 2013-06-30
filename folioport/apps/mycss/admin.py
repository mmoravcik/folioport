from django.db.models import get_model
from django.contrib import admin

MyCSS = get_model('mycss', 'MyCSS')


admin.site.register(MyCSS)