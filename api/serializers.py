from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "passwors")
        extra_kwargs = {"password": {"write_only": True, "required": True}}

    def create(self, validate):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return  user

class TaskSerializer(serializers.HyperlinkedModelSerializer):

    created_at = serializers.DateTimeField(format="%Y-%m-%d %h:%M", read_only=True)
    update_at = serializers.DateTimeField(format="%Y-%m-%d %h:%M", read_only=True)

    class Meta:
        model = Task
        fields = ["id", "title", "created_At", "updated_at"]