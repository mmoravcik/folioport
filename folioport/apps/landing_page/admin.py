from django.db.models import get_model
from django.contrib import admin

Image = get_model('landing_page', 'Image')
Embed = get_model('landing_page', 'Embed')
LandingPage = get_model('landing_page', 'LandingPage')


class LandingPageImageInline(admin.TabularInline):
    model = Image
    extra = 1


class LandingPageEmbedInline(admin.TabularInline):
    model = Embed
    extra = 1


class LandingPageAdmin(admin.ModelAdmin):
    inlines = (LandingPageImageInline, LandingPageEmbedInline,)


admin.site.register(LandingPage, LandingPageAdmin)
admin.site.register(Image)
admin.site.register(Embed)