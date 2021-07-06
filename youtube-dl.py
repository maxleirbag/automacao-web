#import youtube_dl
#youtube-dl -f ("(bestvideo+bestaudio/best)[protocol^=https://www.youtube.com/watch?v=2UM8Z7zckS4]")

from __future__ import unicode_literals
import youtube_dl

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://youtu.be/4z9ADmZhqko'])



# https://www.youtube.com/watch?v=Q3InFEwJVr0 2.5
