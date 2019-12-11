from django.contrib import admin

# Register your models here.

from Goods.models import *

# admin.site.register(goods_good)

# class s (admin.TabularInline):
    # model = site


class GoodImageInline(admin.TabularInline):
    model = goods_goodimage


@admin.register(goods_good)
class GoodRegister(admin.ModelAdmin):

    inlines = [GoodImageInline]


admin.site.register(goods_category)
