from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView

from subscribe.celery.tasks import send_welcome
from subscribe.form import SubscribeForm
from subscribe.models import Subscription
from utils.mixins import RenderMixin


class SubscribeView(RenderMixin, CreateView):
    form_class = SubscribeForm
    template_name = 'subscribe/main.html'
    success_url = reverse_lazy('success')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        render_data: dict = self.get_render_data(title="Subscribe")
        return {**context, **render_data}

    def form_valid(self, form):
        user_id = self.request.user.id
        daily = form.instance.daily
        subscription = Subscription.objects.create(
            user_id=user_id, daily=daily)
        subscription.save()
        send_welcome.apply_async(
            kwargs=dict(email=self.request.user.email,
                        username=self.request.user.username))

        return redirect(self.success_url)


class UnsubscribeView(RenderMixin, CreateView):
    form_class = SubscribeForm
    template_name = 'subscribe/main.html'
    success_url = reverse_lazy('success')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        render_data: dict = self.get_render_data(title="Unsubscribe")
        return {**context, **render_data}

    def form_valid(self, form):
        subscription = self.request.user.subscriptions.first()
        subscription.delete()
        return redirect(self.success_url)


class SuccessView(RenderMixin, TemplateView):
    template_name = 'subscribe/success.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        render_data: dict = self.get_render_data(title="Success")
        return {**context, **render_data}
