from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field

from django.db.models import get_model
from django import forms

Post = get_model('blog', 'Post')


class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.fields['release_date'].widget.attrs['class'] = 'cms_date_field'
        self.helper.layout = Layout(
            Field('title'),
            Fieldset(
                'Optional settings',
                'release_date',
                'slug',
                'active',
                css_class='optional-settings',
                title='Advanced settings'
            )
        )

    class Meta:
        model = Post
        fields = ('title', 'slug', 'release_date', 'active',)