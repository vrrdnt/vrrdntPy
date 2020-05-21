from pydub import AudioSegment, effects

# TODO: configurable audio normalization in dB (ideally) in settings.json, as well as toggling of this module.
# Normalize audio to 93.5 dB?
AudioSegment.converter = "C:\\ffmpeg\\ffmpeg.exe"
AudioSegment.ffmpeg = "C:\\ffmpeg\\ffmpeg.exe"
AudioSegment.ffprobe = "C:\\ffmpeg\\ffprobe.exe"

sound = AudioSegment.from_file("audio.mp3", "mp3")
sound = effects.normalize(sound)
sound.export("audio.mp3", format="mp3")