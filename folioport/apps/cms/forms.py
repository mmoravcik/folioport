from django import forms
from django.db.models import get_model

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from ckeditor.widgets import CKEditorWidget


class ItemImageForm(forms.ModelForm):
    class Meta:
        model = get_model('cms', 'ItemImage')
        fields = ('image', 'hover_image', 'caption', 'width', 'thumbnail_type')


class ImageForm(forms.ModelForm):
    class Meta:
        model = get_model('cms', 'Image')
        fields = ('image', 'caption', 'width', 'thumbnail_type')


class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = get_model('cms', 'GalleryImage')
        fields = ('image', 'hover_image', 'caption', 'width', 'thumbnail_type')


class ItemEmbedForm(forms.ModelForm):
    class Meta:
        model = get_model('cms', 'ItemEmbed')
        fields = ('embed_code', 'caption', 'width', 'type')


class ItemRichTextForm(forms.ModelForm):
    text = forms.CharField(
        widget=CKEditorWidget()
    )

    class Meta:
        model = get_model('cms', 'ItemRichText')
        fields = ('text',)