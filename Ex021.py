#####################################################
##Curso em Vídeo
##Aula 021 - Tocando um MP3
##https://youtu.be/9FiEji_fzvk
#####################################################

import pygame
import requests

file = b''
url_mp3 = 'https://anchor.fm/s/d28e5e4/podcast/play/9426145/https%3A%2F%2Fd3ctxlq1ktw2nl.cloudfront.net%2Fproduction%2F2019-11-31%2F41490349-44100-1-04d736db78cf2.mp3'

req = requests.get(url_mp3, stream=True)
for chunk in req.iter_content(chunk_size=40972):
    if chunk:
        file += chunk

pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
pygame.event.wait()

