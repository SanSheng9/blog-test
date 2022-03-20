from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUsersViewSet

router = DefaultRouter()
router.register(r'users', CustomUsersViewSet)
urlpatterns = [
    path("", include(router.urls))
]