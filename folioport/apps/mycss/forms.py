from django import forms
from django.db.models import get_model

MyCSS = get_model('mycss', 'MyCSS')


class MyCSSForm(forms.ModelForm):
    class Meta:
        model = MyCSS