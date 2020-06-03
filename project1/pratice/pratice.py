import pygame
import virus

pygame.init()
WHITE = (255,255,255)
BLACK = (0,0,0)

width, height = 1280, 720
screen = pygame.display.set_mode((width,height))
wave_num = 5  #이번 wave에 등장하는 몬스터의 숫자
badguy = [num for num in range(0,wave_num)] #바이러스 객체들을 담을 배열
for i in range(0,wave_num):
    badguy[i]= virus.Virus() #여러마리의 바이러스 객체를 만든다
    badguy[i].pos([[1280,250],])

grass = pygame.image.load("resources/images/grass.png") #맵의 이미지

badtimer = 100 #몬스터 출현간격을 조정해준다
badtimer1 = 0
TARGET_FPS = 100
clock = pygame.time.Clock()
life = 20

def draw_text(text, surface, x, y, main_color):
    font = pygame.font.SysFont("notosanscjkkr", 30)
    text_obj = font.render(text, True, main_color)
    text_rect = text_obj.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    surface.blit(text_obj, text_rect)

while True:
    badtimer = badtimer-1
    clock.tick(TARGET_FPS)
    screen.fill((255,255,255))
    #임의의 맵 구현
    for x in range(300//grass.get_width()): #range에 들어가는 것이 개수이다 300//100 +1 이므로 4개가 들어가게 된다
        screen.blit(grass,(x*100,300))
    for y in range(300//grass.get_height(),600//grass.get_height()):
        screen.blit(grass,(300,y*100))
    for x in range(300//grass.get_width(),600//grass.get_width()):
        screen.blit(grass,(x*100,600))
    for y in range(600//grass.get_height(),200//grass.get_height()-1, -1):
        screen.blit(grass,(600, y*100))
    for x in range(600//grass.get_width(),1280//grass.get_width()+1):
        screen.blit(grass,(x*100,200))

    draw_text("remaining virus : ",screen,150,150,BLACK)
    draw_text(str(virus.Virus.virusNum),screen,250,150,BLACK)

    if virus.Virus.staticNum < wave_num:
        if badtimer == 0:
            virus.Virus.staticNum = virus.Virus.staticNum+1
            badtimer = 100-(badtimer1*2)
            if badtimer1 >= 35:
                badtimer1 = 35
            else:
                badtimer1 = badtimer1+5

    for n in range(0, virus.Virus.staticNum):
        for badguys in badguy[n].pos:
            if badguys[0] < badguy[n].x_size: #바이러스가 맵 끝에 도달하면
                badguy[n].pos.pop() #해당 위치정보를 pop해서 바이러스 삭제
                badguy[n].dead()
                life = life -5 #타워의 hp도 깎인다
            else:
               badguy[n].move()

    if life < 0:
        draw_text("Game over", screen, 640, 300, BLACK)

    for n in range(0, virus.Virus.staticNum):
        for badguys in badguy[n].pos: #이미지를 맵에 출력
            badguy[n].drawHealth(screen) #몬스터의 healthbar 출력
            screen.blit(badguy[n].img, badguys)

    pygame.display.flip()

    for event in pygame.event.get():
        # X 를 눌렀는지 검사
        if event.type == pygame.QUIT:
            # 게임종료
            pygame.quit()
            exit(0)


