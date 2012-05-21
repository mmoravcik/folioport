from folioport.project.models import *
from django.contrib import admin

class ProjectImageInline(admin.TabularInline):
    model = Image
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = (ProjectImageInline, )
    
admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)
admin.site.register(Image)