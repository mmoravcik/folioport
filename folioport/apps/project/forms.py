from crispy_forms.helper import FormHelper
from folioport.apps.tekextensions.widgets import MultipleSelectWithPopUp
from crispy_forms.layout import Layout, Fieldset, Field
from crispy_forms.bootstrap import AppendedText

from django.db.models import get_model
from django import forms

Project = get_model('project', 'Project')
Category = get_model('project', 'Category')


class ProjectForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(), widget=MultipleSelectWithPopUp(
            'Category', 'picker/add_new.html', 'project'), required=False)

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper['thumbnail_width'].wrap(AppendedText, "px")
        self.helper.layout = Layout(
            Field('title'),
            Fieldset(
                'Optional settings',
                'category',
                'tags',
                'thumbnail',
                'thumbnail_width',
                'slug',
                'active',
                css_class='optional-settings',
                title='Advanced settings'

            )
        )

    class Meta:
        model = Project
        fields = ('title', 'category', 'thumbnail', 'thumbnail_width',
                  'tags', 'slug', 'active',)
        widgets = {
            'tags': forms.TextInput(attrs={'placeholder': 'any, tag, you, like, ...'})
        }


class CategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

    class Meta:
        model = Category
        fields = ('name',)