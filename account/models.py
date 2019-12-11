from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Usermodel(AbstractUser):
    mobile = models.CharField('手机号', max_length=20, null=True, blank=True, editable=False)
    image = models.CharField('头像', max_length=100, null=True, blank=True, editable=False)

    def to_json(self):
        json_post = {
            "id": self.id,
            "username": self.username,
            "mobile": self.mobile,
            "image":self.image
        }
        return json_post

