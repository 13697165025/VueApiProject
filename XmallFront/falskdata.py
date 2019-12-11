from faker import Faker

from Goods.models import *
from random import randint


def goodspost(count=100):
    fake = Faker(locale='zh_CN')
    i = 0
    ca = goods_category.objects.get(pk=1)
    while i < count:
        goods_good.objects.create(salePrice=randint(1, 9999), productName=fake.name(), subTitle='测试数据',
        productImageBig='goodsimg/babybazzi.jpg', detail=fake.text(), category_id=ca)
        i += 1


