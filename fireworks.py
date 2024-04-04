import random
import math
from config import *

class Fireworks:
  def __init__(self):
    self.__COLORS = [(255, 0, 0),
                     (255, 165, 0),
                     (255, 255, 0),
                     (0, 128, 0),
                     (0, 0, 255),
                     (75, 0, 130),
                     (238, 130, 238)]

    self.particles = []
    self.fireworks = []

  def createFirework(self):
    self.fireworks.append({
      "position": [random.randint(0, WIN_WIDTH), 0],
      "velocity": [random.uniform(-1, 1), random.uniform(1, 5)],
      "color": random.choice(self.__COLORS),
      "exploded": False
    })

  def explode(self, firework):
    num_particles = random.randint(50, 100)
    for _ in range(num_particles):
      angle = random.uniform(0, 2 * math.pi)
      speed = random.uniform(1, 5)
      color = random.choice(self.__COLORS)
      self.particles.append({"position": firework["position"].copy(),
                              "velocity": [speed * math.cos(angle), speed * math.sin(angle)],
                              "color": color,
                              "ttl": random.randint(20, 60)})


  def updateFirework(self, firework):
    if not firework['exploded']:
      firework['position'][0] += firework['velocity'][0]
      firework['position'][1] += firework['velocity'][1]
      firework['velocity'][1] -= 0.1 # Simula el efecto de la gravedad
      if firework['velocity'][1] <= 0:
        firework['exploded'] = True
        self.explode(firework)
