from django.urls import path
from .views import RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # 회원가입 엔드포인트
    path('login/', LoginView.as_view(), name='login'),           # 로그인 엔드포인트
]
