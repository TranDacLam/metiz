from captcha.fields import ReCaptchaField
from django.contrib.auth.forms import AuthenticationForm


class SecureAdminLoginForm(AuthenticationForm):
    captcha = ReCaptchaField(required=True)