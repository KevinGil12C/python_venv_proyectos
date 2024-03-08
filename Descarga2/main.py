import eel
import sys

#Cambiamos la run_path
#sys.path.append('')
#Importamos la libreria para descargar
from pytube import YouTube
parent_dir = 'C:/Users/Kevscl/Music'
parent_dirV = 'C:/Users/Kevscl/Videos'
import os
from moviepy.editor import *

@eel.expose 
def DescargaMP3(enlace):
    video = YouTube(enlace)
    stream = video.streams.get_audio_only().download(parent_dir)
    audioclip = AudioFileClip(stream)
    audioclip.write_audiofile(audioclip.filename.replace('.mp4', '.mp3'))
    os.remove(audioclip.filename)
    mensaje = "Descargado"
    return mensaje

@eel.expose
def DescargaMP4(url):
    video = YouTube(url)
    descarga = video.streams.get_highest_resolution().download(parent_dirV)
    mensaje = "Descargado"
    return mensaje

eel.init("")
eel.start("index.html", mode="brave")