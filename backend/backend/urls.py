from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
# 간단한 루트 응답 함수 추가
def home(request):
    return HttpResponse("Welcome to the Django Project!")



urlpatterns = [
    # 관리자 페이지 URL
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('analyze/', include('analyze.urls')),
    # user 앱의 URL 포함
    path('', home),  # 루트 URL 처리 추가
]

# 개발 환경에서 정적 및 미디어 파일 처리
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)