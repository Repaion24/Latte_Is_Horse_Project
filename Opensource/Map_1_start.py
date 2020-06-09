import pygame
import map

def Map_1_starting(screen) :
    map1 = map.map(screen)
    map1.set([0, 60], [1280, 600])
    map1.draw()





    pygame.display.flip()