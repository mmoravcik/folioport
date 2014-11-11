from django.views import generic
from django.core.urlresolvers import reverse_lazy

from . import forms


class UserRegistrationView(generic.FormView):
    form_class = forms.UserCreationForm
    template_name = 'account/registration.html'
    success_url = reverse_lazy('folioport:dashboard:home')

    def form_valid(self, form):
        form.save()
        return super(UserRegistrationView, self).form_valid(form)