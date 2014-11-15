from django.db.models import get_model
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.utils.html import escape
from django.forms import ValidationError

from forms import get_model_form, normalize_model_name


def add_new_model(request, app, model_name, form=None):
    normal_model_name = normalize_model_name(model_name)
    model = get_model(app, normal_model_name)
    form = form if form else model.get_form_class()

    if not form:
        form = get_model_form(normal_model_name)

    if request.method == 'POST':
        form = form(request.POST, request.FILES)

        if form.is_valid():
            form.instance.user = request.user
            form.instance.site = request.user.site
            try:
                new_obj = form.save()
            except ValidationError as error:
                new_obj = None

            if new_obj:
                return HttpResponse(
                    '<script type="text/javascript">opener.dismissAddAnotherPopup(window, "%s", "%s");</script>' %
                    (escape(new_obj._get_pk_val()), escape(new_obj)))

    else:
        form = form()

    page_context = {'app': app, 'form': form, 'field': normal_model_name, 'is_popup': True}
    return render_to_response('picker/popup.html', page_context,
                              context_instance=RequestContext(request))