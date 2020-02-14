from __future__ import unicode_literals
import os
import subprocess
import easygui
import requests
import youtube_dl
import ffmpeg
from PIL import Image, ImageOps
import requests
from io import BytesIO
import shutil

# I don't know how to exclude else:
x = 1

# Known information
baseDesc = "If you\'re an owner of any song/picture on this channel and want it removed, just message/email me and I\'ll do my best to delete it as soon as possible.\n\nHave a nice day! :)\n\nCopyright Disclaimer Under Section 107 of the Copyright Act 1976, allowance is made for \"fair use\" for purposes such as criticism, comment, news reporting, teaching, scholarship, and research. Fair use is a use permitted by copyright statute that might otherwise be infringing. Non-profit, educational or personal use tips the balance in favor of fair use."

# Is the song going to be downloaded from a URL, or supplied with a file?
songUrlOrFile = easygui.buttonbox ("Enter a URL or choose an audio file", choices = ["File","URL"])
if songUrlOrFile == "File":
    songFile = easygui.fileopenbox(msg=None, title=None, filetypes=["*.mp3"], multiple=False)
    shutil.copy(songFile, 'audio.mp3')
elif songUrlOrFile == "URL":
    songURL = []
    songURL.append(easygui.enterbox("Please enter a YouTube/SoundCloud URL:"))
else:
    x = x

# Is the image going to be downloaded from a URL, or supplied with a file?
imageUrlOrFile = easygui.buttonbox ("Enter a URL or choose an image file", choices = ["File","URL"])
if imageUrlOrFile == "File":
    imageFile = easygui.fileopenbox(msg=None, title=None, filetypes=[["*.jpg","*.png"]], multiple=False)
    img = Image.open(imageFile)
    rgb_img = img.convert('RGB')
    rgb_img.save('image.jpg')
elif imageUrlOrFile == "URL":
    imageURL = easygui.enterbox("Please enter a direct link to an image.")
    response = requests.get(imageURL)
    img = Image.open(BytesIO(response.content))
    rgb_img = img.convert('RGB')
    rgb_img.save('image.jpg')
else:
    x = x

# Asks for the song title and artist. Also requests any social links.
songTitle = easygui.enterbox("Please enter a song title:")
songArtist = easygui.enterbox("Please enter an artist name:")
artistLinks = []
artistLinks = easygui.multenterbox("Please enter all of the artist's social links.", "Social Links", ["Instagram","Twitter","SoundCloud","Spotify","Bandcamp","Website"])
while("" in artistLinks) : 
    artistLinks.remove("") 
listArtistSocials = "\n".join(artistLinks)
descriptionAdd = easygui.enterbox("Please enter any additions to the description you\'d like to add.")
addedTags = easygui.enterbox("Please enter a comma-seperated list of tags to add to the video.")

videoTitle = (songTitle + " | " + songArtist)
listArtistSocials = "\n".join(artistLinks)
videoTags = "lofi,hiphop,mix,mixtape,beat,vrrdntupload,beats,vibe,chill,relax,study,homework,loop," + addedTags

print(listArtistSocials)
# Generate thumbnail
shutil.copy('image.jpg', 'thumbnail.jpg')
original_image = Image.open("thumbnail.jpg")
size = (1920, 1080)
fit_and_resized_image = ImageOps.fit(original_image, size, Image.ANTIALIAS)
fit_and_resized_image.save('thumbnail.jpg')

# Download video, convert to mp3 if URL is given
try:
    songURL
    urlGiven = 1
except NameError:
    urlGiven = 0

if urlGiven == 1:
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'audio.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
            }],
        }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(songURL)
else:
    x = x
    
# Run nexrender
subprocess.call(['node', 'render.js'])

# Upload the video
subprocess.call(['upload', '-filename', 'output.mp4', '-privacy', 'public', '-thumbnail', 'thumbnail.jpg', '-tags', videoTags, '-title', videoTitle, '-categoryId', '10', '-description', descriptionAdd + '\n\nArtist links:\n' + listArtistSocials + "\n\n" + baseDesc])

# Cleanup!
dir_name = "./"
workingDir = os.listdir(dir_name)

for item in workingDir:
    if item.endswith(".jpg") or item.endswith(".mp4") or item.endswith(".mp3"):
        os.remove(os.path.join(dir_name, item))
    else:
        x = x
