from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    full_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.username}'
