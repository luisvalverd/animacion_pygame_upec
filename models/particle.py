from domain.config import *
from random import randint, choice, uniform
from models.trail import Trail # type: ignore
import math

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

  def applyForce(self, force):
    self.acceleration += force

  def move(self):
    if not self.firework:
      self.velocity.x *= 0.8
      self.velocity.y *= 0.8

    self.velocity += self.acceleration
    self.pos += self.velocity
    self.acceleration *= 0

    if self.life == 0 and not self.firework:
      distance = math.sqrt((self.pos.x - self.origin.x) ** 2 + (self.pos.y - self.origin.y) ** 2)
      if distance > self.explosion_radius:
        self.remove = True

    self.decay()
    self.trailUpdate()
    self.life += 1

  def decay(self):
    if 50 > self.life > 10:
      ran = randint(0, 30)

      if ran == 0:
        self.remove = True
    
    elif self.life > 50:
      ran = randint(0, 5)
      if ran == 0:
        self.remove = True

  def trailUpdate(self):
    self.prev_posx.pop()
    self.prev_posx.insert(0, int(self.pos.x))
    self.prev_posy.pop()
    self.prev_posy.insert(0, int(self.pos.y))

    for n, t in enumerate(self.trails):
      if t.dynamic:
        t.set_pos(self.prev_posx[n + DYNAIC_OFFSET], self.prev_posy[n + DYNAIC_OFFSET])
      else:
        t.set_pos(self.prev_posx[n + STATIC_OFFSET], self.prev_posy[n + STATIC_OFFSET])