from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=11, unique=True)
    
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name","last_name","phone_number"]
    
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def has_perm(self, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
    
    
