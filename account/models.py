from django.contrib.auth.models import AbstractUser
from .utils.choices import STATUS_CHOICES, ACTIVE
from django.db import models


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=False, null=False, unique=True)

    # Varsayılan olarak kullanıcı aktif
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=ACTIVE)

    def __str__(self):
        return f"{self.username} | {self.email}"
