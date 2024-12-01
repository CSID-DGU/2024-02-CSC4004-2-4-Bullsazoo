import cv2
import torch
import time
import pathlib as pl
import requests

from backend.backend.api.stt_tts.tts_handler import generate_speech
from backend.backend.api.gpt.gpt_text_generator import gpt_response
from backend.backend.settings import BASE_DIR
from backend.backend.test.yolov5.loadimage import update_dataset_yaml

#감지한 상품 중에 라벨에 없으면 커트
#삼양라면, 침대가 라벨에 잡힐 시, 침대는 커트

temp = pl.PosixPath
pl.PosixPath = pl.WindowsPath

# 라벨을 서버에 POST 요청으로 전송(미완)
def send_labels_to_server(labels):
    url = "http://127.0.0.1:8000/detect/"  # DRF API URL
    response = requests.post(url, json={"labels": labels})
    if response.status_code == 200:
        print("DB 저장 성공:", response.json())
    else:
        print("DB 저장 실패:", response.text)

# 실시간 객체 탐지
def detect_objects_realtime(model):
    #dataset.YML 설정
    update_dataset_yaml()
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        generate_speech("웹캠을 찾을 수 없습니다. 다시 시도하세요", None)

    generate_speech("화면에 물건을 가까이 대주세요", None)

    while cap.isOpened():
        global detected
        detected = False

        start_time = time.time()
        execution_time = time.time()

        while execution_time - start_time < 5.0:
            ret, frame = cap.read()
            if not ret:
                generate_speech("프레임 캡처에 실패했습니다", None)
                break
            # YOLOv5 모델로 객체 탐지
            results = model(frame)
            labels = results.pandas().xyxy[0]["name"].tolist()  # 탐지된 객체 라벨
            # 탐지 결과 그리기
            annotated_frame = results.render()[0]  # 첫 번째 이미지만 사용
            # 객체 탐지 결과를 화면에 표시
            cv2.imshow("Yolov5 Detection", annotated_frame)
            # 'q'를 누르면 종료
            if cv2.waitKey(1) & 0xFF == ord('q'):
                return

            if labels:
                detected = True
                for label in labels:
                    # GPT-4를 통해 상세 정보 생성
                    description = gpt_response(f"{label}의 품목명이나 가격에 대해 알려줘")
                    # TTS를 사용해 음성 출력
                    generate_speech(description, None)

            execution_time = time.time()

        # 5초 이상 객체를 탐지하지 못한 경우
        if not detected:
            generate_speech("탐지된 물체가 없습니다. 이미지 촬영 각도를 조정해주세요", None)

    cap.release()
    cv2.destroyAllWindows()

def main():
    # YOLOv5 모델 경로
    path = str(BASE_DIR) + '/backend/test/yolov5/runs/train/exp7/weights/last.pt'
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=path, force_reload=True) # 모델 로드
    detect_objects_realtime(model)  # 실시간 객체 탐지

# 테스트 실행
if __name__ == "__main__":
    main()