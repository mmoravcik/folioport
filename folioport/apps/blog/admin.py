from django.db.models import get_model
from django.contrib import admin

Post = get_model('blog', 'Post')


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('active', )


admin.site.register(Post, PostAdmin)
