from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response

from account.models import *

from rest_framework import mixins, generics
from apirest.serializers import UserSeralizer, UserPwaSerializer


class apilist(generics.ListCreateAPIView):
    queryset = Usermodel.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return UserSeralizer
        elif self.request.method == "POST":
            return UserPwaSerializer


class apidetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsOneselfOrUpdate, IsOwnerOrReadOnly]
    queryset = Usermodel.objects.all()
    serializer_class = UserSeralizer

    lookup_field = "username"
    lookup_url_kwarg = "username"

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(username=self.object, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        self.object.set_username(serializer.validated_data["username"])
        self.object.set_mobile(serializer.validated_data["mobile"])
        self.object.set_image(serializer.validated_data["image"])
        self.object.save()
        return Response({"status": "信息修改成功！"})

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.update(request, *args, **kwargs)




