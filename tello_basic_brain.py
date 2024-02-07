import pyttsx3
import speech_recognition as sr
import time

def speak (text):
    engine = pyttsx3.init()
    id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
    engine.setProperty('voice',id)
    engine.setProperty('rate',150)
    engine.say(text=text)
    engine.runAndWait()

def recon ():
    hear = sr.Recognizer()
    with sr.Microphone(device_index=4) as source:
        print("Listening....")
        hear.pause_threshold = 1
        audio = hear.listen(source,0,8)

    try:
        print("Recognizing....")
        query = hear.recognize_google(audio,language="en")
        return query.lower()

    except:
        return""
    
def excecute (query):
    Query = str(query).lower()
    if "hello " in query:
        speak("hi sir")
    elif "bye" in query:
        speak("nice to meet you")

while True:
    Query = recon()
    excecute(Query)