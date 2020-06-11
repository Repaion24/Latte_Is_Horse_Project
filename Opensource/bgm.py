import pygame, sys
pygame.init()
pygame.mixer.init()


pygame.mixer.music.load("sound/.wav")
pygame.mixer.music.set_volume(1) # 1 ~ 0.1


pygame.mixer.music.play()


pygame.mixer.Sound("sound/.wav")

