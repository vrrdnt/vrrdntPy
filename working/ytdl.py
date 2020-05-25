import youtube_dl

# TODO: configurable naming of downloaded audio as well as audio codec \
#  and quality handled in settings.json. Error handling for unsupported \
#  codec on youtube-dl's part.
song_download = {
    'format': 'bestaudio/best',
    'outtmpl': 'audio.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}


def ytdl(song_url):
    with youtube_dl.YoutubeDL(song_download) as ytdl:
        ytdl.download(song_url)
