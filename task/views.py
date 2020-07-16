# Create your views here.
import django_filters.rest_framework
from django.contrib.auth.models import User
from rest_framework import filters, viewsets
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from task.models import Project, Task
from task.serializers import (CustomTokenObtainSerializer, ProjectSerializer,
                              TaskSerializer, UserSerializer)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['first_name', 'last_name', 'email',]
    search_fields = ['first_name', 'last_name', 'email',]

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return super().get_permissions()



class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name',]
    search_fields = ['name',]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(project__owner=user)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name',]
    search_fields = ['name',]

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(owner=user)
