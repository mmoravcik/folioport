from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.views.generic import RedirectView
from django.views.generic.edit import UpdateView
from django.contrib import messages

from folioport.apps.my_css.forms import MyCssForm
from folioport.base.mixins import LoginRequiredMixin

MyCss = models.get_model('my_css', 'MyCss')
MyCssArchive = models.get_model('my_css', 'MyCssArchive')


class MyCssEditView(LoginRequiredMixin, UpdateView):
    model = MyCss
    form_class = MyCssForm
    template_name = 'dashboard/my_css/edit.html'

    def get_success_url(self):
        messages.success(self.request, 'CSS has been saved')
        return reverse_lazy('folioport:dashboard:my_css:edit',
                            kwargs={'pk': self.object.pk})


    def get_context_data(self, **kwargs):
        ctx = super(MyCssEditView, self).get_context_data(**kwargs)
        ctx['css_archives'] = MyCssArchive.objects.filter(user=self.request.user)
        return ctx


class MyCssRedirectToEditView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        my_css, _ = MyCss.objects.get_or_create(
            site=self.request.user.site, user=self.request.user)
        return reverse_lazy('folioport:dashboard:my_css:edit',
                            kwargs={'pk': my_css.id})
