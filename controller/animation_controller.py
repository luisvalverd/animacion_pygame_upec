from domain.config import *

class HandlerAnimation:
  def __init__(self):
    self.waiting_time= 0 # los frames de espera de la animacion
    self.__animation_done = False
    self.__waiting = False 

  def stop(self):
    self.__animation_done = True
    return self.__animation_done

  # transformamos los segundos a fotogramas
  def setTimeAnimation(self, waiting_time):
    self.waiting_time = waiting_time* 60
      