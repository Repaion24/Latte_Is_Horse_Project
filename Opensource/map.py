#made by 이동우
import pygame

class map: #copyright 이동우
    def __init__(self, screen):
        self.img = pygame.image.load("image/virus/mapicon1.png") #맵 블록 이미지 파일
        self.first = [0,0] #map의 초기좌표
        self.last = [0,0] #map의 마지막 좌표
        self.pos = [0,0]
        self.ch = [[300,100],[300,300],[100,300],[100,600],[600,600],[600,100],[1000,100],[1000,600],[1280,600]] #맵이 변하는 지점
        self.chIndex = 0
        self.x = self.img.get_width()
        self.y = self.img.get_height()
        self.screen = screen

    def set(self,first,last): #copyright 이동우
        self.first = first
        self.last = last

    def draw(self): #copyright 이동우
        self.chIndex =0
        for list in self.ch:
            if self.chIndex == 0:
                self.pos = self.first
            else:
                self.pos = self.ch[self.chIndex-1]

            if list[0] - self.pos[0] == 0: #전의 좌표와 비교해서 x좌표 변화가 없다면
                if list[1] -self.pos[1] > 0:
                    for y in range(self.pos[1]//self.y , list[1]// self.y):
                        self.screen.blit(self.img, (list[0], y*self.y))
                elif list[1] - self.pos[1] < 0:
                    for y in range(self.pos[1]//self.y , list[1]// self.y,-1):
                        self.screen.blit(self.img, (list[0], y*self.y))

            elif list[1] - self.pos[1] == 0:
                if list[0] -self.pos[0] > 0:
                    for x in range(self.pos[0]//self.x , list[0] // self.x):
                        self.screen.blit(self.img, (x*self.x, list[1]))
                elif list[0] - self.pos[0] < 0:
                    for x in range(self.pos[0]//self.y , list[0] // self.x,-1):
                        self.screen.blit(self.img, (x*self.x, list[1]))

            if self.ch[self.chIndex][0] == self.last[0]:
                self.screen.blit(self.img, ((self.last[0]//self.x)*self.x, self.pos[1]))
            self.chIndex += 1



