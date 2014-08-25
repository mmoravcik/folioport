from django.db.models import get_model
from django import forms

Post = get_model('blog', 'Post')


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'active',)