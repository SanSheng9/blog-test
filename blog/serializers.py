from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from blog.models import Post, User, Comment

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['login', 'about_me', 'avatar', 'is_active']