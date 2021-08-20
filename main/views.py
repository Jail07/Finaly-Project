from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorPermission
from rest_framework.viewsets import ModelViewSet

from main.models import *
from main.serializers import *


class PermissionMixin:
    def get_permission(self):
        if self.action == 'create':
            permissions = [IsAuthenticated, ]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsAuthorPermission, ]
        else:
            permissions = []
        return [permission() for permission in permissions]


class PostViewSet(PermissionMixin, ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # http_method_names = ['GET', 'POST', 'PUT', 'DELETE']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['action'] = self.action
        return context


class ReplyViewSet(PermissionMixin, ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['action'] = self.action
        return context


class StarView(PermissionMixin, ):
    queryset = Post.objects.get('star')
    serializer_class = PostSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['action'] = self.action
        return context



