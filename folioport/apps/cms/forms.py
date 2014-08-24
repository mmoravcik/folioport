from django import forms
from django.db.models import get_model


class ItemImageForm(forms.ModelForm):

    class Meta:
        model = get_model('cms', 'ItemImage')
        fields = ('image', 'caption', 'width', 'thumbnail_type')