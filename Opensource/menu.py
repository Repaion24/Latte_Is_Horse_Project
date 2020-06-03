import pygame
import interface


def start_menu1 (screen):
    menu1_back = pygame.image.load("image/background/menu1_back.png")
    menu4 = pygame.image.load("image/menu/menu4.png")
    tutorial = pygame.image.load("image/map/tutorial.png")
    map1 = pygame.image.load("image/map/map1.png")
    map2 = pygame.image.load("image/map/map2.png")
    map3 = pygame.image.load("image/map/map3.png")


    while True:
        screen.blit(menu1_back, (0, 0))
        screen.blit(menu4, (192, 576))
        screen.blit(tutorial, (51,128))
        screen.blit(map1, (358, 128))
        screen.blit(map2, (665, 128))
        screen.blit(map3, (972, 128))

        position = pygame.mouse.get_pos()
        if position[0] > 384 and position[0] < 896:
            if position[1] > 576 and position[1] < 704:
                interface.print_click(screen,64,576)

        if position[1] > 128 and position[1] < 384:
            if position[0] > 51 and position[0] < 307:
                interface.print_check(screen,51,128)
            elif position[0] > 358 and position[0] < 614:
                interface.print_check(screen,358,128)
            elif position[0] > 665 and position[0] < 921:
                interface.print_check(screen,665,128)
            elif position[0] > 972 and position[0] < 1228:
                interface.print_check(screen,972,128)


        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if position[0] > 384 and position[0] < 896:
                    if position[1] > 576 and position[1] < 704:
                        return 1

                if position[1] > 128 and position[1] < 384:
                    if position[0] > 51 and position[0] < 307:
                        pass
                    elif position[0] > 358 and position[0] < 614:
                        pass
                    elif position[0] > 384 and position[0] < 921:
                        pass
                    elif position[0] > 972 and position[0] < 1228:
                        pass


def start_menu2 (screen):
    menu2_back = pygame.image.load("image/background/menu1_back.png")
    title2 = pygame.image.load("image/title/title2.png")
    menu4 = pygame.image.load("image/menu/menu4.png")
    yellow = pygame.image.load("image/screen/yellow.png")
    FileP = open("Ranking/Rank1.TXT","r")

    initial = FileP.readline()
    initial = initial.rstrip()
    score = FileP.readline()
    score = score.rstrip()
    health = FileP.readline()
    health = health.rstrip()
    gold = FileP.readline()
    gold = gold.rstrip()




    while True:
        screen.blit(menu2_back, (0, 0))
        screen.blit(title2,(384,0))
        screen.blit(menu4, (192, 576))
        screen.blit(yellow,(384,104))

        position = pygame.mouse.get_pos()
        if position[0] > 384 and position[0] < 896:
            if position[1] > 576 and position[1] < 704:
                interface.print_click(screen, 64, 576)



        font = pygame.font.Font(None,52)
        initialplayer = font.render("Player : "+str(initial),True,(0,0,0))
        scoreplayer = font.render("Score : " + str(score),True,(0,0,0))
        healthplayer = font.render("Remaining health : " + str(health),True,(0,0,0))
        goldplayer = font.render("Remaining gold : " + str(gold),True,(0,0,0))
        screen.blit(initialplayer,(416,310))
        screen.blit(scoreplayer, (416, 350))
        screen.blit(healthplayer, (416, 390))
        screen.blit(goldplayer, (416, 430))







        pygame.display.flip()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if position[0] > 384 and position[0] < 896:
                    if position[1] > 576 and position[1] < 704:
                        return 1


