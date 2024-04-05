from types.config import *

class HandlerTimeAnimation:
  def __init__(self, time_animation):
    self.time_animation = time_animation # los frames de la animacion
    self.animation_done = False

  def timeAnimation(self):
    if not self.animation_done:
      self.time_animation -= 1
      if self.time_animation <= 0:
        self.animation_done = True
        # reiniciar posicion de los sprites 