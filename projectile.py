class Projectile():
	def __init__(self,x,y,radius,color):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.vel = -30

	def coverdraw(self, window):
		pygame.draw.circle(window, (0,0,0), (self.x, self.y-self.vel), self.radius)

	def draw(self, window):
		pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)
