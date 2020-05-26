import json
from oauthlib.oauth2 import MobileApplicationClient
from requests_oauthlib import OAuth2Session

with open('../settings.json') as config:
    settings = json.load(config)

# Imgur authentication section
client_id = settings['imgur_client_id']
auth_endpoint = settings['imgur_auth_url']
redirect_uri = settings['imgur_redirect_uri']

oauth = OAuth2Session(client=MobileApplicationClient(client_id=client_id))

uri, state = oauth.authorization_url(auth_endpoint)

authorization_response = oauth.get(url=uri)

print(authorization_response.url)
