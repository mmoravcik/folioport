from django.db.models import get_model
from django import forms

Project = get_model('project', 'Project')


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('name', 'thumbnail', 'active', 'order',)