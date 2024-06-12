import requests
import time 
import os

#base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#Endpoints
UPLOAD_ENDPOINT = "https://api.assemblyai.com/v2/upload"
TRANSCRIPTION_ENDPOINT = "https://api.assemblyai.com/v2/transcript"

#Variables
api_key = "ecba2c4970eb4daba7e1deb8c5e6d150"
headers = {"authorization": api_key, "content-type": "application/json"}

#Generator to read an audio file
def read_file(filename):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(5242880)
            if not data:
                break
            yield data

#Upload
upload_response = requests.post(UPLOAD_ENDPOINT, headers=headers, data=read_file(BASE_DIR + './Owl City - Fireflies.mp3'))
audio_url = upload_response.json()["upload_url"]

#request
transcript_request = {'audio_url': audio_url}
transcript_response = requests.post(TRANSCRIPTION_ENDPOINT, json=transcript_request, headers=headers)
_id = transcript_response.json()["id"]

#wait
while True:
    #get updated
    polling_response = requests.get(TRANSCRIPTION_ENDPOINT + "/" + _id, headers=headers)

    #if the transcription
    if polling_response.json()['status'] == 'completed':
        with open(f'{_id}.txt', 'w') as f:
            f.write(polling_response.json()['text'])
        print('Transcript saved to', _id, '.txt')
        break
    #if failed
    elif polling_response.json()['status'] == 'error':
        raise Exception("Transcription failed. Make sure")
    #otherwise
    else:
        print("processing...")
        time.sleep(5)
