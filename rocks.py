import pygame
from pygame.locals import*

import random
import math


# import controller as contr
import projectile as proj
import enemy
import rocks


pygame.init()


winH = 1080
winL = 1920
window = pygame.display.set_mode((winL,winH))

pygame.display.set_caption("Asteroids")


rockimg = pygame.image.load('asteroid.jpg')




class Asteroid:
	def __init__(self, size):
		self.x = random.randint(0, winL)
		self.y = random.randint(0, winH)

		self.angle = random.randint(0, 360)
		self.size = 3
		self.hit == False


		if self.size == 3:
			self.radius = 75

			self.velY = int(25 * math.cos(self.angle))
			self.velX = int(25 * math.sin(self.angle))

		if self.size == 2:
			self.radius = 50

			self.velY = int(35 * math.cos(self.angle + 90))
			self.velX = int(35 * math.sin(self.angle + 90))

		if self.size == 1:
			self.radius = 25

			self.velY = int(45 * math.cos(self.angle + 90))
			self.velX = int(45 * math.sin(self.angle + 90))




	def draw(self, window):
		pygame.draw.circle(window, (255,0,0), (self.x, self.y), self.radius)
		#window.blit(rockimg, (self.x, self.y))

	def hit(self):
		if rock.hit


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
			model.rocks.append(Asteroid(3))

		view.redrawGameWindow()


	pygame.quit()



if __name__ == "__main__":
	
	startgame()




