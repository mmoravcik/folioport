from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.views.generic import RedirectView
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.contrib.sites.models import get_current_site
from django.contrib.auth import get_user_model

from folioport.apps.account.forms import DashboardAccountForm
from folioport.base.mixins import LoginRequiredMixin



class AccountEditView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = DashboardAccountForm
    template_name = 'dashboard/account/edit.html'

    def get_success_url(self):
        messages.success(self.request, 'Account has been saved')
        return reverse_lazy('folioport:dashboard:account:edit',
                            kwargs={'pk': self.object.pk})


class AccountRedirectToEditView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('folioport:dashboard:account:edit',
                            kwargs={'pk': self.request.user.id})
