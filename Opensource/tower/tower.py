#made by 김재희
import pygame

class tower :
    def __init__(self):
        self.x = 0
        self.y = 0
        self.tower_name = "normal tower"
        self.is_support = False
        self.width = 0
        self.height = 0
        self.damage = 2
        self.plus_damage = 0
        self.range = 100
        self.speed = 1
        self.level = 0
        self.attack = 0
        self.timer = 0
        self.selected = False
        self.upgrade_price = [50, 100, 150, "done"]
        self.sell_price = [25, 50, 75, 100]
        self.Timage = []
        self.Timage.append(pygame.image.load("tower/normal_tower1.png"))
        self.Timage.append(pygame.image.load("tower/normal_tower2.png"))
        self.sell = pygame.image.load("tower/sell.png")
        self.upgrade = pygame.image.load("tower/upgrade.png")


    def blit_tower(self, screen):
        self.draw_menu(screen)
        self.draw_surface(screen)
        self.draw_info(screen)
        screen.blit(self.Timage[self.attack], \
                    (self.x - self.Timage[self.attack].get_width()/2, self.y - self.Timage[self.attack].get_height()/2))


    def select_tower(self, X, Y):         #마우스 X좌표 Y좌표
        if X <= self.x + self.width/2 and X >= self.x - self.width/2 :
            if Y <= self.y + self.height/2 and Y >= self.y - self.height/2 :
                return True
        return False

    def draw_info(self, screen):
        if self.selected :
            tifont = pygame.font.Font(None, 24)
            tower_info = tifont.render(self.tower_name, True, (255, 255, 255))
            tower_damage = tifont.render("damage : " + str(self.damage+self.plus_damage), True, (255, 255, 255))
            tower_range = tifont.render("range : " + str(self.range), True, (255, 255, 255))
            tower_speed = tifont.render("attack speed : " + str(self.speed), True, (255, 255, 255))
            screen.blit(tower_info, (1065, 365))
            screen.blit(tower_damage, (1065, 385))
            screen.blit(tower_range, (1065, 405))
            screen.blit(tower_speed, (1065, 425))

    def draw_menu(self, screen):
        if self.selected:
            tfont = pygame.font.Font(None, 26)
            sell_font = tfont.render("Sell : " + str(self.sell_price[self.level]), True, (255, 255, 255))
            upgrade_font = tfont.render("Upgrade : " + str(self.upgrade_price[self.level]), True, (255, 255, 255))
            screen.blit(self.sell, (1048, 512))
            screen.blit(sell_font, (1068, 532))
            screen.blit(self.upgrade, (1048, 459))
            screen.blit(upgrade_font, (1068, 479))

    def draw_surface(self, screen):
        if self.selected:
            surface = pygame.Surface((self.range*4, self.range*4), pygame.SRCALPHA)
            pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)
            screen.blit(surface, (self.x - self.range, self.y - self.range))

    def build_tower(self, x, y):
        self.x = x
        self.y = y
        self.width = self.Timage[self.attack].get_width()
        self.height = self.Timage[self.attack].get_height()

    def sell_tower(self):
        return self.sell_price[self.level]

    def upgrade_tower(self):
        self.level += 1
        self.range += 25
        self.damage += 3
        return self.upgrade_price[self.level-1]

    def tower_attack(self, gtimer):
        if gtimer - self.timer >= self.speed :
            self.timer = gtimer
            self.attack += 1
            self.attack %= 2
            return True
        else :
            return False






