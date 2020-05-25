import subprocess
from vrrdntPy import settings, title, desc_add, list_artist_links, imgur_link

# TODO: implement Google Cloud Console API for youtube uploading. Shouldn't rely on porjo/youtubeuploader.

default_tags = settings['default_tags']
base_description = settings['base_description']

# Upload the video using youtubeuploader. https://github.com/porjo/youtubeuploader
subprocess.call([
    'youtubeuploader_windows_amd64.exe', '-filename', 'output.mp4', '-privacy',
    'public', '-thumbnail', 'thumbnail.jpg', '-tags', default_tags, '-title', title,
    '-categoryId', '10', '-description', desc_add + '\n\nArtist links:\n' +
                                         list_artist_links + "\n\nImage link:\n" + imgur_link + "\n\n" + base_description
])