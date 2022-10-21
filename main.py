#Import dependencies
import sys
import glob
import requests
import sounddevice as sd 
from config import API_KEY
from scipy.io.wavfile import write

#Recording an audio
def record(duration, name_of_audio):
    fs = 44100
    print("-"*30,"Recording","-"*30)
    record = sd.rec(int(duration*fs), samplerate=fs, channels=1)
    sd.wait()
    write('{}.wav'.format(name_of_audio),fs, record)
    print("-"*30,"Recording finished","-"*30)
    return record

#Upload the recording.
def upload(audio_file):
    upload_url = 'https://api.assemblyai.com/v2/upload'
    filename = audio_file
    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data
    headers = {'authorization': API_KEY}
    response = requests.post(upload_url,
                            headers=headers,
                            data=read_file(filename))
    audio_url = response.json()['upload_url']

#Trancribing the file.
def transcribe():
    endpoint_url = "https://api.assemblyai.com/v2/transcript"
    json = { "audio_url": "https://bit.ly/3yxKEIY" }
    response = requests.post(endpoint_url, json=json, headers=headers)
    response_id = response.json()['id']