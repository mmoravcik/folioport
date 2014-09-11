from django.db.models import get_model
from django.contrib import admin

Category = get_model('project', 'Category')
Project = get_model('project', 'Project')


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('category', 'active', )


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
