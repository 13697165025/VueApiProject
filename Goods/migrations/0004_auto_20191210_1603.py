# Generated by Django 2.2.5 on 2019-12-10 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0003_auto_20191210_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods_good',
            name='created',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='goods_good',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='修改时间'),
        ),
    ]