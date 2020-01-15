import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #define class alien
    def __init__(self,screen,setting):
        super().__init__()
        self.screen=screen
        self.setting=setting
        self.alien_image=pygame.image.load("ship2.jpg")
        self.alien_rect=self.alien_image.get_rect()
        self.alien_rect.x=self.alien_rect.width
        self.alien_rect.y=self.alien_rect.height
    #define alien method
    def alien_blit(self):
        self.screen.blit(self.alien_image,self.alien_rect)
    def alien_move(self):
        self.alien_rect.bottom +=self.setting.alien_speed
