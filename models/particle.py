from domain.config import *
from random import randint, choice, uniform
from models.trail import Trail

class Particle:
  def __init__(self, x, y, firework, colors):
    self.firework = firework
    self.pos = VECTOR(x, y)
    self.origin = VECTOR(x, y)
    self.radius = 30
    self.remove = False
    self.explosion_radius = randint(5, 40)
    self.life = 0
    self.acceleration = VECTOR(0, 0)
    self.trails = []
    self.prev_posx = [-10] * 10
    self.prev_posy = [-10] * 10

    # configurar la particula si es de un fuego artificial
    if self.firework:
      self.velocity = VECTOR(0, -randint(17, 20))
      self.size = 5
      self.color = choice(colors)
      for i in range(5):
        self.trails.append(Trail(i, self.size, True))

    # configurarion de la particula en caso de ser de una explocion
    else:
      self.velocity = VECTOR(uniform(-1, 1), uniform(-1, 1))
      self.velocity.x *= randint(7, self.explosion_radius + 2)
      self.velocity.y *= randint(7, self.explosion_radius + 2)
      self.size = randint(2, 4)
      self.color = choice(colors)
      for i in range(5):
        self.trails.append(Trail(i, self.size, False))

  def apply_force(self, force):
    self.acceleration += force
