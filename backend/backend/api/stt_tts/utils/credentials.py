import os
# Google Cloud 인증 키 경로
GOOGLE_APPLICATION_CREDENTIALS = "C:\Google_Authorization_keys\dynamic-fulcrum-425407-h0-76b27ca3e53d.json"

# 환경 변수에 인증 키 등록
def initialize_credentials():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS

# 타 사용자가 사용 시, 키 파일을 직접 제공받거나 환경변수를 설정하여야함