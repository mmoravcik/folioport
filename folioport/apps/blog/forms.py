from ckeditor.widgets import CKEditorWidget

from django.db.models import get_model
from django import forms

Post = get_model('blog', 'Post')


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=CKEditorWidget()
    )

    class Meta:
        model = Post
        fields = ('title', 'content', 'thumbnail', 'tags', 'active',)