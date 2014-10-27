from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field

from django.contrib.auth import get_user_model
from django import forms


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password',
        widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation',
        widget=forms.PasswordInput)
    redirect_url = forms.CharField(
        widget=forms.HiddenInput, required=False)

    class Meta:
        model = get_user_model()
        fields = ('email', 'subdomain',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class DashboardAccountForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('site_name', 'site_logo', 'logo_width', 'site_catch_phrase', 'social_media',
                  'use_system_blog', 'own_blog_link', 'google_analytics_code')

    def __init__(self, *args, **kwargs):
        super(DashboardAccountForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('site_name'),
            Field('site_catch_phrase'),
            Field('site_logo'),
            Field('logo_width'),
            Field('google_analytics_code'),
            Field('social_media'),
            Field('use_system_blog'),
            Field('own_blog_link'),
        )