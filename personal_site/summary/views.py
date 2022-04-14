from django.views.generic.base import TemplateView

from summary.models import ItArea
from utils.mixins import RenderMixin


class SummaryView(RenderMixin, TemplateView):
    template_name = 'summary/summary.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        it_areas = ItArea.objects.all().prefetch_related('technologies')
        context = super().get_context_data(**kwargs)
        render_data: dict = self.get_render_data(title="Summary")
        return {**context, **render_data, **{'it_areas': it_areas}}
