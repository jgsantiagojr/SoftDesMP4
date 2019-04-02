import pygame
from pygame.locals import*
import math
import random


# import controller as contr
import projectile as proj
import enemy
import rocks

'''
Initialize pygame, screen, and load images
'''

pygame.init()
# rockimg3 = pygame.image.load('asteroid3.jpg')
# rockimg2 = pygame.image.load('asteroid2.jpg')
# rockimg1 = pygame.image.load('asteroid1.jpg')



class Asteroid_Big:
	'''
	Creating the Asteroid Big Class
		- x and y determine the position of the object on the screen
		- angle is the trajectory at which the asteroid is launched
		- Biggest and slowest type
	'''
	def __init__(self,  window, winH, winL, image, sides = [1,2]):
		c_side = random.choice(sides)
		if c_side == 1:
			self.x = random.randint(0, winL)
			self.y = 0
		if c_side == 2:
			self.x = 0
			self.y = random.randint(0, winH)

		self.window = window
		self.winH = winH
		self.winL = winL
		self.angle = random.randint(0, 360)
		self.hit == False

		self.radius = 30

		self.velY = int(.05 * math.degrees(math.cos(self.angle)))
		self.velX = int(.05 * math.degrees(math.sin(self.angle)))
		self.image = image

		self.hitbox = (self.x, self.y, self.x + self.radius, self.y + self.radius)

	def draw(self, window):
		'''
		Draws the Asteroid object correspoinding to its size on the window surface
		'''
		#pygame.display(self.image, self.x, self.y)
		self.window.blit(self.image, (self.x, self.y))

	def hit(self):
		#TODO IMPLEMENT COLLISION BETWEEN PROJECTILES AND ASTEROIDS
		print('HIT')
		return 3

	def update_rock(self):
		self.y += self.velY
		self.x += self.velX
		if self.x > self.winL :
			self.x = 0
		if self.x < 0 :
			self.x = self.winL
		if self.y > self.winH :
			self.y = 0
		if self.y < 0 :
			self.y = self.winH

class Asteroid_Med:
	'''
	Creating the Asteroid Big Class
		- x and y determine the position of the object on the screen
		- angle is the trajectory at which the asteroid is launched
		- Medium size and speed
	'''
	def __init__(self, window,  winH, winL, x, y, image):
		self.x = x
		self.y = y

		self.window = window
		self.winH = winH
		self.winL = winL

		self.angle = random.randint(0, 360)
		self.hit == False

		self.radius = 17

		self.velY = int(.05 * math.degrees(math.cos(self.angle)))
		self.velX = int(.05 * math.degrees(math.sin(self.angle)))
		self.image = image

		self.hitbox = (self.x, self.y, self.x + self.radius, self.y + self.radius)

	def draw(self, window):
		'''
		Draws the Asteroid object correspoinding to its size on the window surface
		'''
		#pygame.draw.circle(self.window, (255,0,0), (self.x, self.y), self.radius)
		self.window.blit(self.image, (self.x, self.y))
	def hit(self):
		#TODO IMPLEMENT COLLISION BETWEEN PROJECTILES AND ASTEROIDS
		print('HIT')
		return 2

	def update_rock(self):
		self.y += self.velY
		self.x += self.velX
		if self.x > self.winL :
			self.x = 0
		if self.x < 0 :
			self.x = self.winL
		if self.y > self.winH :
			self.y = 0
		if self.y < 0 :
			self.y = self.winH

class Asteroid_Small:
	'''
	Creating the Asteroid Big Class
		- x and y determine the position of the object on the screen
		- angle is the trajectory at which the asteroid is launched
		- Smallest and fastest type
	'''
	def __init__(self, window, winH, winL, x, y, image):
		self.x = x
		self.y = y

		self.window = window
		self.winH = winH
		self.winL = winL

		self.angle = random.randint(0, 360)
		self.hit == False

		self.radius = 9

		self.velY = int(.05 * math.degrees(math.cos(self.angle)))
		self.velX = int(.05 * math.degrees(math.sin(self.angle)))
		self.image = image

		self.hitbox = (self.x, self.y, self.x + self.radius, self.y + self.radius)

	def draw(self, window):
		'''
		Draws the Asteroid object correspoinding to its size on the window surface
		'''
		#pygame.draw.circle(self.window, (255,0,0), (self.x, self.y), self.radius)
		self.window.blit(self.image, (self.x, self.y))

	def hit(self):
		#TODO IMPLEMENT COLLISION BETWEEN PROJECTILES AND ASTEROIDS
		print('HIT')
		return 1

	def update_rock(self):
		self.y += self.velY
		self.x += self.velX
		if self.x > self.winL :
			self.x = 0
		if self.x < 0 :
			self.x = self.winL
		if self.y > self.winH :
			self.y = 0
		if self.y < 0 :
			self.y = self.winH










class View:
	def __init__(self, model):
		self.model = model

	def redrawGameWindow(self):
		'''
		Create the game window, color the background black, and draw each rock object
		'''

		pygame.draw.rect(window, (0,0,0), (0, 0, winL, winH))

		for rock in self.model.rocks:
			rock.draw(window)
			pygame.display.update()



class Model:
	def __init__(self):
		self.rocks = []

def startgame():


	model = Model()
	view = View(model)

	run = True
	while run:
		pygame.time.delay(100)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		for rock in model.rocks:
			if rock.hit == True:
				model.rocks.pop(rock)
			if rock.y < winH and rock.y > 0:
				rock.y += rock.velY
			if rock.x < winL and rock.y > 0:
				rock.x += rock.velX
			else:
				if rock.y >= winH:
					rock.y = 1
				elif rock.y <= 0:
					rock.y = winH-10
				elif rock.x >= winL:
					rock.x = 1
				elif rock.x <= 0:
					rock.x = winL-10




		keys = pygame.key.get_pressed()

		if keys[pygame.K_a]:
			model.rocks.append(Asteroid_Big())

		if keys[pygame.K_s]:
			model.rocks.append(Asteroid_Med(255, 255))

		if keys[pygame.K_d]:
			model.rocks.append(Asteroid_Small(255, 255))


		view.redrawGameWindow()


	pygame.quit()


"""
if __name__ == "__main__":

	startgame()
"""
