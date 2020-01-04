#class to handle the food
import pygame
from random import randint

class Food():
	
	def __init__(self,screen,game_settings):
		self.screen=screen
		self.screen_rect=screen.get_rect()
		
		self.width,self.height=10,10
		self.colour=game_settings.white
		
		#build rect
		self.rect=pygame.Rect(randint(5,1195),randint(5,595),self.width,self.height)
		
	def draw_food(self):
		self.screen.fill(self.colour,self.rect)
		
	def move_food(self,game_settings):
		self.rect.centerx=randint(400,800)
		self.rect.centery=randint(200,400)
		game_settings.points+=1
