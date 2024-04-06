import pygame
from random import randint
from domain.config import *
from models.particle import Particle # type: ignore


class Firework:
  def __init__(self):
    self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
    self.colors = (
      (randint(0, 255), randint(0, 255), randint(0, 255)),
      (randint(0, 255), randint(0, 255), randint(0, 255)),
      (randint(0, 255), randint(0, 255), randint(0, 255))
    )
    self.firework = Particle(randint(0, WIN_WIDTH), WIN_HEIGHT, True, self.colors)
    self.exploded = False
    self.particles = []
    self.min_max_particles = VECTOR(200, 600)

  def explode(self):
    amount = randint(int(self.min_max_particles.x), int(self.min_max_particles.y))
    for _ in range(amount):
      self.particles.append(Particle(self.firework.pos.x, self.firework.pos.y, False, self.colors))

  def remove(self):
    if self.exploded:
      for p in self.particles:
        if p.remove is True:
          self.particles.remove(p)

      if len(self.particles) == 0:
        return True
      else:
        return False
