""" Made by vrrdnt, created February 2020 """

import os
import sys
import subprocess
from io import BytesIO
import shutil
from base64 import b64encode
import json
import easygui
import youtube_dl
from PIL import Image, ImageOps
import requests
from pydub import AudioSegment, effects
from ytdl import ytdl
from render import render



with open('settings.json') as config:
    settings = json.load(config)

# Imgur authentication for image uploads
client_id = settings['client_id']
client_secret = settings['client_secret']
headers = {"Authorization": "Client-ID " + client_id}
api_url = "https://api.imgur.com/3/upload"

# Assignments
base_desc = settings['base_desc']

# Asks the user to supply a song URL or select an image file.
song_source = easygui.buttonbox(
    "Enter a URL or choose an audio file", choices=["File", "URL"])
if song_source == "File":
    song_file = easygui.fileopenbox(
        msg=None, title=None, filetypes=["*.mp3"], multiple=False)
    shutil.copy(song_file, 'audio.mp3')
elif song_source == "URL":
    song_url = [easygui.enterbox("Please enter a YouTube/SoundCloud URL:")]
    print("Downloading song from " + str(song_url))
    # Download a song from a valid source as defined by youtube-dl, and convert to audio.mp3.
    try:
        song_url
    except NameError:
        pass
    else:
        ytdl(song_url)

# Normalize audio to 93.5 dB?
AudioSegment.converter = "C:\\ffmpeg\\ffmpeg.exe"
AudioSegment.ffmpeg = "C:\\ffmpeg\\ffmpeg.exe"
AudioSegment.ffprobe ="C:\\ffmpeg\\ffprobe.exe"

sound = AudioSegment.from_file("audio.mp3", "mp3")
sound = effects.normalize(sound)
sound.export("audio.mp3", format="mp3")

# Asks the user to supply an image URL or select an image file,
# and uploads either to Imgur pre-jpg-conversion.
img_source = easygui.buttonbox(
    "Enter a URL or choose an image file", choices=["File", "URL"])
if img_source == "File":
    img_file = easygui.fileopenbox(
        msg=None, title=None, filetypes=[["*.jpg", "*.png"]], multiple=False)
    img = Image.open(img_file)
    img_to_jpg = img.convert('RGB')
    img_to_jpg = img.save('image.jpg')
    upload_img = requests.post(
        api_url,
        headers=headers,
        data={
            'image': b64encode(open('image.jpg', 'rb').read()),
            'type': 'base64'
        })
    data = json.loads(upload_img.text)['data']
    print(data)
    imgur_link = data['link']
    img = Image.open('image.jpg')
    resized_image = img.convert('RGB')
    size = (2560, 1440)
    resized_image = ImageOps.fit(resized_image, size, Image.ANTIALIAS)
    resized_image.save('image.jpg', format='JPEG', subsampling=0, quality=100)
elif img_source == "URL":
    imageURL = easygui.enterbox("Please enter a direct link to an image.")
    response = requests.get(imageURL)
    img = Image.open(BytesIO(response.content))
    img_to_jpg = img.convert('RGB')
    img_to_jpg = img.save('image.jpg')
    upload_img = requests.post(
        api_url,
        headers,
        data={
            'image': b64encode(open('image.jpg', 'rb').read()),
            'type': 'base64'
        })
    data = json.loads(upload_img.text)['data']
    imgur_link = data['link']
    img = Image.open('image.jpg')
    size = (2560, 1440)
    resized_image = ImageOps.fit(img_to_jpg, size, Image.ANTIALIAS)
    resized_image.save('image.jpg', format='JPEG', subsampling=0, quality=100)

# Asks for song title, artist, artist links, any additions to
# the description, and any additional tags.
title = easygui.enterbox("Please enter a song title:")
artist = easygui.enterbox("Please enter an artist name:")
artist_links = []
artist_links = easygui.multenterbox(
    "Please enter all of \
the artist's social links.", "Social Links",
    ["Instagram", "Twitter", "SoundCloud", "Spotify", "Bandcamp", "Website"])
desc_add = easygui.enterbox("Please enter any additions to \
the description you\'d like to add.")
tags_add = easygui.enterbox("Please enter a comma-seperated list of tags to add to the video.")

# Some formatting for the description.
while "" in artist_links:
    artist_links.remove("")
list_artist_links = "\n".join(artist_links)
title = (title + " | " + artist)
tags = settings['base_tags'] + "," + tags_add

# Tag overflow check
tagCheck = tags.replace(",", "")

if len(str(tagCheck)) > 500:
    print("WARNING! TAG OVERFLOW!")
    overflowValue = len(str(tagCheck))-500
    tags = tags[:-overflowValue]



# Run nexrender. https://github.com/inlife/nexrender
nexscript = "render.js" # script that nexrender uses to configure the After Effects project and aerender.
render(nexscript)

# Upload the video using youtubeuploader. https://github.com/porjo/youtubeuploader
subprocess.call([
    'youtubeuploader_windows_amd64.exe', '-filename', 'output.mp4', '-privacy',
    'public', '-thumbnail', 'thumbnail.jpg', '-tags', tags, '-title', title,
    '-categoryId', '10', '-description', desc_add + '\n\nArtist links:\n' +
    list_artist_links + "\n\nImage link:\n" + imgur_link + "\n\n" + base_desc
])

# Cleanup all downloaded, rendered and converted files.
root_dir = "./"
working_dir = os.listdir(root_dir)
for item in working_dir:
    if item.endswith(".jpg") or item.endswith(".mp4") or item.endswith(
            ".mp3") or item.endswith(".png"):
        os.remove(os.path.join(root_dir, item))
