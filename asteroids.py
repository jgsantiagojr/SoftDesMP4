import pygame
import controller as contr
import projectile as proj
import rocks


pygame.init()

winH = 1000
winL = 900

window = pygame.display.set_mode((winL,winH))

ship_img = pygame.image.load('ship.png')
ship_img.convert()
ship_img = pygame.transform.scale(ship_img, (15,15))
asteroid1 = pygame.image.load('asteroid1.png')
asteroid1.convert()
asteroid2 = pygame.image.load('asteroid1.png')
asteroid2.convert()
asteroid3 = pygame.image.load('asteroid1.png')
asteroid3.convert()

pygame.display.set_caption("Asteroids")


class View:
	def __init__(self, model):
		self.model = model

	def redrawGameWindow(self):

		pygame.draw.rect(window, (0,0,0), (0, 0, winL, winH))

		for ship in self.model.ships:
			ship.draw()
			pygame.display.update()
		for bullet in self.model.bullets:
			bullet.draw()
			pygame.display.update()
		for rock in self.model.rocks:
			rock.draw(window)
			pygame.display.update()

class Model:
	def __init__(self):
		self.ships = [contr.Ship(winL = winL, winH = winH, window = window, image = ship_img)]
		self.bullets = []
		self.rocks = []
	def reset(self):
		self.ships = [contr.Ship(winL = winL, winH = winH, window = window, image = ship_img)]
		self.bullets = []
		self.rocks = []
	def blank(self):
		self.ships = []
		self.bullets = []
		self.rocks = []

def startgame():
	shot = 0
	rock_timer = -1
	model = Model()
	view = View(model)
	ship = model.ships[0]
	run = True
	score = 0
	lives = 3
	bullet_pop = False
	while run and lives > 0:
		while(rock_timer > 0):
			rock_timer -= 1
		if(rock_timer == 0):
			model.rocks.append(rocks.Asteroid_Big(window, winH, winL, image = asteroid3))
			model.rocks.append(rocks.Asteroid_Big(window, winH, winL, image = asteroid3))
			model.rocks.append(rocks.Asteroid_Big(window, winH, winL, image = asteroid3))
			model.rocks.append(rocks.Asteroid_Big(window, winH, winL, image = asteroid3))
			rock_timer = -1

		if shot > 0 and shot <= 5:
			shot += 1
		else :
			shot = 0
		pygame.time.delay(100)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		for rock in model.rocks:
			rock.update_rock()
			if(rock.x + rock.radius < ship.hitbox[0] + ship.hitbox[2] and rock.x + rock.radius > ship.hitbox[0]):
				if(rock.y + rock.radius < ship.hitbox[1] + ship.hitbox[3] and rock.y + rock.radius < ship.hitbox[1]):
					model.ships.pop(model.ships.index(ship))
					lives -= 1
					model.ships.append(contr.Ship(winL = winL, winH = winH, window = window, image = ship_img))
					ship = model.ships[0]

		shots_fired_ship = ship.update_ship()
		if shots_fired_ship == True and shot == 0 :
			bullet = proj.Projectile(round(ship.x), round(ship.y), 2, (250,250,250), ship.angle, ship.window, winL, winH)
			model.bullets.append(bullet)
			shot += 1

		for bullet in model.bullets:
			bullet.update_projectile()
			# print('bullet check :', bullet)
			if bullet.lifetime > 15 :
				model.bullets.pop(model.bullets.index(bullet))
			for rock in model.rocks:
				if(bullet.x + bullet.radius < rock.hitbox[0] + rock.hitbox[2] and bullet.x + bullet.radius > rock.hitbox[0]):
					if(bullet.y + bullet.radius < rock.hitbox[1] + rock.hitbox[2] and bullet.y + bullet.radius > rock.hitbox[1]):
						size = rock.hit()
						if size == 3:
							score += 10
							model.rocks.append(rocks.Asteroid_Med(window, winH, winL, rock.x, rock.y, image = asteroid2))
							model.rocks.append(rocks.Asteroid_Med(window, winH, winL, rock.x, rock.y, image = asteroid2))
						elif size == 2:
							score += 25
							model.rocks.append(rocks.Asteroid_Small(window, winH, winL, rock.x, rock.y, image = asteroid1))
							model.rocks.append(rocks.Asteroid_Small(window, winH, winL, rock.x, rock.y, image = asteroid1))
						elif size == 1:
							score += 50
						model.rocks.pop(model.rocks.index(rock))
						bullet_pop = True
				if bullet_pop == True:
					model.bullets.pop(model.bullets.index(bullet))
					bullet_pop = False
		if not model.rocks:
			rock_timer = 4


		keys = pygame.key.get_pressed()


		view.redrawGameWindow()


	pygame.display.update()

	pygame.quit()


if __name__ == "__main__":

	startgame()
