import os
import shutil
import youtube_dl
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import font as tkfont
import json

with open('../settings.json') as config:
    settings = json.load(config)


class MainResourceGather(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("vrrdntPy")
        self.title_font = tkfont.Font(family='Segoe', size=18, weight="bold")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainMenu, AudioSource, ImageSource, AudioURLEntry, VideoDetails):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


# TODO: Constantly resize to fit the TOP FRAME only
class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="vrrdntPy", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        audio_source_button = tk.Button(self, text="Select Audio Source",
                                        command=lambda: controller.show_frame("AudioSource"))
        image_source_button = tk.Button(self, text="Select Image Source",
                                        command=lambda: controller.show_frame("ImageSource"))
        video_details_button = tk.Button(self, text="Enter video details",
                                         command=lambda: controller.show_frame("VideoDetails"))

        exit_button = tk.Button(self, text="Quit", command=controller.destroy)
        audio_source_button.pack()
        image_source_button.pack()
        video_details_button.pack()
        exit_button.pack()


def local_audio_source():
    local_audio_file = tk.filedialog.askopenfilename(initialdir=os.path.expanduser('~'),
                                                     title="Select audio file",
                                                     filetypes=(("Audio Files", ".mp3 .wav .aac .m4a .opus"),
                                                                ("All Files", "*.*")))
    audio_extension = local_audio_file.rsplit('.', 1)[1]
    shutil.move(local_audio_file, "../working/audio.%s" % audio_extension, copy_function=shutil.copy2)


def remote_audio_download(url):
    download_options = {
        'format': 'bestaudio/best',
        'outtmpl': '../working/audio.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': settings['audio_format'],
            'preferredquality': settings['audio_quality'],
        }],
    }
    with youtube_dl.YoutubeDL(download_options) as ytdl:
        ytdl.download([url])


class AudioSource(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Select the audio source", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        local_source = tk.Button(self, text="Local Source",
                                 command=local_audio_source)
        remote_source = tk.Button(self, text="Remote Source",
                                  command=lambda: controller.show_frame("AudioURLEntry"))
        back_button = tk.Button(self, text="Go to the main menu",
                                command=lambda: controller.show_frame("MainMenu"))
        local_source.pack()
        remote_source.pack()
        back_button.pack()


class AudioURLEntry(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Enter audio URL", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        back_button = tk.Button(self, text="Go to the main menu",
                                command=lambda: controller.show_frame("MainMenu"))
        local_source = tk.Entry(self, textvariable=tk.StringVar())
        enter_button = tk.Button(self, text="Enter",
                                 command=lambda: remote_audio_download(local_source.get()))
        back_button.pack()
        local_source.pack()
        enter_button.pack()


class ImageSource(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Select the image source", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        back_button = tk.Button(self, text="Go to the main menu",
                                command=lambda: controller.show_frame("MainMenu"))
        back_button.pack()


# TODO: Add video detail entry boxes such as title, description, additional tags, etc.
class VideoDetails(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Enter Video Details", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        video_title = tk.Entry(self, textvariable=tk.StringVar())
        video_description = tk.scrolledtext.ScrolledText(self, width=20, height=5)
        enter_button = tk.Button(self, text="Enter")
        back_button = tk.Button(self, text="Go to the main menu",
                                command=lambda: controller.show_frame("MainMenu"))
        video_title.pack()
        video_description.pack()
        enter_button.pack()
        back_button.pack()


if __name__ == "__main__":
    app = MainResourceGather()
    app.mainloop()
