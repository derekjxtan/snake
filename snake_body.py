#class to handle the snakes body
import pygame

class Snakebody():
	
	def __init__(self,screen,game_settings,center_rect):
		self.screen=screen
		self.screen_rect=screen.get_rect()
		
		self.colour=game_settings.white
		self.width,self.height=20,20
		
		#build snake body rect object
		self.rect=pygame.Rect(0,0,self.width,self.height)
		self.rect.center=center_rect
		
		
	def draw_body(self):
		self.screen.fill(self.colour,self.rect)
