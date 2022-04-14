from string import punctuation
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Feedback
from captcha.fields import CaptchaField


class FeedbackForm(forms.ModelForm):
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['age_confirmation'].label = 'I have 18'
        self.fields['age_confirmation'].required = True

    class Meta:
        model = Feedback
        fields = ['description', 'category', 'content', 'age_confirmation', 'image']
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_description(self):
        description = self.cleaned_data['description']
        forbidden_symbols = punctuation.replace('-', '')
        for i in forbidden_symbols:
            if i in description:
                raise ValidationError(f'Forbidden symbol: {i}')

        return description


class UserRegisterForm(UserCreationForm):
    attrs = {'class': 'form-input'}

    username = forms.CharField(
        label='Username', widget=forms.TextInput(attrs=attrs))
    email = forms.EmailField(
        label='Email', widget=forms.EmailInput(attrs=attrs))
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs=attrs))
    password2 = forms.CharField(
        label='Password again', widget=forms.PasswordInput(attrs=attrs))
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    attrs = {'class': 'form-input'}

    username = forms.CharField(
        label='Login', widget=forms.TextInput(attrs=attrs))
    password = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs=attrs))
