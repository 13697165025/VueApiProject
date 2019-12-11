from django.urls import path, include
from account.views import *
from Goods.views import *

urlpatterns = [
    path('goods/', GoodsListView.as_view()),
    path('goods/<int:pk>/', GoodsDetailView.as_view()),
]


