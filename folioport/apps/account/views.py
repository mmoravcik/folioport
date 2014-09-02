from django.views import generic
from django.conf import settings

from . import forms


class UserRegistrationView(generic.FormView):
    form_class = forms.UserCreationForm
    template_name = 'account/registration.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(UserRegistrationView, self).form_valid(form)