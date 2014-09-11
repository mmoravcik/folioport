import json

from crispy_forms.helper import FormHelper

from django.forms.models import ModelMultipleChoiceField
from django.views.generic import RedirectView
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.views.generic.list import ListView, View
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib import messages

from folioport.base.mixins import LoginRequiredMixin, FilterUserMixin

Post = models.get_model('blog', 'Post')
Container = models.get_model('cms', 'Container')
ContainerItems = models.get_model('cms', 'ContainerItems')
Item = models.get_model('cms', 'Item')


class ContainerListView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/cms/container_list.html'
    model = Container


class ContainerEditView(LoginRequiredMixin, UpdateView):
    model = Container
    template_name = 'dashboard/cms/edit.html'

    def get_success_url(self):
        return reverse_lazy('folioport:dashboard:cms:container-list')

    def form_valid(self, form):
        messages.info(self.request, 'Post has been saved!')
        return super(ContainerEditView, self).form_valid(form)


class CMSViewMixin(LoginRequiredMixin):
    def get_template_names(self):
        if self.model.get_edit_create_template():
            return [self.model.get_edit_create_template()]
        return [self.template_name]

    def get_context_data(self, **kwargs):
        ctx = super(CMSViewMixin, self).get_context_data(**kwargs)
        ctx['next_url'] = self.get_success_url()
        return ctx

    def get_success_url(self):
        if self.request.GET.get('next'):
            return self.request.GET.get('next')
        return reverse_lazy('folioport:dashboard:home')


class ItemEditView(CMSViewMixin, UpdateView):
    template_name = 'dashboard/cms/item_edit.html'

    def get_form(self, form_class):
        form = super(ItemEditView, self).get_form(form_class)
        # remove form tag for all crispy-form forms
        if not getattr(form, 'helper', None):
            form.helper = FormHelper()
            form.helper.form_tag = False
        # images are foreign keys and we need to limit them to current user
        if isinstance(form.fields.get('image', None), ModelMultipleChoiceField):
            form.fields['image'].queryset = form.fields['image'].queryset.\
                filter(user=self.request.user)
        return form

    def get_queryset(self):
        self.model = models.get_model('cms', self.kwargs['class_name'])
        return self.model.objects.filter(
            user=self.request.user, id=self.kwargs['pk'])

    def get_form_class(self):
        if self.model.get_form_class():
            return self.model.get_form_class()
        return super(ItemEditView, self).get_form_class()

    def form_valid(self, form):
        messages.info(self.request, 'Item has been saved!')
        return super(ItemEditView, self).form_valid(form)


class ItemCreateRedirectView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return "%s?next=%s" % (reverse_lazy('folioport:dashboard:cms:item-create',
            kwargs={'class_name': self.request.GET['class_name'],
                    'container_id': self.request.GET.get('container_id', 0)}),
        self.request.GET.get('next', ''))


class ItemCreateView(CMSViewMixin, CreateView):
    template_name = 'dashboard/cms/item_create.html'

    def get_form(self, form_class):
        form = super(ItemCreateView, self).get_form(form_class)
        # remove form tag for all crispy-form forms
        if not getattr(form, 'helper', None):
            form.helper = FormHelper()
            form.helper.form_tag = False
        # images are foreign keys and we need to limit them to current user
        if isinstance(form.fields.get('image', None), ModelMultipleChoiceField):
            form.fields['image'].queryset = form.fields['image'].queryset.\
                filter(user=self.request.user)
        return form

    def get_form_class(self):
        if self.model.get_form_class():
            return self.model.get_form_class()
        return super(ItemCreateView, self).get_form_class()

    def dispatch(self, *args, **kwargs):
        self.model = models.get_model('cms', self.kwargs['class_name'])
        return super(ItemCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.assign_to_user(self.request.user)
        response = super(ItemCreateView, self).form_valid(form)
        self.object.assign_to_container(self.kwargs['container_id'])
        messages.info(self.request, 'Item has been created!')
        return response


class ItemDeleteView(CMSViewMixin, DeleteView):
    template_name = 'dashboard/cms/item_delete.html'

    def get_queryset(self):
        self.model = models.get_model('cms', self.kwargs['class_name'])
        return self.model.objects.filter(
            user=self.request.user, id=self.kwargs['pk'])


class ItemsOrderSave(View):
    def post(self, request, *args, **kwargs):
        item_order = request.POST.get('item_order', "")
        status = 'success'
        if item_order:
            for idx, item in enumerate(item_order.split(',')):
                try:
                    container_item = ContainerItems.objects.get(
                        id=int(item), container__user=self.request.user)
                except ValueError:
                    status = 'fail'
                except ContainerItems.DoesNotExist:
                    status = 'fail'
                else:
                    container_item.position = idx + 5
                    container_item.save()

        response_data = {'status': status, 'result': ''}
        return HttpResponse(
            json.dumps(response_data), content_type="application/json")


class ContainerPreviewView(View):
    def get(self, request, *args, **kwargs):
        status = 'fail'
        result = ''
        try:
            container = Container.objects.get(
                id=kwargs['container_id'], user=self.request.user)
        except ValueError:
            pass
        except Container.DoesNotExist:
            pass
        else:
            status = 'success'
            result = container.render()

        response_data = {'status': status, 'result': result}
        return HttpResponse(
            json.dumps(response_data), content_type="application/json")