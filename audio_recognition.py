import wave
import pyaudio
import speech_recognition as sr

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
def communicate_to_drone ():
    try:
        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=FRAMES_PER_BUFFER,input_device_index=4)

        print("Listening.....")
        secounds = 5
        frames = []
        for i in range(0,int(RATE/FRAMES_PER_BUFFER*secounds)):
            data = stream.read(FRAMES_PER_BUFFER)
            frames.append(data)

        stream.stop_stream()
        stream.close()
        p.terminate()

        obj = wave.open("output3.wav","wb")
        obj.setnchannels(CHANNELS)
        obj.setsampwidth(p.get_sample_size(FORMAT))
        obj.setframerate(RATE)
        obj.writeframes(b"".join(frames))
        obj.close()

        recognizer = sr.Recognizer()

        
        with sr.AudioFile("output3.wav") as source:
            print("Recognizing.....\n")
            audio_data = recognizer.record(source)
            text = recognizer.recognize_whisper(audio_data)
        print("text from speech\n",text)
        return text

    

    except Exception as e:
        print(f"an unexpexted error occured{e}")
        return 'cannot recive text'

communicate_to_drone()
