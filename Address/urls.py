from django.urls import path, include

from Address.views import *


urlpatterns = [
    path('list/', AddressListView.as_view()),
    path('list/<int:pk>/', AddressDetileView.as_view()),
]