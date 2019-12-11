from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()

# 地址表
class address_address(models.Model):
    name = models.CharField("姓名", max_length=20, null=True, blank=True)
    tel = models.CharField('联系电话', max_length =11, null=True, blank=True)
    address = models.CharField('详细地址', max_length =150, null=True, blank=True)
    created = models.DateField("创建时间", auto_now=True, null=True, blank=True)
    updated = models.DateField("修改时间", auto_now_add=True, null=True, blank=True)
    user_id = models.ForeignKey(User, verbose_name="用户id", on_delete=models.CASCADE)
    is_default = models.BooleanField("默认地址", null=True, blank=True)
    # address_address.objects.create(name='老王', tel='13697165025', address='湖北省武汉市', user_id=)
    def __str__(self):
        return self.name + self.address

    class Meta:
        verbose_name = "地址表"
        verbose_name_plural = verbose_name