from domain.config import *

class Trail:
  def __init__(self, n, size, dynamic):
    self.pos_in_line = n
    self.pos = VECTOR(-10, -10)
    self.dynamic = dynamic

    # determinamos el color y el trazo dinamico de la cola
    if self.dynamic:
      self.color = TRAIL_COLORS[n]
      self.size = int(size - n / 2)
    else:
      self.color = (255, 255, 255)
      self.size = size - 2
      if self.size < 0:
        self.size = 0

  def set_pos(self, x, y):
    self.pos = VECTOR(x, y)