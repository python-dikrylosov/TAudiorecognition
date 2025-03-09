import speech_recognition as sr

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Настраиваюсь на микрофон...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Говорите...")
        audio = recognizer.listen(source)

    try:
        print("Распознавание...")
        text = recognizer.recognize_google(audio, language="ru-RU")
        print(f"Распознанный текст: {text}")
    except sr.UnknownValueError:
        print("Не удалось распознать речь")
    except sr.RequestError as e:
        print(f"Ошибка сервиса распознавания: {e}")

if __name__ == "__main__":
    print("Запуск распознавания. Нажмите Ctrl+C для выхода.")
    try:
        while True:
            recognize_speech_from_mic()
    except KeyboardInterrupt:
        print("\nПрограмма завершена")
