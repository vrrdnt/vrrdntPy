import moviepy.editor as mpy
from mutagen.mp3 import MP3
from image_gen import fit_image
import json

with open('../settings.json') as config:
    settings = json.load(config)

test_image_source = "../working/image.jpg"
test_audio_source = "../working/audio.mp3"

fit_image(test_image_source)
final_image = "../working/modified_image.jpg"

mutagen_load = MP3(test_audio_source)

test_image = mpy.ImageClip(final_image).set_position('center', 'center')
test_audio = mpy.AudioFileClip(test_audio_source)

video_size = (settings['video_width'], settings['video_height'])

video = mpy.CompositeVideoClip(
    [
        test_image
    ],
    size=video_size).set_duration(mutagen_load.info.length).set_audio(test_audio)

video.write_videofile('../working/video.mp4', fps=24)
