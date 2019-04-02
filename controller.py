import pygame
import math
import asteroids as astr
#import rocks
import projectile
import enemy

pygame.init()

## global vairables

max_velocity = .5
min_velocity = 0
accel = .01
d_angle = 1
locations = []
##[a,b], [c,d], [e,f], [h,i], [j,k], [l,m], [n,o]
def rotate(self, direction):
	##TODO: IMPLEMENT VISUAL ROTATION
	if direction == True:
		self.angle += d_angle
		print('rotate right deep')
	else:
		self.angle -= d_angle
		print('rotate left deep')
	print(self)
def accelerate(direction, self):
	if direction == True:
		if self.vel < max_velocity and self.vel > -max_velocity:
			self.vel += accel
			print('accel deep')
	elif self.vel > min_velocity :
			self.vel -= ((math.e**self.vel))/((math.e**self.vel)+10) -.09
			# math.log(self.vel + 1)*.6
			print('deaccel deep neg')
	elif self.vel < min_velocity :
			self.vel += ((math.e**self.vel))/((math.e**self.vel)+10) -.09
			print('deaccel deep pos')



	print(self)
def hyperdrive(ship, ):
	for x in locations:
		"""TODO: CHECK WHICH LOCATIONS CURRENTLY HAVE Asteroids
				SEND THE SHIP TO A RANDOM Cwindow = pygame.display.set_mode((winL,winH))URRENTLY EMPTY LOCATION
		 """
		pass

class Ship():
	def __init__(self, winH, winL, window, x = None, y = None , angle = 0, width = 30, height = 30, vel = 0, alive = True): ##UNTESTED
		if x == None :
			self.x = winL/2
		else:
			self.x = x
		if y == None :
			self.y = winH/2
		else:
			self.y = y
		self.angle = angle
		self.width = width
		self.height = height
		self.vel = vel
		self.alive = alive
		self.hitbox = (self.x, self.y, self.width)
		self.winH = winH
		self.winL = winL
		self.window = window

	def __str__(self): ##UNTESTED
		location = "Coordinates: (" + str(self.x) + "," + str(self.y) + ") \n"
		size = "Width: " + str(self.width) + "\n"
		speed = "Speed: " +  str(self.vel) + "\n"
		status = "Status: " + str(self.alive)
		angle = "Angle: " + str(self.angle) + "\n"

		return location + size + speed + status + angle ##Printing important information

	def draw(self, screen): ##UNTESTED
		pygame.draw.rect(screen, (250,250,250), (self.x, self.y, self.width, self.height))

	def rotate(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_RIGHT] :
			rotate(self, True) #rotate to the right
			print('rotate right')
		if keys[pygame.K_LEFT] :
			rotate(self, False) #rotate to the left
			print('rotate left')

	def thrust(self):
		keys = pygame.key.get_pressed()
		open = True
		if keys[pygame.K_UP] :
			accelerate(True, self)
			print('accel')
			open = False
		elif abs(self.vel) > 0 and open == True:
			accelerate(False, self)
			print('deaccel')
		print("OPEN>>>>>>>>>>><>>>>>>>>>>>>>>>>>>>>>>>>>>>>", open)


	def hyperdrive(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_DOWN] :
			hyperdrive(self)
		else:
			pass

	def shoot(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE] :
			return True

	def update_hitbox(self):
		self.hitbox = (self.x, self.y, self.width, self.height)

	def update_ship(self):
		keys = pygame.key.get_pressed()
		self.rotate()
		self.thrust()
		shots_fired = self.shoot()
		if self.x > self.winL :
			self.x = 0
		if self.x < 0 :
			self.x = self.winL
		if self.y > self.winH :
			self.y = 0
		if self.y < 0 :
			self.y = self.winH

		pygame.draw.rect(self.window, (0, 0, 0), (self.x, self.y, self.width, self.height))
		self.x += math.degrees(math.cos(self.angle)) * self.vel
		self.y += math.degrees(math.sin(self.angle)) * self.vel
		self.update_hitbox()
		pygame.draw.rect(self.window, (250, 250, 250), (self.x, self.y, self.width, self.height))
		pygame.display.update()
		return shots_fired


"""
if keys[pygame.K_LEFT] and ship.x > 0:
    pygame.draw.rect(window, (0, 0, 0), (ship.x, ship.y, ship.width, ship.height))
    ship.x -= ship.vel
    pygame.draw.rect(window, (0, 0, 255), (ship.x, ship.y, ship.width, ship.height))
    pygame.display.update()


if keys[pygame.K_RIGHT] and ship.x < 590:
    pygame.draw.rect(window, (0, 0, 0), (ship.x, ship.y, ship.width, ship.height))
    ship.x += ship.vel
    pygame.draw.rect(window, (0, 0, 255), (ship.x, ship.y, ship.width, ship.height))
    pygame.display.update()


if keys[pygame.K_UP] and ship.y > 0:
    pygame.draw.rect(window, (0, 0, 0), (ship.x, ship.y, ship.width, ship.height))
    ship.y -= ship.vel
    pygame.draw.rect(window, (0, 0, 255), (ship.x, ship.y, ship.width, ship.height))
    pygame.display.update()


if keys[pygame.K_DOWN] and ship.y < 430:
    pygame.draw.rect(window, (0, 0, 0), (ship.x, ship.y, ship.width, ship.height))
    ship.y += ship.vel
    pygame.draw.rect(window, (0, 0, 255), (ship.x, ship.y, ship.width, ship.height))
    pygame.display.update()
"""
