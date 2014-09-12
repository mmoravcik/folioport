from crispy_forms.helper import FormHelper

from django.db.models import get_model
from django import forms

Project = get_model('project', 'Project')


class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

    class Meta:
        model = Project
        fields = ('title', 'thumbnail', 'thumbnail_width', 'tags', 'active',)