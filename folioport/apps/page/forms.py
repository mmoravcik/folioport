from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field

from django.core.exceptions import ValidationError
from django.db.models import get_model
from django import forms

Page = get_model('page', 'Page')


class PageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
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

    def clean_type(self):
        Page = get_model('page', 'Page')
        if self.cleaned_data['type'] == Page.LANDING_PAGE:
            qs = Page.objects.filter(user=self.user, type=Page.LANDING_PAGE)
            if self.instance.id:
                qs = qs.exclude(id=self.instance.id)
            if qs:
                raise ValidationError('You can have only one '
                                      'landing page at any time')
        return self.cleaned_data['type']