import pygame
#import sys
from pygame.locals import *
from setting import Setting
from ship import Ship
import game_function as game_f
from bullet import Bullet
from pygame.sprite import Group
from alien import Alien

def run_game():
    pygame.init()
    setting=Setting()
    screen=pygame.display.set_mode((setting.screen_w, setting.screen_h))
    pygame.display.set_caption("Alien War!")
    ship=Ship(screen)
    alien=Alien(screen,setting)
    bullets=Group()
    
    while True: 
        #alien.alien_move()
        game_f.check_event(ship,screen,setting,bullets)
	    #ship.ship_move(setting)
	    for bullet in bullets:
	        bullet.bullet_move()
	        if bullet.bullet_rect.top<=0:
	        	bullets.remove(bullet)
	    game_f.screen_update(setting,screen,ship,bullets,alien)

run_game()
	