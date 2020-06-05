# vrrdntPy

Hey there! This is a script I authored that I use to render videos and upload them to [vrrdnt](https://youtube.com/vrrdnt). I wrote it over the span of about a week. It's my first self-authored script. I do know, however, that it could use some massive improvement. If you feel like contributing it please don't hesitate to make a pull request.

## Compatibility  

This script is currently only compatible with Windows systems.  
Requires Python 3.8 (?)

## Requirements

Please run `pip install -r requirements.txt`
 
This script heavily relies on [porjo/youtubeuploader](https://github.com/porjo/youtubeuploader) and [inlife/nexrender](https://github.com/inlife/nexrender) for uploading and rendering, respectively. You'll probably want to install nexrender using [Node.js](https://nodejs.org), and download the [latest Windows build](https://github.com/porjo/youtubeuploader/releases) of youtubeuploader, and place the latter in the same directory as the rest of this project.  
  
NOTE: This is subject to change. Both youtubeuploader and nexrender can in some way be integrated natively into this project, depending on what you use After Effects for. This script will change as I change the nature of my videos as well as my workflow.

## Files and folders

You'll need a working Adobe After Effects project file, either named Video.aep or something else that you specify in render.js.

## TODO

Normalize audio.mp3 to 93.5 dB (using pyDub?)
