from django.contrib.auth import get_user_model
from rest_framework import routers, serializers
from account.models import *

from account.models import *


class UserSeralizer(serializers.ModelSerializer):
    mobile = serializers.CharField(max_length=20, label='电话')
    image = serializers.CharField(max_length=100, label='头像')

    class Meta:
        model = Usermodel
        fields = ['id', 'username', 'mobile', 'image']

    def update(self, instance, validated_data):
        return instance.objects.update_or_create(**validated_data)


# 用户名和密码
class UserPwaSerializer(serializers.Serializer):
    username =serializers.CharField(max_length=120, label='用户名')
    password = serializers.CharField(max_length=120, label="密码")

    def create(self, validated_data):
        return Usermodel.objects.create_user(**validated_data)

