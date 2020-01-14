import sys
import pygame
from setting import Setting
from ship import Ship
from bullet import Bullet
from alien import Alien

def check_event_keydown(event,screen,ship,setting,bullets):
	if event.type==pygame.KEYDOWN:
		if event.key==pygame.K_RIGHT:
			ship.is_move_right=True
		if event.key==pygame.K_UP:
			ship.is_move_up=True	
		if event.key==pygame.K_LEFT:
			ship.is_move_left=True
		if event.key==pygame.K_DOWN:
			ship.is_move_down=True
		if event.key==pygame.K_TAB:
			new_bullet=Bullet(screen,ship,setting)
			#bullets.is_fired=True
			bullets.add(new_bullet)
		ship.ship_move(setting)
def check_event_keyup(event,ship,bullets):
	if event.type==pygame.KEYUP:
		if event.key==pygame.K_RIGHT:
			ship.is_move_right=False
		if event.key==pygame.K_UP:
			ship.is_move_up=False
		if event.key==pygame.K_LEFT:
			ship.is_move_left=False
		if event.key==pygame.K_DOWN:
			ship.is_move_down=False
		if event.key==pygame.K_TAB:
			bullets.is_fired=False
			
			
def check_event(ship,screen,setting,bullets):
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		
		check_event_keydown(event,screen,ship,setting,bullets)
		
		check_event_keyup(event,ship,bullets)

def screen_update(setting,screen,ship,bullets,alien):
	screen.fill(setting.screen_bgc)
	for bullet in bullets:
		bullet.draw_bullet()
	ship.blitme()
	alien.alien_blit()
	pygame.display.flip()