import pygame
from setting import Setting

class Ship(object):
    def __init__(self,screen):
        self.screen=screen
        self.ship_image=pygame.image.load("ship1.jpg")
        self.ship_rect=self.ship_image.get_rect()
        self.screen_rect=self.screen.get_rect()
        self.ship_rect.centerx=self.screen_rect.centerx
        self.ship_rect.bottom=self.screen_rect.bottom
        self.is_move_right=False
        self.is_move_left=False
        self.is_move_up=False
        self.is_move_down=False
        self.is_fire=False
    def ship_move(self,setting):
        if self.is_move_right==True and self.ship_rect.right<self.screen_rect.right:
            self.ship_rect.right+=setting.ship_speed
        if self.is_move_up==True and self.ship_rect.top>0:
            self.ship_rect.top-=setting.ship_speed
        if self.is_move_left==True and self.ship_rect.left>0:
            self.ship_rect.left-=setting.ship_speed
        if self.is_move_down and self.ship_rect.bottom<self.screen_rect.bottom:
            self.ship_rect.bottom+=setting.ship_speed
    def ship_fire(self,screen):
        if self.is_fire:
            weapon=Weapon(screen,ship)
            weapon.weapon_move(setting)
    def blitme(self):
        self.screen.blit(self.ship_image,self.ship_rect)
