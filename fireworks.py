from random import randint
import math
from config import *

class Fireworks:
  def __init__(self):
    self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
    self.colors = (
      (randint(0, 255), randint(0, 255), randint(0, 255), randint(0, 255), randint(0, 255),
      (randint(0, 255)), randint(0, 255), randint(0, 255)))
    self.firework = Particle(randint(0, WIN_WIDTH), WIN_HEIGHT, True,
                             self.color)
    
    self.exploded = False
    self.particles = []
    self.amount_particle = vector(200, 600)
  
  def update(self, win):
    if not self.exploded:
      self.firework.appl


