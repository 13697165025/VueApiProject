from rest_framework import routers, serializers
from Address.models import *


class UserSeralizer(serializers.ModelSerializer):
    class Meta:
        model = address_address
        fields = ['name', 'tel', 'address', 'is_default']

    def create(self,validated_data):
        print(validated_data)
        return address_address.objects.create(**validated_data)