from django.views.generic import DetailView, ListView

from core.models import Skill
from utils.mixins import RenderMixin


class SkillsView(RenderMixin, ListView):
    model = Skill
    template_name = 'core/skills.html'
    context_object_name = 'skills'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        render_data: dict = self.get_render_data(title="Skills")
        return {**context, **render_data}

    def get_queryset(self):
        return Skill.objects.filter(is_published=True). \
            select_related('it_area', 'work')


class SkillDetailView(RenderMixin, DetailView):
    model = Skill
    template_name = 'core/skill_detail.html'
    slug_url_kwarg = 'skill_slug'
    context_object_name = 'skill'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        title = f'Skills - {kwargs["object"].slug}'
        render_data: dict = self.get_render_data(title=title)
        return {**context, **render_data}
