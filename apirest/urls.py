from django.urls import path, include
from account.views import *
from apirest.views import *

urlpatterns = [
    path('user/', apilist.as_view()),
    path('user/<str:username>/', apidetail.as_view()),
]