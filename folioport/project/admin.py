from folioport.project.models import *
from django.contrib import admin

class ProjectImageInline(admin.TabularInline):
    model = Image
    extra = 1

#class ProjectEmbedInline(admin.TabularInline):
#    model = Embed
#    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    #ProjectEmbedInline,
    inlines = (ProjectImageInline,  )
    list_filter = ('category', 'active', )
    
admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)
admin.site.register(Image)
#admin.site.register(Embed)