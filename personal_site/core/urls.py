from django.conf import settings
from django.urls import include, path
from django.views.decorators.cache import cache_page
from rest_framework import routers

from .views import (
    ContactsView,
    ExperienceView,
    FeedbackView,
    GetAppProgramInterfaceView,
    HobbyView,
    HomePageView,
    LoginUser,
    RegisterUser,
    SkillDetailView,
    SkillsView,
    logout_user
)
from .views_api import (
    FeedbackViewSet,
    SkillViewSet
)

router = routers.DefaultRouter()
router.register(r'skills_list', SkillViewSet)
router.register(r'feedbacks_list', FeedbackViewSet)
# override api-root name
router.urls[-1].name = router.urls[-2].name = 'ervand-api-root'

urlpatterns = [
    # ======= URLS =====
    path('', cache_page(5)(HomePageView.as_view()), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('experience/', ExperienceView.as_view(), name='experience'),
    path('feedback/', FeedbackView.as_view(), name='feedback'),
    path('get_api/', GetAppProgramInterfaceView.as_view(), name='get_api'),
    path('hobby/', HobbyView.as_view(), name='hobby'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('site_login/', LoginUser.as_view(), name='site_login'),
    path('site_logout/', logout_user, name='site_logout'),
    path('skills/', SkillsView.as_view(), name='skills'),
    path('skills/<slug:skill_slug>/', SkillDetailView.as_view(), name='skill_detail'),

    # ======= API URLS =====
    path(f'{settings.API_V1_BASE_PREFIX}/', include(router.urls, )),
]
