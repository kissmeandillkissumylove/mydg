import pygame     #import pygame
import random     #import random
import math        #improve our math



#sprites paths
floor1sprite = "dgfiles/floor1.png" #sprite for dg floor
#colors
almost_black = (30, 30, 30)




class Keyboard:
	'''keyboard class'''

	def __new__(cls, *args, **kwargs):
		'''set __new__ method'''
		print("call __new__ for object Keyboard")
		return super().__new__(cls) #return class link


	def __init__(self):
		'''set __init__ method'''
		print("call __init__ for object Keyboard")


	def __del__(self):
		'''set __del__ method'''
		print("call __del__ for object Keyboard")


	def check_keyboard(self):
		'''check keyboard events'''
		for event in pygame.event.get(): #player wanna leave game
			if event.type == pygame.QUIT:
				game.running = False



class Floor:
	'''class which drawing dungeon floor'''

	def __new__(cls, *args, **kwargs):
		'''set __new__ method'''
		print("call __new__ for object Floor")
		return super().__new__(cls) #return class link


	def __init__(self):
		'''set __init__ method'''
		print("call __init__ for object Floor")
		self.floor1 = pygame.image.load(floor1sprite) #load image for tileble floor
		self.floor1_size = 100 #image size (should be AxA)
		#number of columns to fill with sprites
		self.columns = (Screen.get_screen_width()) // self.floor1_size
		#number of rows to fill with sprites
		self.rows = (Screen.get_screen_height()) // self.floor1_size


	def __del__(self):
		'''set __del__ method'''
		print("call __del__ for object Floor")


	def draw_floor(self, surface):
		'''method for render floor'''
		for row in range(self.rows):
			for column in range(self.columns):
				surface.blit(self.floor1, (column*self.floor1_size + 4, row*self.floor1_size + 4))



class Screen:
	'''class for render main screen'''

	width = 608 # init main screen size
	height = 608

	def __new__(cls, *args, **kwargs):
		'''set __new__ method'''
		print("call __new__ for object Screen")
		return super().__new__(cls)  #return class link


	def __init__(self):
		'''set __init__ method'''
		print("call __init__ for object Screen")
		#make screen
		self.game_screen = pygame.display.set_mode((self.width, self.height))


	def __del__(self):
		'''set __del__ method'''
		print("call __del__ for object Screen")


	@classmethod
	def get_screen_width(cls):
		#get width of current main screen
		return cls.width


	@classmethod
	def get_screen_height(cls):
		#get width of current main screen
		return cls.height


	def get_screen(self):
		#get screen surface
		return self.game_screen



class Game:
	'''object which include game settings'''

	def __new__(cls, *args, **kwargs):
		'''set __new__ method'''
		print("call __new__ for object Game")
		return super().__new__(cls) #return class link


	def __init__(self):
		'''set __init__ method'''
		print("call __init__ for object Game")
		pygame.init() #init pygame
		self.running = True #flag for main loop


	def __del__(self):
		'''set __del__ method'''
		print("call __del__ for object Game")
		pygame.quit()


	def game_loop(self):
		#main loop
		obj_screen = Screen()
		obj_floor = Floor()
		obj_keyboard = Keyboard()
		obj_wall = Wall()

		while self.running:
			#keyboard
			obj_keyboard.check_keyboard()
			#rendering
			self.render_objects(obj_floor, obj_screen, obj_keyboard, obj_wall)
			#display update and fps
			pygame.display.update() #update display
			pygame.time.Clock().tick(60) #set 60 fps


	def render_objects(self, obj_floor, obj_screen, obj_keyboard, obj_wall):
		#function for rendering all sprites
		obj_floor.draw_floor(obj_screen.game_screen)
		obj_wall.draw_bariers(obj_screen.game_screen)




class Wall:
	'''class for walls'''

	def __new__(cls, *args, **kwargs):
		'''set __new__ method'''
		print("call __new__ for object Wall")
		return super().__new__(cls)  #return class link


	def __init__(self):
		'''set __init__ method'''
		print("call __init__ for object Wall")
		self.top_barier = pygame.Rect(0, 0, Screen.get_screen_width(), 4)
		self.bot_barier = pygame.Rect(0, Screen.get_screen_height()-4,
		                                        Screen.get_screen_width(), 4)
		self.left_barier = pygame.Rect(0, 0, 4, Screen.get_screen_height())
		self.right_barier = pygame.Rect(Screen.get_screen_width()-4, 0,
		                                        4, Screen.get_screen_height())


	def __del__(self):
		'''set __del__ method'''
		print("call __del__ for object Wall")


	def draw_bariers(self, surface):
		'''draw all screen borders'''
		pygame.draw.rect(surface, almost_black, self.top_barier)
		pygame.draw.rect(surface, almost_black, self.bot_barier)
		pygame.draw.rect(surface, almost_black, self.left_barier)
		pygame.draw.rect(surface, almost_black, self.right_barier)



game = Game()
game.game_loop()