import pygame
from models.trail import Trail

class TrailRules(Trail):
  def __init__(self, n , size, dynamic):
    super(TrailRules, self).__init__(n, size, dynamic)

  def show(self, screen):
    pygame.draw.circle(screen, self.color, (int(self.pos.x), int(self.pos.y)), self.size)