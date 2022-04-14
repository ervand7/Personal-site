from django.views.generic.base import TemplateView

from utils.mixins import RenderMixin


class HomePageView(RenderMixin, TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        render_data: dict = self.get_render_data(title="Home page")
        return {**context, **render_data}
