import youtube_dl
import json
import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import font as tkfont

with open('../settings.json') as config:
    settings = json.load(config)

working_dir = "../working/"

download_options = {
    'format': 'bestaudio/best',
    'outtmpl': 'audio.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}


def download(song_url):
    with youtube_dl.YoutubeDL(download_options) as ytdl:
        ytdl.download(song_url)


def local_load():
    local_audio_file = filedialog.askopenfilename(initialdir=os.path.expanduser('~'),
                                                  title="Select audio file",
                                                  filetypes=(("Audio Files", ".mp3 .wav .aac .m4a .opus"),
                                                             ("All Files", "*.*")))
    window.destroy()
    audio_extension = local_audio_file.rsplit('.', 1)[1]
    shutil.move(local_audio_file, "../working/audio.%s" % audio_extension, copy_function=shutil.copy2)


def download_from_source():
    url_enter = tk.Tk()
    tk.Label(url_enter,
             text="URL:").grid(row=0)

    url_entry = tk.Entry(url_enter)

    url_entry.grid(row=0, column=1)

    tk.Button(url_enter,
              text='Enter',
              command=download(url_entry.get())).grid(row=2,
                                                      column=0,
                                                      pady=(4, 4))
    # TODO: download does nothing. fix
    tk.mainloop()


window = tk.Tk()
text_size_14 = tkfont.Font(size=14)

body_text = tk.Label(window, text="Download audio or provide from local source?")
frame_1 = tk.Frame(window)
download_button = tk.Button(frame_1, text="Download", command=download_from_source)
download_button.config(width="10")
local_button = tk.Button(frame_1, text="Local", command=local_load)
local_button.config(width="10")
download_button['font'] = text_size_14
local_button['font'] = text_size_14

body_text.grid(row=0, column=1)
frame_1.grid(row=1, column=1, padx=(10, 10), pady=(10, 10), sticky="nesw")

download_button.pack(side="left")
local_button.pack(side="right")

window.mainloop()
# window.withdraw()
