from random import uniform, randint
from models.fireworks import Firework # type: ignore
from domain.config import *

class FireworkRules(Firework):
  def __init__(self):
    super(FireworkRules, self).__init__()

  def update(self, screen):
    if not self.exploded:
      self.firework.applyForce(GRAVITY)
      self.firework.move()
      for tf in self.firework.trails:
        tf.show(screen)

      self.show(screen)

      if self.firework.velocity.y >= 0:
        self.exploded = True
        self.explode()

    else:
      for particle in self.particles:
        particle.applyForce(VECTOR(GRAVITY.x + uniform(-1, 1) / 20,
                                    GRAVITY.y / 2 + (randint(1, 8) / 100)))
      
        particle.move()
        for t in particle.trails:
          t.show(screen)

        particle.show(screen)

  def show(self, screen):
    pygame.draw.circle(screen, self.color, (int(self.firework.pos.x), int(self.firework.pos.y)),
                       self.firework.size)
    

def update(screen, fireworks):
  for fw in fireworks:
    fw.update(screen)
    if fw.remove():
      fireworks.remove(fw)

  pygame.display.update()