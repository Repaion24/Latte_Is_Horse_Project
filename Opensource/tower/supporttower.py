#made by 김재희
import pygame

from .tower import tower

class support_tower(tower) :
    def __init__(self) :
        self.x = 0
        self.y = 0
        self.is_support = True
        self.width = 0
        self.height = 0
        self.plus_damage = 2
        self.range = 100
        self.speed = 1
        self.level = 0
        self.attack = 0
        self.timer = 0
        self.selected = False
        self.attack_on = False
        self.upgrade_price = [100, 150, 200, "Done"]
        self.sell_price = [50, 75, 100, 125]
        self.Timage = []
        self.Timage.append(pygame.image.load("tower/support_tower1.png"))
        self.Timage.append(pygame.image.load("tower/support_tower2.png"))
        self.sell = pygame.image.load("tower/sell.png")
        self.upgrade = pygame.image.load("tower/upgrade.png")

    def upgrade_tower(self):
        self.range += 25
        self.plus_damage += 1
        return self.upgrade_price[self.level]
