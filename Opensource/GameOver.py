import pygame
from pygame.locals import *
from os import unlink
import interface


# Copyright : 노관태 - 게임오버화면 구현 및 랭킹 정렬후 파일 입출력
def GameClear (screen,score,Health,gold) :

    up = "\n"

    shouldreturn =0

    Gameover_back = pygame.image.load("image/background/menu1_back.png")
    game_over = pygame.image.load("image/menu/Game_clear.png")
    name = ""
    Name = ""
    font = pygame.font.Font(None, 70)
    FileP1 = open("Ranking/Rank1.TXT", "r")
    FileP2 = open("Ranking/Rank2.TXT", "r")
    FileP3 = open("Ranking/Rank3.TXT", "r")

    rankP1 = FileP1.read()
    rankP2 = FileP2.read()
    rankP3 = FileP3.read()

    FileP1.seek(0)
    FileP2.seek(0)
    FileP3.seek(0)

    P1score = FileP1.readline()
    P2score = FileP2.readline()
    P3score = FileP3.readline()


    playerscore =  [P1score,P2score,P3score,score]

    FileP1.close()
    FileP2.close()
    FileP3.close()


    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    if len(name) <3:
                        name += evt.unicode
                        Name = name
                elif evt.key == K_BACKSPACE:
                    name = name[:-1]
                    Name = name
                elif evt.key == K_RETURN:
                    Name = name
                    name = ""
                    shouldreturn = 1
            elif evt.type == QUIT:
                return 1




        newplayer = str(score) + up + Name + up + str(Health) + up + str(gold)
        ranklist = interface.what_is_big(int(P1score),int(P2score),int(P3score),int(score))
        playerinf = [rankP1,rankP2,rankP3,newplayer]


        if shouldreturn == 1 :
            interface.saveinf(ranklist,playerinf,playerscore)
            return 1



        block = font.render(name, True, (0, 0, 0))
        yourscore = font.render("Your Score : "+ str(score),True,(255,0,0))
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(Gameover_back,(0,0))
        screen.blit(game_over, (256, 40))
        screen.blit(block, (600, 275))
        screen.blit(yourscore,(430,370))





        pygame.display.flip()

def GameOver (screen,score,Health,gold) :

    up = "\n"

    shouldreturn =0

    Gameover_back = pygame.image.load("image/background/menu1_back.png")
    game_over = pygame.image.load("image/menu/game_over.png")
    name = ""
    Name = ""
    font = pygame.font.Font(None, 70)
    FileP1 = open("Ranking/Rank1.TXT", "r")
    FileP2 = open("Ranking/Rank2.TXT", "r")
    FileP3 = open("Ranking/Rank3.TXT", "r")

    rankP1 = FileP1.read()
    rankP2 = FileP2.read()
    rankP3 = FileP3.read()

    FileP1.seek(0)
    FileP2.seek(0)
    FileP3.seek(0)

    P1score = FileP1.readline()
    P2score = FileP2.readline()
    P3score = FileP3.readline()


    playerscore =  [P1score,P2score,P3score,score]

    FileP1.close()
    FileP2.close()
    FileP3.close()


    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    if len(name) <3:
                        name += evt.unicode
                        Name = name
                elif evt.key == K_BACKSPACE:
                    name = name[:-1]
                    Name = name
                elif evt.key == K_RETURN:
                    Name = name
                    name = ""
                    shouldreturn = 1
            elif evt.type == QUIT:
                return 1




        newplayer = str(score) + up + Name + up + str(Health) + up + str(gold)
        ranklist = interface.what_is_big(int(P1score),int(P2score),int(P3score),int(score))
        playerinf = [rankP1,rankP2,rankP3,newplayer]


        if shouldreturn == 1 :
            interface.saveinf(ranklist,playerinf,playerscore)
            return 1



        block = font.render(name, True, (0, 0, 0))
        yourscore = font.render("Your Score : "+ str(score),True,(255,0,0))
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(Gameover_back,(0,0))
        screen.blit(game_over, (256, 40))
        screen.blit(block, (592,245))
        screen.blit(yourscore,(400,490))





        pygame.display.flip()