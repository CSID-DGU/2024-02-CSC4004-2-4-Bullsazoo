from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'personal_id']  # 사용자 이름(ID)와 개인식별 ID(PW)를 포함

    def create(self, validated_data):
        # personal_id를 password로 저장
        validated_data['password'] = make_password(validated_data.pop('personal_id'))
        return super().create(validated_data)
