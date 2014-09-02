from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.sites.models import get_current_site


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