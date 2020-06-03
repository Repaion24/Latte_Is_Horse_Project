import pygame
import random

pygame.init()

width, height = 1280, 720
screen = pygame.display.set_mode((width,height))
badguyimg = pygame.image.load("resources/images/badguy.png")
grass = pygame.image.load("resources/images/grass.png")
badtimer = 100
badtimer1 = 0
badguys = [[1280,250],]

while True:
    screen.fill((255,255,255))

    for x in range(width//grass.get_width()+1):
        screen.blit(grass, (x,200))
    index = 0
    for badguy in badguys:
        if badguy[0] < -64:
            badguys.pop(index)
        else:
            badguy[0] = badguy[0] -5

        screen.blit(badguyimg, badguy)
    pygame.display.flip()

    for event in pygame.event.get():
        # X 를 눌렀는지 검사
        if event.type == pygame.QUIT:
            # 게임종료
            pygame.quit()
            exit(0)
