# Generated by Django 2.2.5 on 2019-12-09 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20191209_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='image',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='mobile',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='手机号'),
        ),
    ]
