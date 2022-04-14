from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from core.form import FeedbackForm
from utils.mixins import RenderMixin


class FeedbackView(
    RenderMixin,
    LoginRequiredMixin,
    SuccessMessageMixin,
    CreateView
):
    form_class = FeedbackForm
    template_name = 'core/feedback.html'
    success_url = reverse_lazy('feedback')
    success_message = 'The form was completed successfully!'
    login_url = reverse_lazy('site_login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        render_data: dict = self.get_render_data(title="Feedback")
        return {**context, **render_data}
