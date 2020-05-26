import subprocess
import json

with open('../settings.json') as config:
    settings = json.load(config)

# TODO: implement Google Cloud Console API for youtube uploading. Shouldn't rely on porjo/youtubeuploader.

# Asks for song title, artist, artist links, any additions to
# the description, and any additional tags.
title = easygui.enterbox("Please enter a song title:")
artist = easygui.enterbox("Please enter an artist name:")
artist_links = []
artist_links = easygui.multenterbox(
    "Please enter all of \
the artist's social links.", "Social Links",
    ["Instagram", "Twitter", "SoundCloud", "Spotify", "Bandcamp", "Website"])
desc_add = easygui.enterbox("Please enter any additions to \
the description you\'d like to add.")
tags_add = easygui.enterbox("Please enter a comma-seperated list of tags to add to the video.")

default_tags = settings['default_tags']
base_description = settings['base_description']

# Upload the video using youtubeuploader. https://github.com/porjo/youtubeuploader
subprocess.call([
    'youtubeuploader_windows_amd64.exe', '-filename', 'output.mp4', '-privacy',
    'public', '-thumbnail', 'thumbnail.jpg', '-tags', default_tags, '-title', title,
    '-categoryId', '10', '-description', desc_add + '\n\nArtist links:\n' +
                                         list_artist_links + "\n\nImage link:\n" + imgur_link + "\n\n" + base_description
])