import pygame
import virus
import map

pygame.init()
WHITE = (255,255,255)
BLACK = (0,0,0)

selectNum = -1
selectTure = False

width, height = 1280, 720
screen = pygame.display.set_mode((width,height))
wave_num = 6 #이번 wave에 등장하는 몬스터의 숫자
badguy = virus.madeVirus(1,2,2,1) #바이러스 객체들을 담을 배열
for i in range(0,wave_num):
    badguy[i].setPos([1280,600])

TARGET_FPS = 100
clock = pygame.time.Clock()
life = 20
count = 0 #타임 조정을 위해 선언됨

while True:

    #마우스 좌표받기 #copyright 이동우
    position = pygame.mouse.get_pos()

    #화면 구성 #copyright 이동우
    screen.fill((255,255,255))

    #임의의 맵 구현 #copyright 이동우
    map1 = map.map(screen)
    map1.set([0, 100], [1280, 600])
    map1.draw()

    #타이머 구현 #copyright 이동우
    if count == 0:
        count += 1
        tick = pygame.time.get_ticks()
    if 2900 <= pygame.time.get_ticks() - tick <= 3000:
        if virus.Virus.staticNum < wave_num:
            virus.Virus.staticNum += 1
            count -= 1

    #문구 출력 #copyright 이동우
    virus.draw_text("remaining virus : ",screen,150,150,BLACK)
    virus.draw_text(str(virus.Virus.virusNum),screen,250,150,BLACK)
    virus.draw_text(str(selectNum),screen,250,170,BLACK)
    if life < 0:
        virus.draw_text("Game over", screen, 640, 300, BLACK)

    #바이러스 좌표 조정 #copyright 이동우
    for n in range(0, virus.Virus.staticNum):
        if badguy[n].pos[0] < badguy[n].x_size: #바이러스가 맵 끝에 도달하면
            badguy[n].deadP()
            badguy.pop(n)
            if selectNum == n:
                selectNum = -1
            elif selectNum > n:
                selectNum -=1
            virus.Virus.staticNum -= 1
            life = life -5 #타워의 hp도 깎인다
            break
        else:
           badguy[n].move()

    #바이러스 화면 출력 #copyright 이동우
    for n in range(0, virus.Virus.staticNum):
        x = badguy[n].pos[0]
        y = badguy[n].Repeat(badguy[n].pos[1])
        screen.blit(badguy[n].img, (x,y))

    #바이러스 클릭 시 바이러스 정보 출력 #copyright 이동우
    if selectNum != -1:
        badguy[selectNum].drawInfo(screen, 1000, 600)
    for n in range(0, virus.Virus.staticNum):
        badguy[n].calDistance(position[0], position[1])

    #화면 재구성 #copyright 이동우
    pygame.display.flip()

    #이벤트 구성 - 마우스 클릭 #copyright 이동우
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(0, virus.Virus.staticNum):
                if badguy[i].boolDtc():
                    selectNum = i
        # 게임종료 #copyright 이동우
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)


