from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

from django.utils.timezone import now
from random import choice
from Goods.models import goods_good

User = get_user_model()


# 随机数
def get_random_orderno():
    timestart = now().strftime("%Y%m%d%H%M%S%F")
    strnum = "0123456789"
    list_time = []
    for i in range(6):
        list_time.append(choice(strnum))
    return timestart + "".join(list_time)


# 订单表
class order_order(models.Model):
    STATE_NOPAY = "0"
    STATE_NODELIVERY = "1"
    STATE_DELIVERY = "2"
    STATE_GOODS = "3"
    STATE_OVERDUE = "4"
    STATE_CANVEL = "5"

    choect = (
        (STATE_NOPAY, "未支付"),
        (STATE_NODELIVERY, "未发货"),
        (STATE_DELIVERY, "已发货"),
        (STATE_GOODS, "确认发货"),
        (STATE_OVERDUE, "已过期"),
        (STATE_CANVEL, "已取消")
    )

    order_sn = models.CharField("订单编号", default=get_random_orderno,  max_length=30,  unique=True, blank=True, editable=False)
    trade_no = models.CharField("交易编号", default=get_random_orderno, max_length=200, unique= True, blank=True, editable=False)
    pay_status = models.CharField("订单状态", choices=choect, default=STATE_NOPAY, max_length=4)
    post_script = models.CharField("请求脚本", max_length=200, null=True, blank=True)
    order_total = models.DecimalField("订单金额", max_digits=20, decimal_places=2, default=0.00)
    pay_time = models.DateField("订单时间", auto_now=True, null=True, blank=True)
    address = models.CharField("地址", max_length=100, null=True, blank=True)
    singer_name = models.CharField("用户姓名", max_length=20, null=True, blank=True)
    singer_mobile = models.CharField("用户姓名", max_length=11, null=True, blank=True)
    created = models.DateField("创建时间", auto_now=True, null=True, blank=True)
    updated = models.DateField("修改时间", auto_now_add=True, null=True, blank=True)
    user_id = models.ForeignKey(User, verbose_name="用户id", on_delete=models.CASCADE)
    close_time = models.DateField("关闭时间", auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = "订单表"
        verbose_name_plural = verbose_name


# 订单商品表
class order_ordergoods(models.Model):
    goods_num = models.IntegerField("商品编号", null=True, blank=True)
    price = models.DecimalField("商品金额", max_digits=20, decimal_places=2, default=0.00)
    created = models.DateField("创建时间", auto_now=True, null=True, blank=True)
    updated = models.DateField("修改时间", auto_now_add=True, null=True, blank=True)
    order_id = models.ForeignKey(order_order, verbose_name="订单id", on_delete=models.CASCADE)
    good_id = models.ForeignKey(goods_good, verbose_name="商品id", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "订单商品表"
        verbose_name_plural = verbose_name
