from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    personal_id = models.CharField(max_length=20, unique=True, verbose_name="개인 식별 ID")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="가입일")

    def __str__(self):
        return f"{self.username} ({self.personal_id})"
