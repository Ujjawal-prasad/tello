import speech_recognition as sr
import pyaudio
import distutils

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone(device_index=3) as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Error with the service; {e}")

recognize_speech()