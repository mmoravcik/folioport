from django.db.models import get_model
from django.contrib import admin

Image = get_model('project', 'Image')
HoverOnImage = get_model('project', 'HoverOnImage')
Embed = get_model('project', 'Embed')
Category = get_model('project', 'Category')
Project = get_model('project', 'Project')


class ProjectImageInline(admin.TabularInline):
    model = Image
    extra = 1


class ProjectEmbedInline(admin.TabularInline):
    model = Embed
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = (ProjectImageInline, ProjectEmbedInline,)
    list_filter = ('category', 'active', )


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Image)
admin.site.register(Embed)
admin.site.register(HoverOnImage)