from django.db.models import get_model
from django.contrib import admin

SocialMedia = get_model('account', 'SocialMedia')


admin.site.register(SocialMedia)