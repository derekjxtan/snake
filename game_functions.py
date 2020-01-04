import pygame
import sys
from time import sleep

from snake_body import Snakebody


#function to handle events
def check_events(game_settings,snakehead,playbutton):
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
			
		if event.type==pygame.KEYDOWN:
			check_keydown_events(game_settings,event,snakehead)
			
		if event.type==pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y=pygame.mouse.get_pos()
			play_clicked=playbutton.rect.collidepoint((mouse_x,mouse_y))
			if play_clicked and game_settings.game_active==False:
				game_settings.game_active=True


#check keydown events
def check_keydown_events(game_settings,event,snakehead):
		if event.key==pygame.K_q:
			sys.exit()
			
		if event.key==pygame.K_LEFT and snakehead.move_right==False and game_settings.game_active==True:
			snakehead.move_left=True
			snakehead.move_right=False
			snakehead.move_up=False
			snakehead.move_down=False
		
		if event.key==pygame.K_RIGHT and snakehead.move_left==False and game_settings.game_active==True:
			snakehead.move_left=False
			snakehead.move_right=True
			snakehead.move_up=False
			snakehead.move_down=False
			
		if event.key==pygame.K_UP and snakehead.move_down==False and game_settings.game_active==True:
			snakehead.move_left=False
			snakehead.move_right=False
			snakehead.move_up=True
			snakehead.move_down=False
			
		if event.key==pygame.K_DOWN and snakehead.move_up==False and game_settings.game_active==True:
			snakehead.move_left=False
			snakehead.move_right=False
			snakehead.move_up=False
			snakehead.move_down=True

		if event.key==pygame.K_p:
			game_settings.game_active=True




#function to update screen
def update_screen(screen,game_settings,snakehead,food,snake_rect):
	if snake_rect:
		snake_rect.pop(-1)
	screen.fill(game_settings.black)
	snakehead.update_head()
	#if snakehead.rect.center not in snake_rect:
	snake_rect.append(snakehead.rect.center)
	snakehead.draw_head()
	food.draw_food()
	draw_snake_body(screen,game_settings,snake_rect)
	if snakehead.rect.colliderect(food.rect):
		food.move_food(game_settings)
		snake_body=Snakebody(screen,game_settings,(snake_rect[-1][0]+20,snake_rect[-1][1]+20))
		snake_rect.append((snake_rect[-1][0],snake_rect[-1][1]+20))
	sleep(0.05)
	



#function to draw the snake body
def draw_snake_body(screen,game_settings,snake_rect):
	for n in range(0,game_settings.points):
		center_rect=snake_rect[0]
		snakebody=Snakebody(screen,game_settings,center_rect)
		snakebody.draw_body()
		snake_rect.append(center_rect)
		snake_rect.pop(0)


		
#function to update screen when game not active
def update_inactive_screen(screen,game_settings,playbutton):
	screen.fill(game_settings.black)
	playbutton.draw_playbutton()
	
	




#function to end game
def end_game(game_settings,snakehead,snake_rect):
	if off_board(snakehead)==True and game_settings.game_active==True:
		initialize_game(game_settings,snakehead,snake_rect)
		sleep(1)
	
	if collide_tail(snakehead,snake_rect)==True and game_settings.game_active==True:
		initialize_game(game_settings,snakehead,snake_rect)
		sleep(1)


#function to check out of bounds
def off_board(snakehead):
	#check top and bottom
	if snakehead.rect.centery<10 or snakehead.rect.centery>590:
		return True
	#check left right
	if snakehead.rect.centerx<10 or snakehead.rect.centerx>1190:
		return True

		
#function to check if head collides with tail
def collide_tail(snakehead,snake_rect):
	snake_rect_copy=snake_rect.copy()
	if snake_rect_copy:
		snake_rect_copy.pop(0)
		for rect in snake_rect_copy:
			if snakehead.rect.center==rect:
				return True

	
#initiatize all settings
def initialize_game(game_settings,snakehead,snake_rect):
	game_settings.game_active=False
	game_settings.points=0
	snake_rect.clear()
	snakehead.move_right=False
	snakehead.move_left=False
	snakehead.move_up=False
	snakehead.move_down=False
	snakehead.rect.center=(600,300)
