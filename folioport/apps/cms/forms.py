from ckeditor.widgets import CKEditorWidget
from django import forms
from django.db.models import get_model


class ItemImageForm(forms.ModelForm):

    class Meta:
        model = get_model('cms', 'ItemImage')


class ItemRichText(forms.ModelForm):
    text = forms.CharField(
        widget=CKEditorWidget()
    )
    class Meta:
        model = get_model('cms', 'ItemRichText')
        fields = ('text',)