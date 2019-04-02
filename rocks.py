import pygame
from pygame.locals import*

import random
import math


# import controller as contr
import projectile as proj
import enemy
import rocks

'''
Initialize pygame, screen, and load images
'''

pygame.init()


winH = 1080
winL = 1920
window = pygame.display.set_mode((winL,winH))

pygame.display.set_caption("Asteroids")


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
	def __init__(self):
		self.x = random.randint(0, winL)
		self.y = random.randint(0, winH)

		self.angle = random.randint(0, 360)
		self.hit == False

		self.radius = 75

		self.velY = int(25 * math.cos(self.angle))
		self.velX = int(25 * math.sin(self.angle))
		# self.image = rockimg3

		self.hitbox = (self.x, self.y, self.x + self.radius, self.y + self.radius)




	def draw(self, window):
		'''
		Draws the Asteroid object correspoinding to its size on the window surface
		'''
		pygame.draw.circle(window, (255,0,0), (self.x, self.y), self.radius)
		#window.blit(self.image, (self.x, self.y))

	def hit(self):
		#TODO IMPLEMENT COLLISION BETWEEN PROJECTILES AND ASTEROIDS
		pass



class Asteroid_Med:
	'''
	Creating the Asteroid Big Class
		- x and y determine the position of the object on the screen
		- angle is the trajectory at which the asteroid is launched
		- Medium size and speed
	'''
	def __init__(self, x, y):
		self.x = random.randint(0, winL)
		self.y = random.randint(0, winH)

		self.angle = random.randint(0, 360)
		self.hit == False

		self.radius = 50

		self.velY = int(35 * math.cos(self.angle + 90))
		self.velX = int(35 * math.sin(self.angle + 90))
		# self.image = rockimg2

		self.hitbox = (self.x, self.y, self.x + self.radius, self.y + self.radius)

	def draw(self, window):
		'''
		Draws the Asteroid object correspoinding to its size on the window surface
		'''
		pygame.draw.circle(window, (255,0,0), (self.x, self.y), self.radius)
		#window.blit(self.image, (self.x, self.y))

	def hit(self):
		#TODO IMPLEMENT COLLISION BETWEEN PROJECTILES AND ASTEROIDS
		pass



class Asteroid_Small:
	'''
	Creating the Asteroid Big Class
		- x and y determine the position of the object on the screen
		- angle is the trajectory at which the asteroid is launched
		- Smallest and fastest type
	'''
	def __init__(self, x, y):
		self.x = random.randint(0, winL)
		self.y = random.randint(0, winH)

		self.angle = random.randint(0, 360)
		self.hit == False

		self.radius = 25

		self.velY = int(45 * math.cos(self.angle + 90))
		self.velX = int(45 * math.sin(self.angle + 90))
		# self.image = rockimg1

		self.hitbox = (self.x, self.y, self.x + self.radius, self.y + self.radius)

	def draw(self, window):
		'''
		Draws the Asteroid object correspoinding to its size on the window surface
		'''
		pygame.draw.circle(window, (255,0,0), (self.x, self.y), self.radius)
		#window.blit(self.image, (self.x, self.y))

	def hit(self):
		#TODO IMPLEMENT COLLISION BETWEEN PROJECTILES AND ASTEROIDS
		pass










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
<<<<<<< HEAD

	startgame()
"""
=======
	
	startgame()
>>>>>>> b02601be0277cc7999895b00017c2cc15af94121
