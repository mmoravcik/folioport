from django.db.models import get_model
from django.contrib import admin

Post = get_model('blog', 'Post')


admin.site.register(Post)