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
        self.damage = 1
        self.plus_damage = 0
        self.range = 75
        self.speed = 0.5
        self.level = 0
        self.attack = 0
        self.timer = 0
        self.selected = False
        self.attack_on = False
        self.upgrade_price = [100, 150, 200, "done"]
        self.sell_price = [50, 75, 100, 100]
        self.Timage = []
        self.Timage.append(pygame.image.load("tower/short_tower1.png"))
        self.Timage.append(pygame.image.load("tower/short_tower2.png"))
        self.sell = pygame.image.load("tower/sell.png")
        self.upgrade = pygame.image.load("tower/upgrade.png")