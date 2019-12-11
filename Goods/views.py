from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from Goods.models import *
from Goods.serializers import *


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'size'
    max_page_size = 80


# 商品列表
class GoodsListView(generics.ListAPIView):

    queryset = goods_good.objects.all()
    serializer_class = Goodsserializers
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        queyset = super().get_queryset()
        priceGt = self.request.query_params.get("priceGt")
        priceLte = self.request.query_params.get("priceLte")
        if self.request.query_params.get("sort"):
            sort = self.request.query_params.get("sort")
            priceGt = "1" if priceGt == "" else priceGt
            priceLte = "9999" if priceLte == "" else priceLte
            if sort == "1":
                queyset = queyset.filter(salePrice__gt=priceGt, salePrice__lt=priceLte).all().order_by("salePrice")
            elif sort == "-1":
                queyset = queyset.filter(salePrice__gt=priceGt, salePrice__lt=priceLte).all().order_by("-salePrice")
        return queyset


# 商品详细:
class GoodsDetailView(generics.RetrieveAPIView):
    queryset = goods_good.objects.all()
    serializer_class = GoodsDetailserializers


