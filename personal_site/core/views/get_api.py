from django.views.generic.base import TemplateView

from utils.menu import APIS
from utils.mixins import RenderMixin


class GetAppProgramInterfaceView(RenderMixin, TemplateView):
    template_name = 'core/get_api.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        render_data: dict = self.get_render_data(title="Get API")
        return {**context, **render_data, **{'apis': APIS}}
