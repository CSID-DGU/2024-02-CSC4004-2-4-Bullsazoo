from django.apps import AppConfig

class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.user'  # 정확한 경로를 설정 (backend.user)
