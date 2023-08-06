from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts.models import Profile
from quick_talk.models import Post, Comment


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'avatar']


class ProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    follows = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), many=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'follows', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'body', 'created_at']
        

    


