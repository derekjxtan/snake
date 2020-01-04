import pygame
import sys

from settings import Settings
import game_functions as gf
from snake_head import Snakehead
from food import Food
from play_button import Playbutton

def run_game():
	pygame.init()
	game_settings=Settings()
	screen=pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
	pygame.display.set_caption("Snake")
	
	snakehead=Snakehead(screen,game_settings)
	food=Food(screen,game_settings)
	playbutton=Playbutton(screen,game_settings,'Play')
	
	snake_rect=[]
	
	#main loop of game
	while True:
		
		gf.check_events(game_settings,snakehead,playbutton)
		#print(game_active)
		if game_settings.game_active==True:
			gf.update_screen(screen,game_settings,snakehead,food,snake_rect)
			gf.end_game(game_settings,snakehead,snake_rect)
		if game_settings.game_active==False:
			gf.update_inactive_screen(screen,game_settings,playbutton)
		
		
		#draw lastest screen
		pygame.display.flip()
	
run_game()
