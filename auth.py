from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import webbrowser
import http.server
import socketserver
import json


with open('settings.json') as config:
    settings = json.load(config)

# TODO: see https://requests-oauthlib.readthedocs.io/en/latest/oauth2_workflow.html#backend-application-flow

# YouTube authentication section

CLIENT_SECRETS_FILE = 'youtube_client_secrets.json'
SCOPES = ['https://www.googleapis.com/auth/youtube']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'


# Authorize the request and store authorization credentials.
#def get_authenticated_service():
#    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
#    credentials = flow.run_console()
#    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)


# Imgur authentication section

imgur_id = settings['imgur_client_id']
imgur_secret = settings['imgur_client_secret']

imgur_auth_endpoint = "https://api.imgur.com/oauth2/authorize?client_id=" + imgur_id + "&response_type=token"

webbrowser.open(imgur_auth_endpoint, autoraise=True)

# Webserver
PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()



