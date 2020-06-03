import pygame
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