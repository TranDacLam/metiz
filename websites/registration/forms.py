from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites.models import Site
from django.contrib.auth import login
from django.core.urlresolvers import reverse
from django.conf import settings
import datetime
import random
import sha
from core.custom_models import User
import messages as msg
import metiz_email
from django.utils import timezone


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
                msg.EMAIL_NOT_EXIST, code='invalid')

        if user:
            if not user.check_password(password):
                raise forms.ValidationError(
                    msg.PASSWORD_WRONG, code='invalid')

            if user.is_active:
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(self.request, user)
            else:
                raise forms.ValidationError(msg.INACTIVE, code='invalid')
        else:
            raise forms.ValidationError(
                msg.EMAIL_NOT_EXIST, code='invalid')

        return cleaned_data


class MetizSignupForm(UserCreationForm):

    phone = forms.CharField(error_messages={'unique':_("User with this phone already exists.")})
    email = forms.CharField(error_messages={'unique':_("User with this email already exists.")})
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(MetizSignupForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        exclude = ['is_staff', 'is_active', 'date_joined', 'modified',
                   'token_last_expired', 'activation_key', 'key_expires', 'password']

    def save(self, commit=True):
        # call save function of super
        user = super(MetizSignupForm, self).save(commit=False)
        try:
            if commit:
                salt = sha.new(str(random.random())).hexdigest()[:5]
                activation_key = sha.new(salt + user.email).hexdigest()
                key_expires = timezone.now() + datetime.timedelta(30)
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
                    '/static/websites/images/Metiz_logo/METIZ_LOGO_WEB.png'
                url_activate = self.request.build_absolute_uri(
                    reverse('confirm-activation', kwargs={'activation_key': activation_key}))
                data_binding = {
                    'full_name': user.full_name,
                    'email': user.email,
                    'URL_LOGO': logo_url,
                    'activate_url': url_activate
                }
                # Send email activation link
                metiz_email.send_mail(subject, None, message_html, settings.DEFAULT_FROM_EMAIL, [
                                      user.email], data_binding)
            return user

        except Exception, e:
            print 'Save Form Error ', e
            raise Exception('Internal Server Error.')


class UpdateUserForm(forms.Form):

    full_name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    birth_date = forms.DateField(required=False)
    address = forms.CharField(required=False)
    personal_id = forms.CharField(required=False)
    gender = forms.CharField(required=False)
    city = forms.CharField(required=False)
    district = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super(UpdateUserForm, self).__init__(*args, **kwargs)

    def clean_phone(self):
        cleaned_data = super(UpdateUserForm, self).clean()
        phone = cleaned_data.get("phone")
        
        check_phone = User.objects.filter(phone=phone).exclude(pk=self.user.id)
        if check_phone.count() > 0:
            raise forms.ValidationError(_('This phone is already in use.'))
        return phone

    def save(self):
        self.user.full_name = self.cleaned_data.get('full_name')
        self.user.phone = self.cleaned_data.get('phone')
        self.user.birth_date = self.cleaned_data.get('birth_date')
        self.user.address = self.cleaned_data.get('address')
        self.user.personal_id = self.cleaned_data.get('personal_id')
        self.user.gender = self.cleaned_data.get('gender')
        self.user.city = self.cleaned_data.get('city')
        self.user.district = self.cleaned_data.get('district')
        self.user.save()
        return self.user


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(required=True)
    new_password = forms.CharField(required=True)
    new_password2 = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        valid = self.user.check_password(old_password)
        if not valid:
            raise forms.ValidationError(
                _("The old password fields did not match."))

    def clean(self):
        cleaned_data = super(ChangePasswordForm, self).clean()
        new_password = self.cleaned_data.get('new_password')
        new_password2 = self.cleaned_data.get('new_password2')
        if new_password != new_password2:
            raise forms.ValidationError(
                _("The two password fields did not match."))
        return cleaned_data

    def save(self, commit=True):
        """
        Saves the new password.
        """
        if commit:
            self.user.set_password(self.cleaned_data["new_password"])
            self.user.save()
        return self.user
