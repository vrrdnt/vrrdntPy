""" Made by vrrdnt, created February 2020 """

from __future__ import unicode_literals
import os
import subprocess
from io import BytesIO
import shutil
from base64 import b64encode
import json
import easygui
import youtube_dl
from PIL import Image, ImageOps
import requests

with open('settings.json') as s
    settings = json.load(s)

# Imgur authentication for image uploads
CLIENT_ID = settings['ClientID']
CLIENT_SECRET = settings['ClientSecret']
headers = {"Authorization": "Client-ID " + CLIENT_ID}
imgUploadEndpoint = "https://api.imgur.com/3/upload"

# Assignments
baseDesc = settings['basedesc']

# Asks the user to supply a song URL or select an image file.
songSource = easygui.buttonbox("Enter a URL or choose an audio file", choices=["File", "URL"])
if songSource == "File":
    songFile = easygui.fileopenbox(msg=None, title=None, filetypes=["*.mp3"], multiple=False)
    shutil.copy(songFile, 'audio.mp3')
elif songSource == "URL":
    songURL = [easygui.enterbox("Please enter a YouTube/SoundCloud URL:")]

# Asks the user to supply an image URL or select an image file,
# and uploads either to Imgur pre-jpg-conversion.
imgSource = easygui.buttonbox("Enter a URL or choose an image file", choices=["File", "URL"])
if imgSource == "File":
    imgFile = easygui.fileopenbox(msg=None, title=None,\
    filetypes=[["*.jpg", "*.png"]], multiple=False)
    img = Image.open(imgFile)
    imgToJPG = img.convert('RGB')
    imgToJPG = img.save('image.jpg')
    uploadImg = requests.post(
        imgUploadEndpoint,
        headers=headers,
        data={
            'image': b64encode(open('image.jpg', 'rb').read()),
            'type': 'base64'
        }
    )
    data = json.loads(uploadImg.text)['data']
    print(data)
    imgurLink = data['link']
    img = Image.open('image.jpg')
    resizedImage = img.convert('RGB')
    size = (2560, 1440)
    resizedImage = ImageOps.fit(resizedImage, size, Image.ANTIALIAS)
    resizedImage.save('image.jpg', format='JPEG', subsampling=0, quality=100)
elif imageSource == "URL":
    imageURL = easygui.enterbox("Please enter a direct link to an image.")
    response = requests.get(imageURL)
    img = Image.open(BytesIO(response.content))
    imgToJPG = img.convert('RGB')
    imgToJPG= img.save('image.jpg')
    uploadImg = requests.post(
        imgUploadEndpoint,
        headers,
        data={
            'image': b64encode(open('image.jpg', 'rb').read()),
            'type': 'base64'
        }
    )
    data = json.loads(uploadImg.text)['data']
    imgurLink = data['link']
    img = Image.open('image.jpg')
    size = (2560, 1440)
    resizedImg = ImageOps.fit(imgToJpg, size, Image.ANTIALIAS)
    resizedImg.save('image.jpg', format='JPEG', subsampling=0, quality=100)

# Asks for song title, artist, artist links, any additions to
# the description, and any additional tags.
title = easygui.enterbox("Please enter a song title:")
artist = easygui.enterbox("Please enter an artist name:")
artistLinks = []
artistLinks = easygui.multenterbox("Please enter all of \
the artist's social links.", "Social Links", ["Instagram",\
"Twitter", "SoundCloud", "Spotify", "Bandcamp", "Website"])
descAdds = easygui.enterbox("Please enter any additions to \
the description you\'d like to add.")
tagAdds = "," + easygui.enterbox("Please enter a comma-seperated list of tags to add to the video.")

# Some formatting for the description.
while "" in artistLinks:
    artistLinks.remove("")
listArtistLinks = "\n".join(artistLinks)
title = (title + " | " + artist)
tags = settings['basetags'] + tagAdds

# Generate thumbnail.jpg.
shutil.copy('image.jpg', 'thumbnail.jpg')
thumbnail = Image.open("thumbnail.jpg")
size = (1920, 1080)
thumbnailGen = ImageOps.fit(thumbnail, size, Image.ANTIALIAS)
thumbnailGen.save('thumbnail.jpg', format='JPEG', optimized=True,subsampling=0, quality=85)

# Download a song from a valid source as defined by youtube-dl, and convert to audio.mp3.
try:
    songURL
except NameError:
    pass
else:
    songDownload = {
        'format': 'bestaudio/best',
        'outtmpl': 'audio.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
            }],
        }
    with youtube_dl.YoutubeDL(songDownload) as ydl:
        ydl.download(songURL)

# Run nexrender. https://github.com/inlife/nexrender
subprocess.call(['node', 'render.js'])

# Upload the video using youtubeuploader. https://github.com/porjo/youtubeuploader
subprocess.call(['youtubeuploader_windows_amd64.exe', '-filename', 'output.mp4', '-privacy', \
    'public', '-thumbnail', 'thumbnail.jpg', '-tags', tags, \
    '-title', title, '-categoryId', '10', '-description', \
    descAdds + '\n\nArtist links:\n' + listArtistLinks + \
    "\n\nImage link:\n" + imgurLink + "\n\n" + baseDesc])

# Cleanup all downloaded, rendered and converted files.
rootDir = "./"
workingDir = os.listdir(rootDir)
for item in workingDir:
    if item.endswith(".jpg") or item.endswith(".mp4") \
    or item.endswith(".mp3") or item.endswith(".png"):
        os.remove(os.path.join(rootDir, item))
