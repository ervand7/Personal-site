from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from utils.mixins import PermissionMixin
from .models import Feedback, ItArea, Skill
from .permissions import IsOwnerOrReadOnly, IsSuperuserOrReadOnly
from .serializers import FeedbackSerializer, SkillSerializer
from .utils.drf_pagination import CoreAPIListPagination


class SkillViewSet(PermissionMixin, viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes_by_action = {
        'create': [IsSuperuserOrReadOnly],
        'list': [AllowAny],
        'retrieve': [AllowAny],
        'update': [IsSuperuserOrReadOnly],
        'partial_update': [IsSuperuserOrReadOnly],
        'destroy': [IsSuperuserOrReadOnly]
    }

    def get_permissions(self):
        return super(SkillViewSet, self).get_permissions_by_action()

    @action(methods=['get'], detail=True)
    def it_area(self, request, pk=None):
        # http://127.0.0.1:8000/api/v1/skills_list/{id of it_area}/it_area/
        """ Adding a new route named 'it_area' through action decorator """
        it_area = ItArea.objects.filter(pk=pk).first()
        if not it_area:
            return Response({'msg': 'Not found'})
        return Response({'it_area': it_area.name})

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FeedbackViewSet(PermissionMixin, viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    filterset_fields = ['category', 'user__username']
    search_fields = ['description', 'content']
    ordering_fields = ['category', 'user']

    pagination_class = CoreAPIListPagination
    permission_classes_by_action = {
        'create': [IsAuthenticated],
        'list': [AllowAny],
        'retrieve': [AllowAny],
        'update': [IsOwnerOrReadOnly],
        'partial_update': [IsOwnerOrReadOnly],
        'destroy': [IsOwnerOrReadOnly]
    }

    def get_permissions(self):
        return super(FeedbackViewSet, self).get_permissions_by_action()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
