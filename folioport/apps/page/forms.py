from crispy_forms.helper import FormHelper

from django.db.models import get_model
from django import forms

Page = get_model('page', 'Page')


class PageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

    class Meta:
        model = Page
        fields = ('title', 'type', 'active',)