from django.core.cache import cache
from django.views.generic.base import TemplateView

from core.models import Video
from utils.mixins import RenderMixin

DEFAULT_VIDEO_CACHE_TIME = 60


class HobbyView(RenderMixin, TemplateView):
    template_name = 'core/hobby.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        render_data: dict = self.get_render_data(title="Hobby")
        videos = cache.get('videos')
        if not videos:
            videos = Video.objects.all()
            cache.set('videos', videos, DEFAULT_VIDEO_CACHE_TIME)
        return {**context, **render_data, **{'videos': videos}}
