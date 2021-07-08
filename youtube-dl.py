from __future__ import unicode_literals
import youtube_dl

link = input("Insira o link do vídeo do Youtube que deseja baixar: ")

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
