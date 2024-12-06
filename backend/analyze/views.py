import os
import logging
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ultralytics import YOLO
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser
from django.core.files.storage import default_storage
from .models import AnalyzeResult
from .yolov5_handler import detect_objects
from .serializers import AnalyzeResultSerializer, DetectionSerializer, ImageUploadSerializer
from rest_framework import serializers


# 저장된 데이터 조회
result = AnalyzeResult.objects.first()
print(result.detected_objects)  # 분석된 객체 출력
# 로그 설정
logger = logging.getLogger(__name__)

# YOLO 모델 로드
MODEL_PATH = settings.YOLO_MODEL_PATH  # YOLO 모델 경로
model = YOLO(MODEL_PATH)


# 파일 업로드를 위한 Serializer 정의
class ImageUploadSerializer(serializers.Serializer):
    file = serializers.FileField()


class YoloImageAnalysisView(APIView):
    parser_classes = [MultiPartParser]

    @swagger_auto_schema(
        operation_description="Upload an image to analyze using YOLOv5.",
        request_body=ImageUploadSerializer,  # Serializer 사용
        responses={
            200: AnalyzeResultSerializer(many=False),
            400: 'No file provided',
            500: 'Internal server error',
        },
    )
    def post(self, request, *args, **kwargs):
        logger.debug("Starting image analysis...")  # 로그 추가: 분석 시작
        serializer = ImageUploadSerializer(data=request.data)

        if not serializer.is_valid():
            logger.error(f"Invalid serializer: {serializer.errors}")  # 로그 추가: 유효하지 않은 데이터
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        file = serializer.validated_data['file']  # Serializer에서 파일 추출
        logger.debug(f"Received file: {file.name}")  # 로그 추가: 받은 파일 이름

        try:
            # 이미지 저장
            logger.debug(f"Saving image: {file.name}")  # 로그 추가: 이미지 저장 시작
            image_path = default_storage.save(f'uploads/{file.name}', file)
            absolute_image_path = os.path.join(settings.MEDIA_ROOT, image_path)

            logger.debug(f"Image saved at: {absolute_image_path}")  # 로그 추가: 이미지 경로 확인

            # YOLOv5 핸들러 호출
            logger.debug("Running YOLOv5 detection...")  # 로그 추가: YOLO 모델 실행
            detected_objects = detect_objects(absolute_image_path)

            logger.debug(f"Detected objects: {detected_objects}")  # 로그 추가: 탐지된 객체 확인

            # `detected_objects`는 리스트 형식이므로, 이를 DetectionSerializer로 직렬화
            detection_serializer = DetectionSerializer(detected_objects, many=True)

            # 응답 데이터 생성 (AnalyzeResult 모델에 저장)
            result = AnalyzeResult.objects.create(image=image_path, detected_objects=detection_serializer.data)
            response_serializer = AnalyzeResultSerializer(result)

            logger.debug("Analysis successful, returning result.")  # 로그 추가: 분석 성공
            return Response(response_serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            logger.error(f"Error during analysis: {str(e)}")  # 로그 추가: 예외 발생
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
