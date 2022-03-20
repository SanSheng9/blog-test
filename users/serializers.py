from rest_framework.serializers import ModelSerializer
from users.models import CustomUser

class CustomUsersSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'groups']