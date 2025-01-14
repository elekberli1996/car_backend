from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from .utils.choices import STATUS_CHOICES, ACTIVE
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=False, null=False, unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=ACTIVE)

    objects = CustomUserManager()  # Custom Manager

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

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


# id   username   first_name  last_name   email  password  is_staff is_active date_joined last_login
#  phone (CustomField) status (CustomField) groups  user_permissions
