#class to handle the play button

import pygame.font

class Playbutton():
	
	def __init__(self,screen,game_settings,msg):
		self.screen=screen
		self.screen_rect=screen.get_rect()
		
		self.button_colour=game_settings.white
		self.width,self.height=200,100
		self.text_colour=game_settings.black
		self.font=pygame.font.SysFont(None,48)
		
		#build button rect object
		self.rect=pygame.Rect(0,0,self.width,self.height)
		self.rect.center=self.screen_rect.center

		self.prep_msg(msg)
	
	def prep_msg(self,msg):
		self.msg_image=self.font.render(msg,True,self.text_colour)
		self.msg_image_rect=self.msg_image.get_rect()
		self.msg_image_rect.center=self.rect.center
	
	def draw_playbutton(self):
		self.screen.fill(self.button_colour,self.rect)
		self.screen.blit(self.msg_image,self.msg_image_rect)
