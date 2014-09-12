from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, MultiField, Div, HTML

from django.db.models import get_model
from django import forms

Project = get_model('project', 'Project')


class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        '''
        self.helper.layout = Layout(
                'title',
                'thumbnail',
                HTML('Display advanced options [+]'),
                Div(
                    'thumbnail_width',
                    'tags',
                    'active',
                    css_id='form_optional_fields'
                )
        )
        '''

    class Meta:
        model = Project
        fields = ('title', 'thumbnail', 'thumbnail_width', 'tags', 'active',)