import youtube_dl
import json
import os
import shutil
from tkinter import filedialog
from tkinter import *

home = os.path.expanduser('~')

window = Tk()
window.withdraw()

local_audio_file = filedialog.askopenfilename(initialdir = home,title = "Select audio file",filetypes = (("Audio Files",".mp3 .wav .aac .m4a .opus"),("All Files","*.*")))
shutil.copy2(local_audio_file, "../working/")
window.destroy()
os.rename(local_audio_file,"audio")

# TODO: preserve extension in os.rename


# with open('../settings.json') as config:
#     settings = json.load(config)



# # Asks the user to supply a song URL or select an image file.
# song_source = tkinter.(mode="r", filetypes="*", initialdir=home)(
#     "Enter a URL or choose an audio file", choices=["File", "URL"])
# if song_source == "File":
#     song_file = easygui.fileopenbox(
#         msg='', title='', filetypes=["*.mp3"], multiple=False)
#     shutil.copy(song_file, 'audio.mp3')
# elif song_source == "URL":
#     song_url = [easygui.enterbox("Please enter a YouTube/SoundCloud URL:")]
#     print("Downloading song from " + str(song_url))
#     # Download a song from a valid source as defined by youtube-dl, and convert to audio.mp3.
#     try:
#         song_url
#     except NameError:
#         pass
#     else:
#         ytdl(song_url)
#
#
# # TODO: configurable naming of downloaded audio as well as audio codec \
# #  and quality handled in settings.json. Error handling for unsupported \
# #  codec on youtube-dl's part.
# song_download = {
#     'format': 'bestaudio/best',
#     'outtmpl': 'audio.%(ext)s',
#     'postprocessors': [{
#         'key': 'FFmpegExtractAudio',
#         'preferredcodec': 'mp3',
#         'preferredquality': '320',
#     }],
# }
#
#
# def ytdl(song_url):
#     with youtube_dl.YoutubeDL(song_download) as ytdl:
#         ytdl.download(song_url)
