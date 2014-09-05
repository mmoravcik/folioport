from django.db.models import get_model
from django import forms

MyCSS = get_model('my_css', 'MyCSS')


class MyCssForm(forms.ModelForm):

    class Meta:
        model = MyCSS
        fields = ('css',)