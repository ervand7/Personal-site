from captcha.fields import CaptchaField
from django import forms

from subscribe.models import Subscription


class SubscribeForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Subscription
        fields = ('daily',)
