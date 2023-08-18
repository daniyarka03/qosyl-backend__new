from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from main.models import Project, Post

User = get_user_model()


class MyUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined']

class UserSerializerWithToken(MyUserCreateSerializer):
    token = serializers.SerializerMethodField()  # Define the token field

    class Meta(MyUserCreateSerializer.Meta):
        fields = MyUserCreateSerializer.Meta.fields + ['token']  # Include the token field

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
