import speech_recognition
import pyttsx3

def recognize_and_speak():
    recognizer = speech_recognition.Recognizer()
    engine = pyttsx3.init()

    while True:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio)
                text = text.lower()

                print(f'Recording: {text}')

                # Speak the recognized text
                engine.say(text)
                engine.runAndWait()

        except speech_recognition.UnknownValueError:
            pass
        except speech_recognition.RequestError as e:
            print(f"Speech recognition request failed: {e}")

recognize_and_speak()
