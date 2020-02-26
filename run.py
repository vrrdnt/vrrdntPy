""" Made by vrrdnt, February 2020 """

from __future__ import unicode_literals
import os
import subprocess
from io import BytesIO
import shutil
import webbrowser
import easygui
import youtube_dl
from PIL import Image, ImageOps
import requests
import pyimgur

# Stuff for pyimgur
CLIENT_ID = "CLIENT_ID"
CLIENT_SECRET = "CLIENT_SECRET"
IM = pyimgur.Imgur(CLIENT_ID, CLIENT_SECRET)
AUTH_URL = IM.authorization_url('pin')
webbrowser.open(AUTH_URL)
PIN = easygui.enterbox("Please enter the pin provided in your browser.")
IM.exchange_pin(PIN)

# This information automatically goes into the description.
BASEDESC = "If you\'re an owner of any song/picture on this channel \
            and want it removed, just message/email me and I\'ll do \
            my best to delete it as soon as possible.\n\nHave a nice \
            day! :)\n\nCopyright Disclaimer Under Section 107 of the \
            Copyright Act 1976, allowance is made for \"fair use\" \
            for purposes such as criticism, comment, news reporting, \
            teaching, scholarship, and research. Fair use is a use \
            permitted by copyright statute that might otherwise be \
            infringing. Non-profit, educational or personal use tips \
            the balance in favor of fair use."

# Asks the user to supply a song URL or select an image file.
SONGURLORFILE = easygui.buttonbox("Enter a URL or choose an audio file", choices=["File", "URL"])
if SONGURLORFILE == "File":
    SONGFILE = easygui.fileopenbox(msg=None, title=None, filetypes=["*.mp3"], multiple=False)
    shutil.copy(SONGFILE, 'audio.mp3')
elif SONGURLORFILE == "URL":
    SONGURL = []
    SONGURL.append(easygui.enterbox("Please enter a YouTube/SoundCloud URL:"))

# Asks the user to supply an image URL or select an image file,
# and uploads either to Imgur pre-jpg-conversion.
IMAGEURLORFILE = easygui.buttonbox("Enter a URL or choose an image file", choices=["File", "URL"])
if IMAGEURLORFILE == "File":
    IMAGEFILE = easygui.fileopenbox(msg=None, title=None,\
    filetypes=[["*.jpg", "*.png"]], multiple=False)
    UPLOADED_IMAGE = IM.upload_image(IMAGEFILE)
    IMAGELINK = UPLOADED_IMAGE.link
    IMG = Image.open(IMAGEFILE)
    RGB_IMG = IMG.convert('RGB')
    RGB_IMG.save('image.jpg')
elif IMAGEURLORFILE == "URL":
    IMAGEURL = easygui.enterbox("Please enter a direct link to an image.")
    RESPONSE = requests.get(IMAGEURL)
    IMG = Image.open(BytesIO(RESPONSE.content))
    RGB_IMG = IMG.convert('RGB')
    RGB_IMG.save('image.jpg')
    UPLOADED_IMAGE = IM.upload_image('image.jpg')
    IMAGELINK = UPLOADED_IMAGE.link

# Asks for song title, artist, artist links, any additions to
# the description, and any additional tags.
SONGTITLE = easygui.enterbox("Please enter a song title:")
SONGARTIST = easygui.enterbox("Please enter an artist name:")
ARTISTLINKS = []
ARTISTLINKS = easygui.multenterbox("Please enter all of \
    the artist's social links.", "Social Links", ["Instagram", \
    "Twitter", "SoundCloud", "Spotify", "Bandcamp", "Website"])
DESCRIPTIONADD = easygui.enterbox("Please enter any additions to \
    the description you\'d like to add.")
ADDEDTAGS = easygui.enterbox("Please enter a comma-seperated list of tags to add to the video.")

# Some formatting for the description.
while "" in ARTISTLINKS:
    ARTISTLINKS.remove("")
LISTARTISTSOCIALS = "\n".join(ARTISTLINKS)
VIDEOTITLE = (SONGTITLE + " | " + SONGARTIST)
LISTARTISTSOCIALS = "\n".join(ARTISTLINKS)
VIDEOTAGS = "lofi,hiphop,mix,mixtape,beat,vrrdntupload,beats,vibe,\
    chill,relax,study,homework,loop," + ADDEDTAGS

# Generate thumbnail.jpg.
shutil.copy('image.jpg', 'thumbnail.jpg')
ORIGINAL_IMAGE = Image.open("thumbnail.jpg")
ORIGINAL_IMAGE.save('thumbnail.jpg')
ORIGINAL_IMAGE = Image.open("thumbnail.jpg")
SIZE = (1920, 1080)
RESIZEDIMAGED = ImageOps.fit(ORIGINAL_IMAGE, SIZE, Image.ANTIALIAS)
RESIZEDIMAGED.save('thumbnail.jpg')

# Download a song from a valid source as defined by youtube-dl, and convert to audio.mp3.
try:
    SONGURL
except NameError:
    pass
else:
    YTDL_OPTS = {
        'format': 'bestaudio/best',
        'outtmpl': 'audio.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
            }],
        }
    with youtube_dl.YoutubeDL(YTDL_OPTS) as ydl:
        ydl.download(SONGURL)

# Run nexrender. https://github.com/inlife/nexrender
subprocess.call(['node', 'render.js'])

# Upload the video using youtubeuploader. https://github.com/porjo/youtubeuploader
subprocess.call(['youtubeuploader_windows_amd64.exe', '-filename', 'output.mp4', '-privacy', \
    'public', '-thumbnail', 'thumbnail.jpg', '-tags', VIDEOTAGS, \
    '-title', VIDEOTITLE, '-categoryId', '10', '-description', \
    DESCRIPTIONADD + '\n\nArtist links:\n' + LISTARTISTSOCIALS + \
    "\n\nImage link:\n" + IMAGELINK + "\n\n" + BASEDESC])

# Cleanup all downloaded, rendered and converted files.
DIR_NAME = "./"
WORKINGDIR = os.listdir(DIR_NAME)
for item in WORKINGDIR:
    if item.endswith(".jpg") or item.endswith(".mp4") or item.endswith(".mp3"):
        os.remove(os.path.join(DIR_NAME, item))
