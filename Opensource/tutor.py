#shin
import pygame


def Tutorial(screen):
    Imgbefore = pygame.image.load("tutorial/before.png")
    Imgnext = pygame.image.load("tutorial/next.png")
    tImg1 = pygame.image.load("tutorial/main.png")
    tImg2 = pygame.image.load("tutorial/map.png")
    tImg3 = pygame.image.load("tutorial/wave.png")
    tImg4 = pygame.image.load("tutorial/menu.png")
    tImg5 = pygame.image.load("tutorial/tower.png")
    tImg6 = pygame.image.load("tutorial/virus.png")
    tImg7 = pygame.image.load("tutorial/rank.png")
    tImg8 = pygame.image.load("tutorial/start.png")

    getx = Imgnext.get_width()
    getu = Imgnext.get_height()
    std1 = [0,720-getu]
    std2 = [1280-getx,720-getu]
    count = 1

    while True:
        screen.fill((0,0,0))

        if count == 0:
            count = 0
        if count == 1:
            screen.blit(tImg1, (0,0))
        if count == 2:
            screen.blit(tImg2, (0,0))
        if count == 3:
            screen.blit(tImg3, (0,0))
        if count == 4:
            screen.blit(tImg4, (0,0))
        if count == 5:
            screen.blit(tImg5, (0,0))
        if count == 6:
            screen.blit(tImg6, (0,0))
        if count == 7:
            screen.blit(tImg7, (0,0))
        if count == 8:
            return 1
      # if count == 7:
          # return 2
        screen.blit(Imgbefore,(0,720-getu))
        screen.blit(Imgnext, (1280-getx,720-getu))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if position[0] >= 0 and position[0] <= getx:
                    if position[1] >= 720 - getu and position[1] <= 720:
                        count -= 1
                if position[0] >= 1280 - getx and position[0] <= 1280:
                    if position[1] >= 720 - getu and position[1] <= 720:
                        count += 1

