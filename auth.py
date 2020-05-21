from main import settings

# TODO: Better Imgur/GCC authentication handling. Both services authenticated by and in this module.
# Imgur authentication for image uploads

client_id = settings['client_id']
client_secret = settings['client_secret']
headers = {"Authorization": "Client-ID " + client_id}
api_url = "https://api.imgur.com/3/upload"
