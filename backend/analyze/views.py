import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from pathlib import Path
import torch

# YOLOv5 모델 로드
MODEL_PATH = 'backend/test/yolov5/best.pt'  # YOLOv5 모델 경로
model = torch.hub.load('ultralytics/yolov5', 'custom', path=MODEL_PATH)


class ImageAnalyzeView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        try:
            # 이미지 파일 가져오기
            image_file = request.FILES['image']
            temp_path = f"/tmp/{image_file.name}"

            # 임시 파일 저장
            with open(temp_path, 'wb+') as f:
                for chunk in image_file.chunks():
                    f.write(chunk)

            # YOLOv5를 사용한 분석
            results = model(temp_path)
            predictions = results.pandas().xyxy[0].to_dict(orient="records")

            # 임시 파일 삭제
            os.remove(temp_path)

            # 결과 반환
            return Response({"predictions": predictions}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
