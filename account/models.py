from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from .utils.choices import STATUS_CHOICES, ACTIVE
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=False, null=False, unique=True)

    # Varsayılan olarak kullanıcı aktif
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=ACTIVE)

    def __str__(self):
        return f"{self.username} | {self.email}"


class BlacklistedToken(models.Model):
    """
    Kara listeye alınmış JWT refresh token'ları saklamak için model.
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    refresh_token = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Blacklisted token for {self.user.email}"
