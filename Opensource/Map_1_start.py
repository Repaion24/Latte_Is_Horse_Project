import pygame
import map
import time


def Map_1_starting(screen) :
    back_ground = pygame.image.load("image/virus/map2.png")
    interface = pygame.image.load("image/virus/interface.png")
    map1 = map.map(screen)
    map1.ch = [[120,60],[120,420],[300,420],[300,180],[540,180],[540,420],[780,420],[780,720]]
    map1.set([0, 60], [1280, 600])




    screen.blit(back_ground, (0, 0))
    map1.draw()


    while True :
        screen.blit(back_ground, (0, 0))
        screen.blit(interface, (1030, 0))
        map1.draw()
        pygame.display.flip()

        oldtime = time.time()
        curtime = time.time()

        while curtime - oldtime <=30000 :
            screen.blit(back_ground, (0, 0))
            screen.blit(interface, (1030, 0))





            map1.draw()








            pygame.display.flip()
            curtime = time.time()
















        while True :




            screen.blit(back_ground, (0, 0))
            screen.blit(interface, (1030, 0))
            map1.draw()
            pygame.display.flip()


        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)





