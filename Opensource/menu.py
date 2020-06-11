import pygame
import interface
import GameOver
import Map_1_start

# Copyright : 노관태 - 메뉴1 구현 - 맵 선택화면


def start_menu1 (screen):
    menu1_back = pygame.image.load("image/background/menu1_back.png")
    menu4 = pygame.image.load("image/menu/menu4.png")
    tutorial = pygame.image.load("image/map/tutorial.png")
    map1 = pygame.image.load("image/map/map1.png")
    map2 = pygame.image.load("image/map/map2.png")


    while True:
        screen.blit(menu1_back, (0, 0))
        screen.blit(menu4, (192, 576))
        screen.blit(tutorial, (128,128))
        screen.blit(map1, (128+256+128, 128))
        screen.blit(map2, (128+256+128+256+128, 128))

        position = pygame.mouse.get_pos()
        if position[0] > 384 and position[0] < 896:
            if position[1] > 576 and position[1] < 704:
                interface.print_click(screen,64,576)

        if position[1] > 128 and position[1] < 384:
            if position[0] > 128 and position[0] < 128+256:
                interface.print_check(screen,128,128)
            elif position[0] >128+256+128 and position[0] < 128+256+128+256:
                interface.print_check(screen,128+256+128,128)
            elif position[0] > 128+256+128+256+128 and position[0] < 128+256+128+256+128+256:
                interface.print_check(screen,128+256+128+256+128,128)


        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.init()
                pygame.mixer.music.load("sound/click.wav")
                pygame.mixer.music.set_volume(1)  # 1 ~ 0.1

                pygame.mixer.music.play()

                pygame.mixer.Sound("sound/click.wav")
                position = pygame.mouse.get_pos()
                if position[0] > 384 and position[0] < 896:
                    if position[1] > 576 and position[1] < 704:
                        return 1

                if position[1] > 128 and position[1] < 384:
                    if position[0] > 128 and position[0] < 128+256:
                        GameOver.GameOver(screen,95000,8,1200)
                        return 1
                    elif position[0] > 128 + 256 + 128 and position[0] < 128 + 256 + 128 + 256:
                        Map_1_start.Map_1_starting(screen)
                        return 1
                    elif position[0] > 128 + 256 + 128 and position[0] < 128 + 256 + 128 + 256:
                        pass



# Copyright : 노관태 - 메뉴2 구현 - 랭킹 파일 입출력

def start_menu2 (screen):
    menu2_back = pygame.image.load("image/background/menu1_back.png")
    title2 = pygame.image.load("image/title/title2.png")
    menu4 = pygame.image.load("image/menu/menu4.png")
    ranking1 = pygame.image.load("image/screen/1st.png")
    ranking2 = pygame.image.load("image/screen/2nd.png")
    ranking3 = pygame.image.load("image/screen/3rd.png")
    FileP1 = open("Ranking/Rank1.TXT","r")
    FileP2= open("Ranking/Rank2.TXT","r")
    FileP3= open("Ranking/Rank3.TXT","r")


    score1 = FileP1.readline()
    initial1 = FileP1.readline()
    health1 = FileP1.readline()
    gold1 = FileP1.readline()

    initial1 = initial1.rstrip()
    score1 = score1.rstrip()
    health1 = health1.rstrip()
    gold1 = gold1.rstrip()


    score2 = FileP2.readline()
    initial2 = FileP2.readline()
    health2 = FileP2.readline()
    gold2 = FileP2.readline()

    initial2 = initial2.rstrip()
    score2 = score2.rstrip()
    health2 = health2.rstrip()
    gold2 = gold2.rstrip()


    score3 = FileP3.readline()
    initial3 = FileP3.readline()
    health3 = FileP3.readline()
    gold3 = FileP3.readline()

    initial3 = initial3.rstrip()
    score3 = score3.rstrip()
    health3 = health3.rstrip()
    gold3 = gold3.rstrip()


    while True:
        screen.blit(menu2_back, (0, 0))
        screen.blit(title2,(384,0))
        screen.blit(menu4, (192, 576))
        screen.blit(ranking1,(512,256))
        screen.blit(ranking2, (128, 256))
        screen.blit(ranking3, (896, 256))

        position = pygame.mouse.get_pos()
        if position[0] > 384 and position[0] < 896:
            if position[1] > 576 and position[1] < 704:
                interface.print_click(screen, 64, 576)

        font = pygame.font.Font(None,26)
        initialplayer1 = font.render("Player : "+str(initial1),True,(0,0,0))
        scoreplayer1 = font.render("Score : " + str(score1),True,(0,0,0))
        healthplayer1 = font.render("Remaining health : " + str(health1),True,(0,0,0))
        goldplayer1 = font.render("Remaining gold : " + str(gold1),True,(0,0,0))
        screen.blit(initialplayer1,(530,310))
        screen.blit(scoreplayer1, (530, 350))
        screen.blit(healthplayer1, (530, 390))
        screen.blit(goldplayer1, (530, 430))

        initialplayer2 = font.render("Player : " + str(initial2), True, (0, 0, 0))
        scoreplayer2 = font.render("Score : " + str(score2), True, (0, 0, 0))
        healthplayer2 = font.render("Remaining health : " + str(health2), True, (0, 0, 0))
        goldplayer2 = font.render("Remaining gold : " + str(gold2), True, (0, 0, 0))
        screen.blit(initialplayer2, (146, 310))
        screen.blit(scoreplayer2, (146, 350))
        screen.blit(healthplayer2, (146, 390))
        screen.blit(goldplayer2, (146, 430))

        initialplayer3 = font.render("Player : " + str(initial3), True, (0, 0, 0))
        scoreplayer3 = font.render("Score : " + str(score3), True, (0, 0, 0))
        healthplayer3 = font.render("Remaining health : " + str(health3), True, (0, 0, 0))
        goldplayer3 = font.render("Remaining gold : " + str(gold3), True, (0, 0, 0))
        screen.blit(initialplayer3, (914, 310))
        screen.blit(scoreplayer3, (914, 350))
        screen.blit(healthplayer3, (914, 390))
        screen.blit(goldplayer3, (914, 430))


        pygame.display.flip()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.init()
                pygame.mixer.music.load("sound/click.wav")
                pygame.mixer.music.set_volume(1)  # 1 ~ 0.1

                pygame.mixer.music.play()

                pygame.mixer.Sound("sound/click.wav")
                position = pygame.mouse.get_pos()
                if position[0] > 384 and position[0] < 896:
                    if position[1] > 576 and position[1] < 704:
                        FileP1.close()
                        FileP2.close()
                        FileP3.close()
                        return 1


