import pygame
from os import unlink


# Copyright : 노관태 - 코드 분할해둔곳들

def print_click(screen,x_pos,y_pos):

    click = pygame.image.load("image/get/click.png")
    click2 = pygame.image.load("image/get/click2.png")

    screen.blit(click, (x_pos, y_pos))
    screen.blit(click2, (x_pos+896+128, y_pos))
    return 1

def print_check(screen,x_pos,y_pos):

    check = pygame.image.load("image/get/check.png")

    screen.blit(check,(x_pos,y_pos))
    return 1

def what_is_big(x,y,z,d):
    num = [x,y,z,d]
    num.sort(reverse=True)
    renum = [num[0],num[1],num[2]]
    return renum

def saveinf(ranklist,playerinf,playerscore) :
    unlink("Ranking/Rank1.TXT")
    unlink("Ranking/Rank2.TXT")
    unlink("Ranking/Rank3.TXT")

    for j in range(0, 4, 1):
        if (int(ranklist[0]) == int(playerscore[j])):
            Fp = open("Ranking/Rank1.TXT", "w")
            Fp.write(playerinf[j])
            Fp.close()
        if (int(ranklist[1]) == int(playerscore[j])):
            Fp = open("Ranking/Rank2.TXT", "w")
            Fp.write(playerinf[j])
            Fp.close()
        if (int(ranklist[2]) == int(playerscore[j])):
            Fp = open("Ranking/Rank3.TXT", "w")
            Fp.write(playerinf[j])
            Fp.close()