import moviepy.editor as mpy
from math import pi

test_image_source = "./image.jpg"
test_audio_source = "./changes.mp3"

test_image = mpy.ImageClip(test_image_source).set_position('center', 'center')
test_audio = mpy.AudioFileClip(test_audio_source)

video_size = (1920, 1080)


# TODO: use PIL to fit image to dimensions set in settings. mpy can't do it.
video = mpy.CompositeVideoClip(
    [
        test_image
    ],
    size=video_size).set_duration(1).set_audio(test_audio)

video.write_videofile('video_with_python.mp4', fps=24)
