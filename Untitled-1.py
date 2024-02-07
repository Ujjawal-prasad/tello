import whisper

model = whisper.load_model("base")
result = model.transcribe(r"Resorces\file_example_WAV_10MG.wav")
print(result["text"])