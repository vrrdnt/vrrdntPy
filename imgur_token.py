from os import curdir
from os.path import join as pjoin
import json
import webbrowser

from http.server import SimpleHTTPRequestHandler, HTTPServer


class StoreHandler(SimpleHTTPRequestHandler):
    store_path = pjoin(curdir, 'imgur_client_secrets.json')

    def do_GET(self):
        if self.path == '/imgur_client_secrets.json':
            with open(self.store_path) as fh:
                self.send_response(200)
                self.send_header('Content-type', 'text/json')
                self.end_headers()
                self.wfile.write(fh.read().encode())

    def do_POST(self):
        if self.path == '/imgur_client_secrets.json':
            length = self.headers['content-length']
            data = self.rfile.read(int(length))

            with open(self.store_path, 'w') as fh:
                fh.write(data.decode())

            self.send_response(200)


with open('settings.json') as config:
    settings = json.load(config)

# Imgur authentication section

imgur_id = settings['imgur_client_id']
imgur_secret = settings['imgur_client_secret']

imgur_auth_endpoint = "https://api.imgur.com/oauth2/authorize?client_id=" + imgur_id + "&response_type=token"

webbrowser.open(imgur_auth_endpoint, autoraise=True)

server = HTTPServer(('', 8080), StoreHandler)
server.serve_forever()
