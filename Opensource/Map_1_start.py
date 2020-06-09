import pygame
import map
import virus
import time
from tower.tower import tower
from tower.shorttower import short_tower
from tower.longtower import long_tower
from tower.supporttower import support_tower





def Map_1_starting(screen) :
    back_ground = pygame.image.load("image/virus/map2.png")
    interface = pygame.image.load("image/virus/interface.png")
    map1 = map.map(screen)
    map1.ch = [[120,60],[120,420],[300,420],[300,180],[540,180],[540,420],[780,420],[780,720]]
    map1.set([0, 60], [1280, 600])

    support_index = []

    tower1 = []
    enemy1 = []
    index = -1
    eindex = -1
    timg = []
    timg.append(pygame.image.load("tower/normal_tower1.png"))
    timg.append(pygame.image.load("tower/short_tower1.png"))
    timg.append(pygame.image.load("tower/long_tower1.png"))
    timg.append(pygame.image.load("tower/support_tower1.png"))
    cancel_img = pygame.image.load("tower/cancel.png")
    build = 0
    build_ok = True
    game_timer = time.time()
    old_time = game_timer
    gold = 1000
    round123 = 0
    Font = pygame.font.Font(None, 52)
    font = pygame.font.Font(None, 26)

    screen.blit(back_ground, (0, 0))
    map1.draw()


    while True :
        screen.blit(back_ground, (0, 0))
        screen.blit(interface, (1030, 0))
        map1.draw()
        pygame.display.flip()

        oldtime = time.time()
        curtime = time.time()

        while curtime - oldtime <=5 : #Copyright : 김재희
            timer = Font.render("Time : " + str(int(30-(curtime-oldtime))),True,(0,0,0))

            screen.blit(back_ground, (0, 0))
            screen.blit(interface, (1030, 0))
            screen.blit(timer,(850,20))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    if build == 0:  # made by 김재희~
                        for i in range(0, len(tower1)):
                            if tower1[i].selected:
                                if position[1] >= 650 and position[1] <= 650 + tower1[i].sell.get_height():
                                    if position[0] >= 400 and position[0] <= 400 + tower1[i].sell.get_width():
                                        gold += tower1[i].sell_tower()
                                        if tower1[i].is_support == True:
                                            for k in range(0, len(support_index)):
                                                if support_index[k] == i:
                                                    support_index.pop(k)
                                                    break
                                            for k in range(0, len(tower1)):
                                                if tower1[k].is_support == False:
                                                    tower1[k].plus_damage = 0
                                        tower1.pop(i)
                                        index -= 1
                                        break
                                    if position[0] >= 620 and position[0] <= 620 + tower1[i].upgrade.get_width():
                                        if tower1[i].level <= 2:
                                            if gold >= tower1[i].upgrade_price[tower1[i].level]:
                                                if tower1[i].level == 2:
                                                    tower1[i].upgrade_tower()
                                                else:
                                                    gold -= tower1[i].upgrade_tower()
                                else:
                                    tower1[i].selected = tower1[i].select_tower(position[0], position[1])
                            else:
                                tower1[i].selected = tower1[i].select_tower(position[0], position[1])

                        if position[0] >= 1050 and position[0] <= 1050 + timg[0].get_width() and \
                                position[1] >= 110 and position[1] <= 110 + timg[0].get_height():
                            if gold >= 50:
                                gold -= 50
                                index += 1
                                build += 1
                                tower1.append(tower())
                                tower1[index].timer = time.time()
                        if position[0] >= 1170 and position[0] <= 1170 + timg[1].get_width() and \
                                position[1] >= 110 and position[1] <= 110 + timg[1].get_height():
                            if gold >= 100:
                                gold -= 100
                                index += 1
                                build += 1
                                tower1.append(short_tower())
                                tower1[index].timer = time.time()
                        if position[0] >= 1050 and position[0] <= 1050 + timg[2].get_width() and \
                                position[1] >= 230 and position[1] <= 230 + timg[2].get_height():
                            if gold >= 100:
                                gold -= 100
                                index += 1
                                build += 1
                                tower1.append(long_tower())
                                tower1[index].timer = time.time()
                        if position[0] >= 1170 and position[0] <= 1170 + timg[3].get_width() and \
                                position[1] >= 230 and position[1] <= 230 + timg[3].get_height():
                            if gold >= 100:
                                gold -= 100
                                index += 1
                                build += 1
                                tower1.append(support_tower())
                                support_index.append(index)
                                tower1[index].timer = time.time()
                    elif build == 1:
                        for i in range(0, len(tower1)):
                            if (i != index):
                                if (position[0] <= tower1[i].x + timg[0].get_width() / 2 and position[0] >= tower1[
                                    i].x - timg[0].get_width() / 2 \
                                        and position[1] <= tower1[i].y + timg[0].get_height() / 2 and position[1] >=
                                        tower1[i].y - timg[0].get_height() / 2):
                                    build_ok = False
                                    break
                                else:
                                    build_ok = True
                        if (build_ok == True):
                            build -= 1
                        if position[0] >= 1150 and position[0] <= 1150 + cancel_img.get_width() and \
                                position[1] >= 615 and position[1] <= 615 + cancel_img.get_height():
                            index -= 1
                            tower1.pop()

            if build == 1:  # made by 김재희~
                position = pygame.mouse.get_pos()
                tower1[index].build_tower(position[0], position[1])
            for i in range(0, len(tower1)):
                attack_on = False
                if len(enemy1) > 0:
                    for j in range(0, len(enemy1)):
                        if (tower1[i].is_support != True):
                            if (enemy1[j].x - tower1[i].x) * (enemy1[j].x - tower1[i].x) \
                                    + (enemy1[j].y - tower1[i].y) * (enemy1[j].y - tower1[i].y) <= tower1[i].range * \
                                    tower1[i].range:
                                attack_on = True
                                if tower1[i].tower_attack(game_timer):
                                    enemy1[j].health -= tower1[i].damage + tower1[i].plus_damage
                                    if enemy1[j].health <= 0:
                                        enemy1.pop(j)
                                        eindex -= 1
                                break
                            else:
                                attack_on = False
                else:
                    if tower1[i].is_support == False:
                        tower1[i].attack = 0
                if attack_on == False:
                    tower1[i].attack = 0
            if build == 0:
                for i in support_index:
                    exist = False
                    for j in range(0, len(tower1)):
                        if tower1[j].is_support == False:
                            if (tower1[j].x - tower1[i].x) * (tower1[j].x - tower1[i].x) \
                                    + (tower1[j].y - tower1[i].y) * (tower1[j].y - tower1[i].y) <= tower1[i].range * \
                                    tower1[i].range:
                                tower1[j].plus_damage = tower1[i].plus_damage
                                exist = True
                                tower1[i].tower_attack(game_timer)
                    if exist == False:
                        tower1[i].attack = 0  # ~made by 김재희

            for i in range(0, len(tower1)):
                tower1[i].blit_tower(screen)

            for i in range(0, len(enemy1)):
                screen.blit(enemy1[i].enemy_img, (
                enemy1[i].x - enemy1[i].enemy_img.get_width() / 2, enemy1[i].y - enemy1[i].enemy_img.get_height() / 2))

            gold_font = font.render(str(gold), True, (0, 0, 0))
            screen.blit(gold_font, (1195, 32))
            screen.blit(timg[0], (1050, 112))
            screen.blit(timg[1], (1175, 115))
            screen.blit(timg[2], (1052, 238))
            screen.blit(timg[3], (1177, 233))
            screen.blit(cancel_img, (1150, 615))

            map1.draw()

            pygame.display.flip()
            curtime = time.time()


        while True :
            screen.blit(back_ground, (0, 0))
            screen.blit(interface, (1030, 0))
            map1.draw()
            for i in range(0, len(tower1)):
                tower1[i].blit_tower(screen)
            gold_font = font.render(str(gold), True, (0, 0, 0))
            screen.blit(gold_font, (1195, 32))
            screen.blit(timg[0], (1050, 112))
            screen.blit(timg[1], (1175, 115))
            screen.blit(timg[2], (1052, 238))
            screen.blit(timg[3], (1177, 233))
            screen.blit(cancel_img, (1150, 615))








            pygame.display.flip()


        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)





