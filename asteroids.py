import pygame
import controller as contr
import projectile as proj


pygame.init()

winH = 500
winL = 450

window = pygame.display.set_mode((winL,winH))

pygame.display.set_caption("Asteroids")


class View:
	def __init__(self, model):
		self.model = model

	def redrawGameWindow(self):

		pygame.draw.rect(window, (0,0,0), (0, 0, winL, winH))

		for ship in self.model.ships:
			ship.draw(window)
			pygame.display.update()
		for bullet in self.model.bullets:
			bullet.draw()
			pygame.display.update()
		for rock in self.model.rocks:
			rock.draw(window)
			pygame.display.update()

class Model:
	def __init__(self):
		self.ships = [contr.Ship(winL = winL, winH = winH, window = window)]
		self.bullets = []
		self.rocks = []


def startgame():
	shot = 0

	model = Model()
	view = View(model)
	run = True
	while run:
		print("SHOT..................................................................................", shot)
		if shot > 0 and shot <= 5:
			shot += 1
		else :
			shot = 0
		pygame.time.delay(100)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		for ship in model.ships:
			shots_fired_ship = ship.update_ship()
			if shots_fired_ship == True and shot == 0 :
				bullet = proj.Projectile(round(ship.x), round(ship.y), 2, (250,250,250), ship.angle, ship.window, winL, winH)
				model.bullets.append(bullet)
				print('shots fired')
				shot += 1
		for bullet in model.bullets:
			bullet.update_projectile()
			print('bullet check :', bullet)
			if bullet.lifetime > 15 :
				model.bullets.pop(model.bullets.index(bullet))
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


		view.redrawGameWindow()


	pygame.quit()



if __name__ == "__main__":

	startgame()
