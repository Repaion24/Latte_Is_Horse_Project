# 파이게임 모듈 불러오기
import pygame
import menu
import interface
import GameOver


# 파이게임 초기화, 화면설정(해상도 1280*720)
pygame.init()
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))

# 이미지 객체
title_back_ground = pygame.image.load("image/background/title_back.png")
title = pygame.image.load("image/title/title.png")
menu1 = pygame.image.load("image/menu/menu1.png")
menu2 = pygame.image.load("image/menu/menu2.png")
menu3 = pygame.image.load("image/menu/menu3.png")
click = pygame.image.load("image/get/click.png")



# Copyright : 노관태 - 메인메뉴 구현
while True:
    # 화면 초기화
    screen.fill((0,0,0))

    #화면 요소들 그리기
    screen.blit(title_back_ground,(0,0))
    screen.blit(title, (128,-64))
    screen.blit(menu1, (192, 256))
    screen.blit(menu2, (192, 416))
    screen.blit(menu3, (192, 576))


    #마우스가 해당 위치에 올라갔을때
    position = pygame.mouse.get_pos()
    if position[0] > 192 and position[0] < 1088:
        if position[1] > 256 and position[1] < 384:
            interface.print_click(screen,64,256)
        elif position[1] > 416 and position[1] < 544:
            interface.print_click(screen,64,416)
        elif position[1] > 576 and position[1] < 704:
            interface.print_click(screen,64,576)


    # 화면 재구성
    pygame.display.flip()

    # X 누를시 종료
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    # 마우스 클릭시 발생 이밴트
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mixer.init()
            pygame.mixer.music.load("sound/click.wav")
            pygame.mixer.music.set_volume(1)  # 1 ~ 0.1

            pygame.mixer.music.play()

            pygame.mixer.Sound("sound/click.wav")

            position = pygame.mouse.get_pos()
            if position[0] >192 and position[0] < 1088 :
                if position[1] >256 and position[1] <384 :
                    menu.start_menu1(screen)
                elif position[1] >416 and position[1] <544 :
                    menu.start_menu2(screen)
                elif position[1] > 576 and position[1] <704 :
                    pygame.quit()
                    exit(0)


