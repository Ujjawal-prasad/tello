import wave
import numpy as np
import matplotlib.pyplot as plt

obj = wave.open("Resorces/file_example_WAV_10MG.wav","rb")


sample_frequency = obj.getframerate()
no_of_samples = obj.getnframes()*2

signal_wave = obj.readframes(-1)

obj.close()

t_audio = no_of_samples/sample_frequency
print(t_audio)

signal_array = np.frombuffer(signal_wave,dtype=np.int16)

times = np.linspace(0,t_audio,num=no_of_samples)

plt.figure(figsize=(15,6))
plt.plot(times,signal_array)
plt.title("Audio Signal")
plt.ylabel("Signal")
plt.xlabel("Time")
plt.xlim(0,t_audio)
plt.show()
