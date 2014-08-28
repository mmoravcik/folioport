from django.db.models import get_model
from django import forms

Page = get_model('page', 'Page')


class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ('title', 'type', 'active',)