from config import *


class Particles:
  def __init__(self, x, y, firework, color):
    self.firework = firework
    self.position = vector(x, y)
    self.origin = vector(x, y)
    self.radius = 30
    self.remoce = False
    self.life = 0
    self.acc = vector(0, 0)

    # camino 
    self.trails = [] # camino de las particulas
    self.prev_posx = [-10] * 10
    