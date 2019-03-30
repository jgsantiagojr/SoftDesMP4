import pygame
import asteroids
import rocks
import projectiles
import enemy

## global vairables
keys = pygame.key.get_pressed()
max_velocity = 40
min_velocity = 0
accel = .1
deaccel = .05
d_angle = 1
locations = [[a,b], [c,d], [e,f], [h,i], [j,k], [l,m], [n,o]]

def rotate(self, direction):
	##TODO: IMPLEMENT VISUAL ROTATION
	if direction == True:
		self.angle += d_angle
	else:
		self.angle -= d_angle

def accelerate(direction, self):
	if direction == True:
		if self.velocity <= max_velocity:
			self.velocity += accel
	else :
		if self.velocity >= min_velocity:
			self.velocity -= deaccel

def hyperdrive(ship, ):
	for x in locations:
		"""TODO: CHECK WHICH LOCATIONS CURRENTLY HAVE Asteroids
				SEND THE SHIP TO A RANDOM CURRENTLY EMPTY LOCATION
		 """


class Ship():
	def __init__(self, x = winL/2, y = winH/2, angle = 0, width = 5, vel = 0, alive = True ): ##UNTESTED
		self.x = x
		self.y = y
		self.angle = angle
		self.width = width
		self.vel = vel
		self.alive = alive

	def __str__(self): ##UNTESTED
		location = "Coordinates: (" + str(self.x) + "," + str(self.y) + ") \n"
		size = "Width: " + str(self.width) + "\n"
		speed = "Speed: " +  str(self.vel) + "\n"
		status = "Status: " + str(self.alive)
		return location + size + speed + status ##Printing important information

	##The points below are so wonky and complex, because I'm not sure if the screen sie is set yet, so I wanted to make sure it worked regardless.
	def draw_ship(self, points = [[(winH/2)+(winH*.05), winL/2], [(winH/2)-(winH*.01), (winL/2)-(winL*.01)], [(winH/2)-(winH*.01), (winL/2)-(winL*.01)]]): ##UNTESTED
		pygame.draw.polygon(screen, WHITE, points , self.width)

	def angle(self):
		if keys[pygame.k_RIGHT] :
			rotate(self.angle, True) #rotate to the right
		if keys[pygame.k_LEFT] :
			rotate(self.angle, False) #rotate to the left

	def thrust(self):
		if keys[pygame.k_UP] :
			accelerate(true, self)
		else :
			accelerate(false, self)

	def hyperdrive(self):
		if keys[pygame.k_DOWN] :
			hyperdrive(self)
		else:
			pass
	def shoot(self):
		if keys[pygame.K_SPACE] :
			pass

def update_ship(ship):
	ship.angle()
	ship.thrust()
	ship.hyperdrive()
	ship.shoot()
	pygame.draw.rect(window, (0, 0, 0), (ship.x, ship.y, ship.width, ship.height))
    ship.x += ship.vel
    pygame.draw.rect(window, (0, 0, 255), (ship.x, ship.y, ship.width, ship.height))
    pygame.display.update()



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

if keys[pygame.K_SPACE]:
    if len(bullets) < 5:
        bullets.append(Projectile(round(ship.x+ship.width//2), round(ship.y+ship.height//2), 6, (255,255,255)))
