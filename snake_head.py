#class to handle the head of the snake
import pygame


"""
#square snakehead
class Snakehead():
	
	def __init__(self,screen,game_settings):
		self.screen=screen
		self.screen_rect=screen.get_rect()
		
		self.width,self.height=20,20
		self.colour=game_settings.white
		
		#build snake head rect object
		self.rect=pygame.Rect(0,0,self.width,self.height)
		self.rect.center=self.screen_rect.center
		
		#movement flags
		self.move_right=False
		self.move_left=False
		self.move_up=False
		self.move_down=False
		
	def draw_head(self):
		self.screen.fill(self.colour,self.rect)
		
	def update_head(self):
		if self.move_right==True:
			self.rect.centerx+=1
		if self.move_left==True:
			self.rect.centerx-=1		
		if self.move_up==True:
			self.rect.centery-=1
		if self.move_down==True:
			self.rect.centery+=1
"""

#circular snake head
class Snakehead():
	
	def __init__(self,screen,game_settings):
		self.screen=screen
		self.screen_rect=screen.get_rect()
		
		self.radius=10
		self.colour=game_settings.white
		
		#build snake head rect object
		self.rect=pygame.draw.circle(self.screen,self.colour,self.screen_rect.center,self.radius)
		self.rect.center=self.screen_rect.center
		
		#movement flags
		self.move_right=False
		self.move_left=False
		self.move_up=False
		self.move_down=False
		
	def draw_head(self):
		pygame.draw.circle(self.screen,self.colour,self.rect.center,self.radius)
		
	def update_head(self):
		if self.move_right==True:
			self.rect.centerx+=20
		if self.move_left==True:
			self.rect.centerx-=20		
		if self.move_up==True:
			self.rect.centery-=20
		if self.move_down==True:
			self.rect.centery+=20
