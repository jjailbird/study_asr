import whisper
model = whisper.load_model("medium")


def recognize_voice(file_path, language):
    '''
    :param file_path: 사운드 파일의 절대 경로
    :param language: 파일의 언어, "en" : 영어, "ko" : 한국어, "jp" : 일본어 ...
    :return: 실패시 False, 아니면 변환 된 텍스트
    '''
    try:  # 8줄 내에 깔끔 한 예외 처리까지
        result = model.transcribe(file_path, language=language)
        return result['text']
    except Exception:
        return False


result = recognize_voice('./sample.mp3', 'ko')

print(result)
