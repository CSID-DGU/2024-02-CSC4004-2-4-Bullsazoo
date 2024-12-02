from django.urls import path, include
from .views import RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # 회원가입
    path('login/', LoginView.as_view(), name='login'),
    path('user/', include('user.urls')),# 로그인
]
