# v1 is made by 이동우
import pygame

class Virus:

    virusNum =0 #클래스 변수, 현재 맵에 있는 바이러스 수
    staticNum =0 #현재 만들어진 바이러스 수
    maxNum =0 #현재 맵에서 만들 수 있는 바이러스 수

    def __init__(self):
        self.img = pygame.image.load("resources/images/badguy.png") #바이러스 이미지
        self.health = pygame.image.load("resources/images/health.png")
        self.x_size = self.img.get_width() #바이러스 x 사이즈
        self.y_size = self.img.get_height() #바이러스 y 사이즈
        self.hp = 20 #바이러스 체력
        self.dmg = 5 #바이러스 공격력
        self.speed = 1 #바이러스 스피드
        self.path = [[600,250], [600,600],[300,600], [300,300], [0,300]] #변곡점
        self.path_index = 0
        Virus.virusNum = Virus.virusNum + 1 #바이러스가 한 마리 생성되면 그 숫자를 늘려준다

    def setNum(self, num): #현재 맵에 있는 바이러스 수와 맵에서 만들 수 있는 바이러스 수를 설정해준다
        Virus.virusNum = num
        Virus.maxNum = num

    def drawHealth(self, screen):
        for health1 in range(self.hp):
            screen.blit(self.health, (self.pos[0][0]+health1+1*health1, self.pos[0][1]+30))

    def pos(self, pos): #바이러스 좌표
        self.pos = pos

    def dead(self): #바이러스기 죽으면 전체 바이러스 수 1 감소
        Virus.virusNum = Virus.virusNum -1

    def move(self): #바이러스가 움직이는 좌표
        x = self.pos[0][0]
        y = self.pos[0][1]

        if self.path[self.path_index][0] == x and self.path[self.path_index][1] == y:
            self.path_index = self.path_index + 1
        if self.path[self.path_index][0] < x:
            self.pos[0][0] = self.pos[0][0] - self.speed
        if self.path[self.path_index][1] > y:
            self.pos[0][1] = self.pos[0][1] + self.speed
        elif self.path[self.path_index][1] < y:
            self.pos[0][1] = self.pos[0][1] - self.speed

