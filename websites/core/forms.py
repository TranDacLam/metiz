# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site
from django.conf import settings
from django import forms
from captcha.fields import ReCaptchaField
from core.models import Contact
from registration import metiz_email


class ContactForm(forms.Form):
    # error_messages={'invalid': _('User with this phone already exists.')}
    name = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.TextInput())
    phone = forms.IntegerField(error_messages={'invalid': _('Enter a whole number.')}, widget=forms.TextInput(), required=True)
    message = forms.CharField(widget=forms.TextInput(), required=False)
    captcha = ReCaptchaField(required=True)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

    def save(self, commit=True, is_secure=False):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        phone = self.cleaned_data['phone']
        message = self.cleaned_data['message']

        if commit:
            try:
                contact = Contact(name=name, email=email, phone=phone, message=message)
                contact.save()

                message_html = "websites/email/contact_email.html"

                protocol = 'http://'
                if is_secure:
                    protocol = 'https://'
                logo_url = protocol + \
                    str(Site.objects.get_current()) + \
                    '/static/websites/img/logo.png'

                _subject = _("[Metiz] Hỗ trợ khách hàng")

                data_render = {
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "subject": _subject,
                    "message": message,
                    'logo_url': logo_url

                }

                metiz_email.send_mail(subject=_subject, message_plain=None, message_html=message_html,
                                      email_from=settings.DEFAULT_FROM_EMAIL, email_to=[settings.DEFAULT_TO_ADMIN_EMAIL], data_binding=data_render)
            except Exception, e:
                print 'Error ContactForm ', e
                raise Exception(
                    "ERROR : Internal Server Error .Please contact administrator.")

