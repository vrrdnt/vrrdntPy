import json
import youtube_dl

with open('settings.json') as config:
    settings = json.load(config)

song_download = {
    'format': 'bestaudio/best',
    'outtmpl': 'audio.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': settings['audio_format'],
        'preferredquality': settings['audio_quality'],
    }],
}


def ytdl(song_url):
    with youtube_dl.YoutubeDL(song_download) as ytdl:
        ytdl.download(song_url)
