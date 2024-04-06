import pygame
from models.particle import Particle

class ParticleRule(Particle):
  def __init__(self, x, y, firework, colors):
    super(ParticleRule, self).__init__(x, y, firework, colors)

  def show(self, screen):
    pygame.draw.circle(screen, (self.color[0], self.color[1], self.color[2], 0), (int(self.pos.x), int(self.pos.y)),
                       self.size)