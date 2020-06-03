import pygame
import time
from tower.tower import tower

pygame.init()

class enemy :
    def __init__(self) :
        self.x = 0
        self.y = 0
        self.health = 4
        self.enemy_img = pygame.image.load("enemy.png")

screen = pygame.display.set_mode((1280, 720))
is_end = False

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


tower1 = []
enemy1 = []
index = -1
eindex = -1
timg = []
timg.append(pygame.image.load("tower/타워1.png"))
timg.append(pygame.image.load("tower/cancel.png"))
eimg = enemy_img = pygame.image.load("enemy.png")
build = 0
game_timer = time.time()
old_time = game_timer
gold = 0
round123 = 0

while not is_end :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            is_end = True
        if event.type == pygame.MOUSEBUTTONDOWN :
            position = pygame.mouse.get_pos()

            for i in range(0, len(tower1)) :
                if tower1[i].selected :
                    if position[1] >= 650 and position[1] <= 650 + tower1[i].sell.get_height():
                        if position[0] >= 400 and position[0] <= 400 + tower1[i].sell.get_width():
                            gold += tower1[i].sell_tower()
                            tower1.pop(i)
                            index -= 1
                            break
                        if position[0] >= 620 and position[0] <= 620 + tower1[i].upgrade.get_width():
                            gold -= tower1[i].upgrade_tower()
                    else :
                        tower1[i].selected = tower1[i].select_tower(position[0], position[1])
                else :
                    tower1[i].selected = tower1[i].select_tower(position[0], position[1])


            if build == 0 :
                if position[0]>=1100 and position[0]<=1100+timg[0].get_width() and\
                        position[1]>=120 and position[1]<=120+timg[0].get_height() :
                    index += 1
                    build += 1
                    tower1.append(tower())
                    tower1[index].timer = time.time()
                if position[0] >= 1100 and position[0] <= 1100 + eimg.get_width() and\
                        position[1] >= 300 and position[1] <= 300 + eimg.get_height():
                    eindex += 1
                    build += 2
                    enemy1.append(enemy())
            elif build == 1 :
                build -= 1
                if position[0]>=1100 and position[0]<=1100+timg[1].get_width() and\
                        position[1]>=520 and position[1]<=520+timg[1].get_height() :
                    index -= 1
                    tower1.pop()
            elif build == 2 :
                build -= 2
                if position[0]>=1100 and position[0]<=1100+eimg.get_width() and\
                        position[1]>=300 and position[1]<=300+eimg.get_height() :
                    eindex -= 1
                    enemy1.pop()


    screen.fill(BLACK)

    if build == 1 :
        position = pygame.mouse.get_pos()
        tower1[index].build_tower(position[0], position[1])

    elif build == 2 :
        position = pygame.mouse.get_pos()
        enemy1[eindex].x = position[0]
        enemy1[eindex].y = position[1]

    for i in range(0, len(tower1)) :
        for j in range(0, len(enemy1)) :
            if (enemy1[j].x - tower1[i].x)*(enemy1[j].x - tower1[i].x) \
                    + (enemy1[j].y - tower1[i].y)*(enemy1[j].y - tower1[i].y) <= tower1[i].range*tower1[i].range :
                tower1[i].attack_on = True
                break
            else :
                tower1[i].attack_on = False
        if tower1[i].attack_on == True :
            if game_timer - tower1[i].timer >= 1:
                tower1[i].timer = game_timer
                tower1[i].tower_attack()
        else :
            tower1[i].attack = 0

    for i in range(0, len(tower1)) :
        tower1[i].blit_tower(screen)

    for i in range(0, len(enemy1)) :
        screen.blit(enemy1[i].enemy_img, (enemy1[i].x - enemy1[i].enemy_img.get_width()/2, enemy1[i].y - enemy1[i].enemy_img.get_height()/2))

    screen.blit(timg[0], (1100, 120))
    screen.blit(timg[1], (1100, 520))
    screen.blit(eimg, (1100, 300))
    game_timer = time.time()
    pygame.display.flip()

pygame.quit()
quit()