from django.shortcuts import render

# Create your views here.

from rest_framework import mixins, generics
from Address.models import *
from Address.serializers import UserSeralizer


# 列表页
class AddressListView(generics.ListCreateAPIView):
    queryset = address_address.objects.all()
    serializer_class = UserSeralizer


# 详细页
class AddressDetileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = address_address.objects.all()
    serializer_class = UserSeralizer



