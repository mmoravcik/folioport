import json

from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.sites.models import get_current_site
from django.http import HttpResponse


class LoginRequiredMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class FilterSiteMixin(object):
    def get_queryset(self):
        qs = super(FilterSiteMixin, self).get_queryset()
        return qs.filter(site=get_current_site(self.request))


class FilterUserMixin(object):
    def get_queryset(self):
        qs = super(FilterUserMixin, self).get_queryset()
        return qs.filter(user=self.request.user.id)


class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return self.render_to_json_response(data)
        else:
            return response


class ObjectSaveMixin(View):
    def get_model(self, kwargs):
        return self.model if self.model else None

    def post(self, request, *args, **kwargs):
        item_order = request.POST.get('item_order', "")
        status = 'success'
        model = self.get_model(kwargs)
        if item_order:
            for idx, item in enumerate(item_order.split(',')):
                try:
                    obj = model.objects.get(
                        id=int(item), user=self.request.user)
                except ValueError:
                    status = 'fail'
                except model.DoesNotExist:
                    status = 'fail'
                else:
                    obj.order = idx + 5
                    obj.save()

        response_data = {'status': status, 'result': ''}
        return HttpResponse(
            json.dumps(response_data), content_type="application/json")