import youtube_dl
import json
import os
import shutil
from tkinter import filedialog
from tkinter import *

with open('../settings.json') as config:
    settings = json.load(config)

window = Tk()
window.withdraw()
working_dir = "../working/"

local_audio_file = filedialog.askopenfilename(initialdir=os.path.expanduser('~'),
                                              title="Select audio file",
                                              filetypes=(("Audio Files", ".mp3 .wav .aac .m4a .opus"),
                                                         ("All Files", "*.*")))
window.destroy()
audio_extension = local_audio_file.rsplit('.', 1)[1]
shutil.move(local_audio_file, "../working/audio.%s" % audio_extension, copy_function=shutil.copy2)


# TODO: configurable audio codec
#  and quality handled in settings.json. Error handling for unsupported
#  codec on youtube-dl's part.
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
