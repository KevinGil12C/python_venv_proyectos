import eel
import sys
import os

# Importamos la libreria para descargar
from pytube import YouTube
from moviepy.editor import *

# Rutas para las carpetas de música y videos
parent_dir = os.path.join(os.path.expanduser('~'), 'Music')
parent_dirV = os.path.join(os.path.expanduser('~'), 'Videos')

@eel.expose 
def DescargaMP3(enlace):
    def progress_callback(stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = (bytes_downloaded / total_size) * 100
        print(f"Progreso de descarga: {percentage:.2f}%")

    video = YouTube(enlace, on_progress_callback=progress_callback)
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