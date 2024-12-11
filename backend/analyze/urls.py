from django.urls import path
from .views import ImageAnalyzeView

urlpatterns = [
    path('analyze/', ImageAnalyzeView.as_view(), name='image-analyze'),
]
