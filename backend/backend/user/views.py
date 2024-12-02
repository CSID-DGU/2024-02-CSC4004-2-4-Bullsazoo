from rest_framework.schemas import openapi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from .models import User
from .serializers import UserSerializer


def swagger_auto_schema(operation_description, request_body, responses):
    pass


class RegisterView(APIView):
    """회원가입 (POST)"""
    def post(self, request):
        personal_id = request.data.get("personal_id")
        if not personal_id:
            return Response({"error": "personal_id는 필수입니다"}, status=status.HTTP_400_BAD_REQUEST)

        # 이미 존재하는 사용자 확인
        if User.objects.filter(personal_id=personal_id).exists():
            return Response({"error": "이미 존재하는 사용자입니다"}, status=status.HTTP_400_BAD_REQUEST)

        # 사용자 생성
        try:
            user = User.objects.create(personal_id=personal_id)
            return Response({"message": "사용자가 성공적으로 등록되었습니다", "user_id": user.user_id}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginView(APIView):
    """로그인 (GET)"""
    def get(self, request):
        personal_id = request.query_params.get("personal_id")
        if not personal_id:
            return Response({"error": "personal_id는 필수입니다"}, status=status.HTTP_400_BAD_REQUEST)

        # 사용자 존재 여부 확인
        try:
            user = User.objects.get(personal_id=personal_id)
            return Response({"message": "로그인 성공", "user_id": user.user_id}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "유효하지 않은 personal_id입니다"}, status=status.HTTP_404_NOT_FOUND)
