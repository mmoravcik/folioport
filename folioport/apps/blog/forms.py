from django.db.models import get_model
from django import forms

Post = get_model('blog', 'BlogPost')


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'active', 'release_date',)