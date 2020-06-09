# virus.py is made by 이동우
import pygame
import math

WHITE = (255,255,255)
BLACK = (0,0,0)

def madeVirus(a,b,c=0,d=0): #copyright 이동우
    enemy = []
    index = -1
    for i in range(0, a):
        enemy.append(Virus())
        index += 1
    for j in range(0, b):
        enemy.append(Virus(1))
        index += 1
        enemy[index].setType()
    for x in range(0, c):
        enemy.append(Virus(2))
        index += 1
        enemy[index].setType()
    for z in range(0, d):
        enemy.append(Virus(3))
        index += 1
        enemy[index].setType()

    return enemy


def draw_text(text, surface, x, y, main_color): #copyright 이동우
    font = pygame.font.SysFont("notosanscjkkr", 30)
    text_obj = font.render(text, True, main_color)
    text_rect = text_obj.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    surface.blit(text_obj, text_rect)

class Virus: #copyright 이동우

    virusNum =0 #클래스 변수, 현재 맵에 있는 바이러스 수
    staticNum =0 #현재 만들어진 바이러스 수
    maxNum =0 #현재 맵에서 만들 수 있는 바이러스 수
    AllNum = 0 #여태까지 죽인 모든 바이러스 수

    def __init__(self,type=0): #copyright 이동우
        self.img = pygame.image.load("image/virus/virus_0.png") #바이러스 이미지
        self.type = type
        #self.health = pygame.image.load("img/health.png")
        self.x_size = self.img.get_width() #바이러스 x 사이즈
        self.y_size = self.img.get_height() #바이러스 y 사이즈
        self.pos =[0,0]
        self.center = [0,0]
        self.radian = math.sqrt(pow(self.x_size,2)+pow(self.y_size,2))/2
        self.distance=0
        self.name = "MERS virus"
        self.hp = 20 #바이러스 체력
        self.dmg = 5 #바이러스 공격력
        self.speed = 1 #바이러스 스피드
        self.path = [[1000,600],[1000,100],[600,100],[600,600],[100,600],[100,300],[300,300],[300,100],[0,100]] #변곡점
        self.path_index = 0
        self.drawterm = 1
        self.drawNum = 0
        Virus.virusNum = Virus.virusNum + 1 #바이러스가 한 마리 생성되면 그 숫자를 늘려준다

    def setType(self): #copyright 이동우
        if self.type == 1:
            self.type1()
        elif self.type == 2:
            self.type2()
        elif self.type == 3:
            self.type3()

    def calDistance(self,x,y): #copyright 이동우
        self.setCenter()
        self.distance = math.sqrt(pow(x-self.center[0],2)+pow(y-self.center[1],2))

    def setCenter(self): #copyright 이동우
        self.center =[self.pos[0]+self.x_size/2, self.pos[1]+self.y_size/2]

    def boolDtc(self): #copyright 이동우
        if self.distance <= self.radian:
            return True
        return False

    def setNum(self, num): #현재 맵에 있는 바이러스 수와 맵에서 만들 수 있는 바이러스 수를 설정해준다  #copyright 이동우
        Virus.virusNum = num
        Virus.maxNum = num
    #
    # def drawHealth(self, screen):
    #     for health1 in range(self.hp):
    #         screen.blit(self.health, (self.pos[0][0]+health1+1*health1, self.pos[0][1]+30))

    def setPos(self, pos): #바이러스 좌표  #copyright 이동우
        self.pos = pos

    def dead(self): #바이러스기 죽으면 전체 바이러스 수 1 감소  #copyright 이동우
        Virus.AllNum = Virus.AllNum +1
        Virus.virusNum = Virus.virusNum -1

    def deadP(self): #copyright 이동우
        Virus.virusNum = Virus.virusNum -1

    def move(self): #바이러스가 움직이는 좌표 #copyright 이동우
        x = self.pos[0]
        y = self.pos[1]

        if self.path[self.path_index][0] == x and self.path[self.path_index][1] == y:
            self.path_index = self.path_index + 1
        if self.path[self.path_index][0] < x:
            self.pos[0] = self.pos[0] - self.speed
        elif self.path[self.path_index][0] > x:
            self.pos[0] = self.pos[0] + self.speed
        if self.path[self.path_index][1] > y:
            self.pos[1] = self.pos[1] + self.speed
        elif self.path[self.path_index][1] < y:
            self.pos[1] = self.pos[1] - self.speed

    def drawInfo(self,screen,x,y): #copyright 이동우
        draw_text("name:",screen,x,y,BLACK)
        draw_text(str(self.name),screen,x+100,y,BLACK)
        draw_text("hp:",screen,x,y+20,BLACK)
        draw_text(str(self.hp),screen,x+100,y+20,BLACK)
        draw_text("speed:",screen,x,y+40,BLACK)
        draw_text(str(self.speed),screen,x+100,y+40,BLACK)


    def Repeat(self,Y): #copyright 이동우
        self.drawNum = self.drawNum + self.drawterm
        Y = Y + self.drawNum

        if self.drawNum == 3:
            self.drawterm = -1
        if self.drawNum == -3:
            self.drawterm = +1

        return Y

    def type1(self): #copyright 이동우
        self.img = pygame.image.load("image/virus/virus_1.png")  # 바이러스 이미지
        self.name = "ZIKA virus"
        self.hp = 12  # 바이러스 체력
        self.dmg = 5  # 바이러스 공격력
        self.speed = 2  # 바이러스 스피드

    def type2(self): #copyright 이동우
        self.img = pygame.image.load("image/virus/virus_2.png")  # 바이러스 이미지
        self.name = "EBOLA virus"
        self.hp = 12  # 바이러스 체력
        self.dmg = 5  # 바이러스 공격력
        self.speed = 1  # 바이러스 스피드

    def type3(self): #copyright 이동우
        self.img = pygame.image.load("image/virus/virus_bh.png")  # 바이러스 이미지
        self.name = " CORONA virus"
        self.hp = 12  # 바이러스 체력
        self.dmg = 5  # 바이러스 공격력
        self.speed = 1  # 바이러스 스피드
