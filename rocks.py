import pygame
from pygame.locals import*

import random
import math


# import controller as contr
import projectile as proj
import enemy
import rocks


pygame.init()


winH = 480
winL = 640 
window = pygame.display.set_mode((winL,winH))

pygame.display.set_caption("Asteroids")


rockimg = pygame.image.load('asteroid.jpg')




class Asteroid:
	def __init__(self, color):
		self.x = random.randint(0, winL)
		self.y = random.randint(0, winH)
		self.radius = 25
		self.color = color
		self.angle = random.randint(0, 360)
		self.velY = int(25 * math.cos(self.angle))
		self.velX = int(25 * math.sin(self.angle))
		self.size = 3


	def draw(self, window):
		#pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)
		window.blit(rockimg, (self.x, self.y))

class View:
	def __init__(self, model):
		self.model = model

	def redrawGameWindow(self):

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
			model.rocks.append(Asteroid((0,255,0)))

		view.redrawGameWindow()


	pygame.quit()



if __name__ == "__main__":
	
	startgame()




