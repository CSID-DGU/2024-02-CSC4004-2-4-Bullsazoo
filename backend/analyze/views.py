from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import torch
from PIL import Image

class ObjectDetectionView(APIView):
    def get(self, request):
        return Response(
            {
                "message": "Use POST method to upload an image for detection.",
                "allowed_methods": ["POST"]
            },
            status=status.HTTP_200_OK
        )

    def post(self, request):
        # Check if an image is provided
        image_file = request.FILES.get('image')
        if not image_file:
            return Response(
                {
                    "status": "error",
                    "message": "Image file is required."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Load YOLOv5 model
            try:
                model = torch.hub.load('ultralytics/yolov5', 'custom', path='backend/test/yolov5/best.pt')
            except Exception as e:
                return Response(
                    {
                        "status": "error",
                        "message": f"Error loading YOLOv5 model: {str(e)}"
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

            # Process the image
            try:
                image = Image.open(image_file)
                results = model(image)

                # Parse results
                detected_objects = results.pandas().xyxy[0].name.tolist()

                return Response(
                    {
                        "status": "success",
                        "message": "Image processed successfully.",
                        "detected_objects": detected_objects
                    },
                    status=status.HTTP_202_ACCEPTED
                )
            except Exception as e:
                return Response(
                    {
                        "status": "error",
                        "message": f"Unexpected error while processing the image: {str(e)}"
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        except Exception as e:
            return Response(
                {
                    "status": "error",
                    "message": f"Unexpected server error: {str(e)}"
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
