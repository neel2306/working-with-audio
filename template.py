import sys
import requests
from config import API_KEY
#Record the file

#Upload the file
upload_url = 'https://api.assemblyai.com/v2/upload'
filename = 'sample1.wav'
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
#audio_url = response.json()['upload_url']
#Transcribe the file
endpoint_url = "https://api.assemblyai.com/v2/transcript"
json = { "audio_url": "https://bit.ly/3yxKEIY" }
response = requests.post(endpoint_url, json=json, headers=headers)
response_id = response.json()['id']
#Checking if transcription is ready or not
polling_url = endpoint_url + '/' + response_id
polling_result = requests.get(polling_url, headers=headers)
print(polling_result.json())
#Save transcript