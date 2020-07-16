from django.contrib.auth.models import User
from rest_framework import viewsets

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from task.models import Task, Project
from task.serializers import UserSerializer, CustomTokenObtainSerializer, TaskSerializer, ProjectSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return super().get_permissions()


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

