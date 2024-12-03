from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    personal_id = models.CharField(max_length=100, unique=True)  # 개인식별 ID

    USERNAME_FIELD = 'username'  # 사용자 이름을 ID로 사용
    REQUIRED_FIELDS = []  # 추가 필드는 필요하지 않음

    class Meta:
        db_table = 'users'  # PostgreSQL의 'users' 테이블과 연결
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username