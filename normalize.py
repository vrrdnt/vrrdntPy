from pydub import AudioSegment, effects
from ffmpeg import video
import json

with open('settings.json') as config:
    settings = json.load(config)

# TODO: configurable audio normalization in dB (ideally, dBFS if I have to) \
#  in settings.json, as well as toggling of this module.


# Set audio renderers for pydub
AudioSegment.converter = video
AudioSegment.ffmpeg = video

pre_normalized_file = AudioSegment.from_file(("%s" % settings['audio_file_name'] + "." +
                                              "%s" % settings['audio_format']),
                                              "%s" % settings['audio_format'])

normalized_file = effects.normalize(pre_normalized_file)

normalized_file.export(("%s" % settings['audio_file_name'] + "." + "%s" % settings['audio_format']), format=settings['audio_format'])