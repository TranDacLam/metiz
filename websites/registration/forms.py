from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth import login
import datetime
import random
import sha
from core.custom_models import User
import messages as msg
import metiz_email


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    remember_me = forms.BooleanField(required=False)

    def clean_remember_me(self):
        cleaned_data = super(LoginForm, self).clean()
        remember_me = cleaned_data.get('remember_me')
        if not remember_me:
            settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = True
        else:
            settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False
        return remember_me

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        try:
            USER_MODEL = get_user_model()
            user = USER_MODEL.objects.get(email=email.strip())
        except USER_MODEL.DoesNotExist:
            raise forms.ValidationError(
                _(msg.EMAIL_NOT_EXIST), code='invalid')

        if user:
            if not user.check_password(password):
                raise forms.ValidationError(
                    _(msg.PASSWORD_WRONG), code='invalid')

            if user.is_active:
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(self.request, user)
            else:
                raise forms.ValidationError(_(msg.INACTIVE), code='invalid')
        else:
            raise forms.ValidationError(
                _(msg.EMAIL_NOT_EXIST), code='invalid')

        return cleaned_data


class MetizSignupForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(MetizSignupForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        exclude = ['is_staff', 'is_active', 'date_joined', 'modified',
                   'token_last_expired', 'activation_key', 'key_expires', 'password']

    def save(self, commit=True):
        user = super(MetizSignupForm, self).save(commit=False)
        # do custom stuff
        print 'User Register ', user
        if commit:
            salt = sha.new(str(random.random())).hexdigest()[:5]
            activation_key = sha.new(salt + user.email).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(30)
            user.activation_key = activation_key
            user.key_expires = key_expires
            user.save()

            message_html = "registration/email/metiz_account_created_confirm.html"
            subject = _(
                "[Metiz] You've been created an account - Click to Verify!")

            protocol = 'http://'
            if self.request.is_secure():
                protocol = 'https://'
            logo_url = protocol + \
                str(Site.objects.get_current()) + \
                '/static/websites/img/logo.png'
            url_activate = self.request.build_absolute_uri(
                reverse('confirm-activation', kwargs={'activation_key': activation_key}))
            data_binding = {
                'full_name': user.full_name,
                'email': user.email,
                'URL_LOGO': logo_url,
                'activate_url': url_activate
            }
            # http://{{ site.domain }}{% url 'confirm-activation'
            # activation_key %}

            metiz_email.send_mail(subject, None, message_html, settings.EMAIL_FROM, [
                                  email], data_binding)

        return user
