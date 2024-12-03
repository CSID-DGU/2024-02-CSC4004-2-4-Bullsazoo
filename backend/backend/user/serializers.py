from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'personal_id', 'email']  # 사용자 이름, 개인식별 ID, 이메일 포함
        extra_kwargs = {
            'personal_id': {'write_only': True},  # personal_id는 출력하지 않음
        }

    def create(self, validated_data):
        """
        회원가입 시, personal_id를 Django의 password 필드에 저장.
        Django 인증 시스템에서 해시된 비밀번호를 사용하기 위해 make_password를 적용.
        """
        validated_data['password'] = make_password(validated_data.pop('personal_id'))  # 비밀번호 해시화
        return super().create(validated_data)
