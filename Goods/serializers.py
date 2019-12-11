
from rest_framework import serializers
from Goods.models import *


# 商品列表
class Goodsserializers(serializers.Serializer):
    id = serializers.IntegerField()
    salePrice = serializers.DecimalField(max_digits=8, decimal_places=2)
    productName = serializers.CharField(max_length=100)
    subTitle = serializers.CharField(max_length=100)
    productImageBig = serializers.ImageField()
    detail = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()
    category_id_id = serializers.IntegerField()


# 轮播图
class Goodimgserializers(serializers.ModelSerializer):
    class Meta:
        model = goods_goodimage
        fields = "__all__"


# 商品详细
class GoodsDetailserializers(serializers.ModelSerializer):
    image = Goodimgserializers(many=True)

    class Meta:
        model = goods_good
        fields = "__all__"
