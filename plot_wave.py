import wave
import matplotlib.pyplot as plt
import numpy as np

obj = wave.open("sample1.wav", "rb") 
sample_freq = obj.getframerate()
n_samples = obj.getnframes()
signal_wave = obj.readframes(n_samples)
n_channels = obj.getnchannels()
obj.close()

signal_array = np.frombuffer(signal_wave, dtype = np.int16)
times = np.linspace(0, (n_samples/sample_freq), num=n_samples)

l_channel = signal_array[0::2]
r_channel = signal_array[1::2]

plt.figure(figsize=(15,5))
plt.plot(times, l_channel)
plt.title("Audio Signal")
plt.ylabel("Signal Wave")
plt.xlabel("Time")
plt.xlim(0,(n_samples/sample_freq))
plt.show()
