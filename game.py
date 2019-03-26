import pygame
pygame.init()


window = pygame.display.set_mode((640,480))

pygame.display.set_caption("Asteroids")



def redrawGameWindow():
	#black = [0,0,0]
	#window.fill(black)
	pygame.draw.rect(window, (0, 0, 255), (ship.x, ship.y, ship.width, ship.height))
	pygame.display.update()

	for bullet in bullets:
		bullet.coverdraw(window)
		bullet.draw(window)



class Ship():
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = 8
		self.alive = True





class Projectile():
	def __init__(self,x,y,radius,color):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.vel = -10

	def coverdraw(self, window):
		pygame.draw.circle(window, (0,0,0), (self.x, self.y-self.vel), self.radius)

	def draw(self, window):
		pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)







#Main Loop

ship = Ship(320, 400, 50, 50)
bullets = []



run = True
while run:
	pygame.time.delay(100)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	for bullet in bullets:
		if bullet.y < 480 and bullet.y > 0:
			bullet.y += bullet.vel
		else:
			bullets.pop(bullets.index(bullet))


	keys = pygame.key.get_pressed()

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


	redrawGameWindow()






pygame.quit()