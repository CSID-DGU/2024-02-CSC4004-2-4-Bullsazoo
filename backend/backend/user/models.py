from django.contrib.auth.models import AbstractUser
from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)  # PostgreSQL의 SERIAL과 매핑
    personal_id = models.CharField(max_length=100, unique=True)  # UNIQUE 제약 조건

    def __str__(self):
        return self.personal_id

    class Meta:
        db_table = "users"  # PostgreSQL의 'users' 테이블과 연결




