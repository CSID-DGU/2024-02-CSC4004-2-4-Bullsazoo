from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'personal_id']

    def validate_personal_id(self, value):
        if not value.isalnum():
            raise serializers.ValidationError("개인 식별 ID는 영문자와 숫자만 포함할 수 있습니다.")
        return value

class LoginSerializer(serializers.Serializer):
    personal_id = serializers.CharField(max_length=20)

    def validate(self, data):
        personal_id = data.get('personal_id')
        if not User.objects.filter(personal_id=personal_id).exists():
            raise serializers.ValidationError("해당 개인 식별 ID가 존재하지 않습니다.")
        return data
