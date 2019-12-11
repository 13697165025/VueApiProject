from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

from Goods.models import *

User= get_user_model()


# 购物车表
class cart_cart(models.Model):
    checked = models.BooleanField("商品编号", default=False)
    created = models.DateField("创建时间", auto_now=True, null=True, blank=True)
    updated = models.DateField("修改时间", auto_now_add=True, null=True, blank=True)
    good_id = models.ForeignKey(goods_good, verbose_name="商品id", on_delete=models.CASCADE, null=True, blank=True)
    user_id = models.ForeignKey(User, verbose_name="商品id", on_delete=models.CASCADE, null=True, blank=True)
    good_num = models.PositiveIntegerField("商品数量", null=True, blank=True)

    class Meta:
        verbose_name = "商品分类表"
        verbose_name_plural = verbose_name
