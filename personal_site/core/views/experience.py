from django.views.generic.base import TemplateView

from core.models import Work
from utils.mixins import RenderMixin


class ExperienceView(RenderMixin, TemplateView):
    template_name = 'core/experience.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        render_data: dict = self.get_render_data(title="Experience")
        works = Work.objects.all()
        return {**context, **render_data, **{'works': works}}
