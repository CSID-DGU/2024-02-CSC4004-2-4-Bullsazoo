from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from .models import User
from .serializers import UserSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "회원가입이 완료되었습니다."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')  # 사용자 이름(ID)
        personal_id = request.data.get('personal_id')  # 개인식별 ID(PW)

        # 사용자 인증
        user = authenticate(username=username, password=personal_id)
        if user:
            # 세션 생성 및 로그인 처리
            login(request, user)
            return Response({"message": "로그인 성공"}, status=status.HTTP_200_OK)

        return Response({"message": "로그인 정보가 올바르지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)

