import youtube_dl

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