from django import forms
from django.template.loader import render_to_string
from django.contrib.admin.widgets import FilteredSelectMultiple


class PopUpBaseWidget(object):
    def __init__(self, model=None, template='picker/add_new.html', app='None', *args, **kwargs):
        self.model = model
        self.template = template
        self.app = app
        super(PopUpBaseWidget, self).__init__(*args, **kwargs)

    def render(self, name, *args, **kwargs):
        html = super(PopUpBaseWidget, self).render(name, *args, **kwargs)

        if not self.model:
            self.model = name

        popupplus = render_to_string(
            self.template, {'app': self.app, 'field': name, 'model': self.model})
        return html+popupplus

    def _media(self):
        js = ["admin/js/core.js", "admin/js/admin/RelatedObjectLookups.js"]

        return forms.widgets.Media(
            js=js
        )
    media = property(_media)


class FilteredMultipleSelectWithPopUp(PopUpBaseWidget, FilteredSelectMultiple):
    pass


class MultipleSelectWithPopUp(PopUpBaseWidget, forms.SelectMultiple):
    pass


class SelectWithPopUp(PopUpBaseWidget, forms.Select):
    pass
