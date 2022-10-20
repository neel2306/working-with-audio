import sounddevice as sd 
from scipy.io.wavfile import write

fs = 44100
seconds = 5

print("Recording......")
record = sd.rec(int(seconds*fs), samplerate=fs, channels=2)
sd.wait()
write('recording.wav',fs, record)