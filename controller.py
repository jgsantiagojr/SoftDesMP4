import pygame
import math
import asteroids as astr
#import rocks
import projectile
import enemy

pygame.init()

##GOT FROM GITHUB --------------------https://github.com/aminb/asteroids/blob/master/game.py
def draw_centered(surface1, surface2, position):
    """Draw surface1 onto surface2 with center at position"""
    rect = surface1.get_rect()
    rect = rect.move(position[0]-rect.width//2, position[1]-rect.height//2)
    surface2.blit(surface1, rect)


def rotate_center(image, rect, angle):
	rotate_image = pygame.transform.rotate(image, angle)
	rotate_rect = rotate_image.get_rect(center=rect.center)
	return rotate_image, rotate_rect


## global vairables

max_velocity = .5
min_velocity = 0
accel = .01
d_angle = .5
locations = []
##[a,b], [c,d], [e,f], [h,i], [j,k], [l,m], [n,o]
def rotate(self, direction):
	##TODO: IMPLEMENT VISUAL ROTATION
	if direction == True:
		self.angle += d_angle
		# print('rotate right deep')
	else:
		self.angle -= d_angle
		# print('rotate left deep')
	print(self)
def accelerate(direction, self):
	if direction == True:
		if self.vel < max_velocity and self.vel > -max_velocity:
			self.vel += accel
			# print('accel deep')
	elif self.vel > min_velocity :
			self.vel -= ((math.e**self.vel))/((math.e**self.vel)+10) -.09
			# math.log(self.vel + 1)*.6
			# print('deaccel deep neg')
	elif self.vel < min_velocity :
			self.vel += ((math.e**self.vel))/((math.e**self.vel)+10) -.09
			# print('deaccel deep pos')

def hyperdrive(ship, ):
	for x in locations:
		"""TODO: CHECK WHICH LOCATIONS CURRENTLY HAVE Asteroids
				SEND THE SHIP TO A RANDOM Cwindow = pygame.display.set_mode((winL,winH))URRENTLY EMPTY LOCATION
		 """
		pass

class Ship():
	def __init__(self, winH, winL, window, image,  x = None, y = None , angle = 0, width = 10, height = 10, vel = 0, alive = True): ##UNTESTED
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
		self.hitbox = (self.x, self.y, self.width, self.height)
		self.winH = winH
		self.winL = winL
		self.window = window
		self.image = image

	def __str__(self): ##UNTESTED
		location = "Coordinates: (" + str(self.x) + "," + str(self.y) + ") \n"
		size = "Width: " + str(self.width) + "\n"
		speed = "Speed: " +  str(self.vel) + "\n"
		status = "Status: " + str(self.alive)
		angle = "Angle: " + str(self.angle) + "\n"

		return location + size + speed + status + angle ##Printing important information

	def draw(self): ##UNTESTED
		##pygame.draw.rect(screen, (250,250,250), (self.x, self.y, self.width, self.height))
		self.image, rect = rotate_center(self.image, self.image.get_rect(), self.angle)
		draw_centered(self.image, self.window, (self.x, self.y))
	def rotate(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_RIGHT] :
			rotate(self, True) #rotate to the right
			# print('rotate right')
		if keys[pygame.K_LEFT] :
			rotate(self, False) #rotate to the left
			# print('rotate left')

	def thrust(self):
		keys = pygame.key.get_pressed()
		open = True
		if keys[pygame.K_UP] :
			accelerate(True, self)
			# print('accel')
			open = False
		elif abs(self.vel) > 0 and open == True:
			accelerate(False, self)
			# print('deaccel')
		# print("OPEN>>>>>>>>>>><>>>>>>>>>>>>>>>>>>>>>>>>>>>>", open)


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

		# pygame.draw.rect(self.window, (0,0,0), (self.x, self.y, self.width, self.height))
		self.x += math.degrees(math.cos(self.angle)) * self.vel
		self.y += math.degrees(math.sin(self.angle)) * self.vel
		self.update_hitbox()
		#self.image = rot_center(self.image, self.angle)
		#self.draw()
		# pygame.display.update()
		return shots_fired
