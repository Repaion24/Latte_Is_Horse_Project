#made by 김재희
import pygame
from .tower import tower

class short_tower(tower) :
    def __init__(self) :
        self.x = 0
        self.y = 0
        self.tower_name = "short tower"
        self.is_support = False
        self.width = 0
        self.height = 0
        self.damage = 4
        self.plus_damage = 0
        self.range = 75
        self.speed = 0.5
        self.level = 0
        self.attack = 0
        self.timer = 0
        self.selected = False
        self.attack_on = False
        self.upgrade_price = [150, 200, 250, "Done"]
        self.sell_price = [75, 125, 175, 225]
        self.Timage = []
        self.Timage.append(pygame.image.load("tower/short_tower1.png"))
        self.Timage.append(pygame.image.load("tower/short_tower2.png"))
        self.sell = pygame.image.load("tower/sell.png")
        self.upgrade = pygame.image.load("tower/upgrade.png")

    def upgrade_tower(self):
        self.level += 1
        self.range += 25
        self.speed -= 0.1
        return self.upgrade_price[self.level-1]

    def draw_info(self, screen):
        if self.selected :
            tifont = pygame.font.Font(None, 24)
            tower_info = tifont.render(self.tower_name, True, (255, 255, 255))
            tower_damage = tifont.render("damage : " + str(self.damage+self.plus_damage), True, (255, 255, 255))
            tower_range = tifont.render("range : " + str(self.range), True, (255, 255, 255))
            tower_speed = tifont.render("attack speed : " + str(round(self.speed,1)), True, (255, 255, 255))
            screen.blit(tower_info, (1065, 365))
            screen.blit(tower_damage, (1065, 385))
            screen.blit(tower_range, (1065, 405))
            screen.blit(tower_speed, (1065, 425))