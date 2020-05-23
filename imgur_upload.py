import json
import requests
from base64 import b64encode

with open('settings.json') as config:
    settings = json.load(config)

# Imgur authentication section
client_id = settings['imgur_client_id']

imgur_upload_endpoint = "https://api.imgur.com/3/upload"

headers = {"Authorization": "Client-ID " + client_id}

def imgur_upload(image):
    imgur_upload = requests.post(
        imgur_upload_endpoint,
        headers=headers,
        data={
            'image': b64encode(open('image.jpg', 'rb').read()),
            'type': 'base64'
        })
    data = json.loads(imgur_upload.text)['data']
    imgur_link = data['link']