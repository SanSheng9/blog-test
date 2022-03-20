from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from users.models import CustomUser
from users.serializers import CustomUsersSerializer


class CustomUsersViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUsersSerializer