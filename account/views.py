from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, View
from django.http import HttpResponse, JsonResponse
from account.models import *
import json


class UserListView(View):
    def get(self, request, username=None):
        u = Usermodel.objects.all()
        jsonstr = json.dumps(u.to_json())
        return JsonResponse(jsonstr)
        # return HttpResponse(jsonstr, content_type='application/json')

    def post(self, request, username=None):
        print(request.POST.get("username"))


def adjons(request, username=None):
    if request.method == "GET":
        u = Usermodel.objects.get(username=username)
        jsonstr = json.dumps(u.to_json())
        return HttpResponse(jsonstr, content_type='application/json')
    elif request.method == "POST":
        print(json.loads(request.body))
        return HttpResponse(json.dumps({"a": 1}))





