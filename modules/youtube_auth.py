from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import json

with open('../settings.json') as config:
    settings = json.load(config)

# YouTube authentication section

yt_client_secrets_file = 'youtube_client_secrets.json'
yt_scopes = ['https://www.googleapis.com/auth/youtube']
yt_api_service_name = 'youtube'
yt_api_version = 'v3'


# Authorize the request and store authorization credentials.
def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(yt_client_secrets_file, yt_scopes)
    credentials = flow.run_console()
    return build(yt_api_service_name, yt_api_version, credentials=credentials)
