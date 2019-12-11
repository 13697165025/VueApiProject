import decimal
import json

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.


# 商品分类表
class goods_category(models.Model):
    name = models.CharField("分类名称", max_length=50, null=True, blank=True)
    created = models.DateField("创建时间", auto_now=True, null=True, blank=True)
    updated = models.DateField("修改时间", auto_now_add=True, null=True, blank=True)
    slug = models.CharField("动作", max_length=120, null=True, blank=True)
    parent_id = models.ForeignKey("goods_category", verbose_name="自己关联自己", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "商品分类表"
        verbose_name_plural = verbose_name


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        super(DecimalEncoder, self).default(o)


# 商品表
class goods_good(models.Model):
    salePrice = models.DecimalField("单价", max_digits=7,decimal_places=2)
    productName = models.CharField("商品名称", max_length=50, null=True, blank=True)
    subTitle = models.CharField("商品标题", max_length =250, null=True, blank=True)
    productImageBig = models.ImageField("商品图", upload_to='goodsimg', null=True, blank=True)
    detail = RichTextUploadingField("商品详细", null=True, blank=True)
    created = models.DateTimeField("创建时间", auto_now=True, null=True, blank=True)
    updated = models.DateTimeField("修改时间", auto_now_add=True, null=True, blank=True)
    category_id = models.ForeignKey(goods_category, verbose_name="商品分类id", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "商品表"
        verbose_name_plural = verbose_name

    def to_json(self):
        return {"a": self.salePrice}


# 商品轮播图片表
class goods_goodimage(models.Model):
    image = models.ImageField("商品轮播图", upload_to='goodschild', null=True, blank=True)
    created = models.DateField("创建时间", auto_now=True, null=True, blank=True)
    updated = models.DateField("修改时间", auto_now_add=True, null=True, blank=True)
    good_id = models.ForeignKey(goods_good, verbose_name="商品id", related_name='image', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "商品轮播图片表"
        verbose_name_plural = verbose_name