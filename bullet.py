import pygame
from pygame.sprite import Sprite
from setting import Setting

class Bullet(Sprite):
    def __init__(self,screen,ship,setting):
        super().__init__()
        self.screen=screen
        self.bullet_rect=pygame.Rect(0,0,setting.bullet_w,setting.bullet_h)
        self.bullet_rect.centerx=ship.ship_rect.centerx
        self.bullet_rect.top=ship.ship_rect.top
        self.bullet_color=setting.bullet_c
        self.bullet_speed=setting.bullet_s
        self.is_fired=False
        #defin bullet method
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.bullet_color, self.bullet_rect)
    def bullet_move(self):
        self.bullet_rect.top-=self.bullet_speed
