from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import UserManager
from shop.models import Product


class User(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True)
    nickname = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    likes = models.ManyToManyField(Product, blank=True, related_name='likes')
    is_manager = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.nickname

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def get_likes_count(self):
        return self.likes.count()
