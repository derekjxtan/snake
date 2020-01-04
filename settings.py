#a class to handle all settings

class Settings():
	
	def __init__(self):
		
		#display settings
		self.screen_width,self.screen_height=1200,600
		self.white=(255,255,255)
		self.black=(0,0,0)
		
		self.game_active=False
		
		self.points=0
		
