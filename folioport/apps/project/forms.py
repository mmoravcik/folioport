from crispy_forms.helper import FormHelper
from folioport.apps.tekextensions.widgets import SelectWithPopUp

from django.db.models import get_model
from django import forms

Project = get_model('project', 'Project')
Category = get_model('project', 'Category')


class ProjectForm(forms.ModelForm):
    category = forms.ModelChoiceField(Category.objects, widget=SelectWithPopUp)

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

    class Meta:
        model = Project
        fields = ('title', 'thumbnail', 'thumbnail_width', 'category', 'tags', 'active',)