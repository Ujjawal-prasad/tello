from pydub import AudioSegment
audio = AudioSegment.from_wav("Resorces/file_example_WAV_1MG.wav")
audio.export("new.mp3",format="mp3")
audio2 = AudioSegment.from_mp3("new.mp3")
print("done")
