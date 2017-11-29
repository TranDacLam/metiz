from django import forms
from captcha.fields import ReCaptchaField


class PaymentForm(forms.Form):

    order_id = forms.CharField(max_length=250)
    order_type = forms.CharField(max_length=20)
    amount = forms.IntegerField()
    order_desc = forms.CharField(max_length=1000)
    bank_code = forms.CharField(max_length=20, required=False)
    language = forms.CharField(max_length=2)
    captcha = ReCaptchaField(required=True)
