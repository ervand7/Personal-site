from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from core.form import UserLoginForm, UserRegisterForm
from utils.mixins import RenderMixin


class RegisterUser(RenderMixin, CreateView):
    form_class = UserRegisterForm
    template_name = 'core/register.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        render_data: dict = self.get_render_data(title="Registration")
        return {**context, **render_data}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(RenderMixin, LoginView):
    form_class = UserLoginForm
    template_name = 'core/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        render_data: dict = self.get_render_data(title="Authorization")
        return {**context, **render_data}

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('site_login')
