from __future__ import division

from google.cloud import speech
import pyaudio
import queue
import requests
import time

from backend.backend.api.stt_tts.utils.credentials import initialize_credentials

# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 1000)  # 100ms

class MicrophoneStream(object):
    """Opens a recording stream as a generator yielding the audio chunks."""

    def __init__(self, rate, chunk):
        self._rate = rate
        self._chunk = chunk
        self._buff = queue.Queue()
        self.closed = True

    def __enter__(self):
        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
            channels=1, rate=self._rate,
            input=True, frames_per_buffer=self._chunk,
            stream_callback=self._fill_buffer,
        )
        self.closed = False
        return self

    def __exit__(self, type, value, traceback):
        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True
        self._buff.put(None)
        self._audio_interface.terminate()

    def _fill_buffer(self, in_data, frame_count, time_info, status_flags):
        """Continuously collect data from the audio stream, into the buffer."""
        self._buff.put(in_data)
        return None, pyaudio.paContinue

    def generator(self):
        while not self.closed:
            chunk = self._buff.get()
            if chunk is None:
                return
            data = [chunk]
            while True:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)
                except queue.Empty:
                    break
            yield b''.join(data)

def listen_before_click(responses, text_file):
    """Iterates through server responses and prints them, also saving to a file."""
    """Continuously checks button status and processes responses."""
    final_transcript = ""
    button_api_url = ""  # Django 버튼 상태 API

    for response in responses:
        if not response.results:
            continue

        result = response.results[0]
        if not result.alternatives:
            continue

        transcript = result.alternatives[0].transcript
        final_transcript += transcript + " "

        # 버튼 상태 확인
        try:
            api_response = requests.get(button_api_url)
            if api_response.status_code == 200 and api_response.json().get("status") == "Button clicked":
                if final_transcript.strip():
                    print("음성 명령:", final_transcript.strip())
                    text_file.write(final_transcript.strip() + "\n")
        except requests.RequestException as e:
            print(f"버튼 상태 확인 중 오류 발생: {e}")

        time.sleep(0.5)

def main():
    initialize_credentials()
    language_code = 'ko-KR'  # a BCP-47 language tag

    client = speech.SpeechClient()
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code=language_code,
    )
    streaming_config = speech.StreamingRecognitionConfig(
        config=config,
        interim_results=True
    )

    output_text_file = ""  # 결과를 저장할 텍스트 파일 경로
    with open(output_text_file, "w", encoding="utf-8") as text_file:
        with MicrophoneStream(RATE, CHUNK) as stream:
            audio_generator = stream.generator()
            try:
                # 요청 생성
                requests = (speech.StreamingRecognizeRequest(audio_content=content)
                            for content in audio_generator)
                # 응답 받기
                responses = client.streaming_recognize(streaming_config, requests)
                # 응답 처리
                if responses is None:
                    print("서버 응답이 없습니다. API 호출에 실패했습니다. ")
                else:
                    listen_before_click(responses, text_file)
            except Exception as e:
                print(f"음성 인식 중 오류가 발생했습니다: {e}")

if __name__ == '__main__':
    main()