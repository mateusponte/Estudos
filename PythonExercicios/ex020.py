from pygame import mixer
mixer.init()
mixer.music.load('cjbr.mp3')
mixer.music.play()
input('agora você escuta?')

#outra forma
#import pygame

# Inicializando o mixer PyGame
#pygame.mixer.init()

# Iniciando o Pygame
#pygame.init()

#pygame.mixer.music.load('ex021.mp3')
#pygame.mixer.music.play(loops=0, start=0.0)
#pygame.event.wait()