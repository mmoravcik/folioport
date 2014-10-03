from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field

from django.db.models import get_model
from django import forms

Page = get_model('page', 'Page')


class PageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('title'),
            Fieldset(
                'Advanced settings',
                'type',
                'slug',
                'active',
                css_class='optional-settings',
                title='Advanced settings'
            )
        )

    class Meta:
        model = Page
        fields = ('title', 'type', 'slug', 'active',)