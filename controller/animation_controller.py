from domain.config import *

class HandlerAnimation:
  def __init__(self):
    self.waiting_time= 0 # los frames de espera de la animacion
    self.__waiting_done = False
    self.__transition_done = False
    self.__animation_done = False

  def stop(self):
    self.__waiting_done= True
    return self.__waiting_done

  # transformamos los segundos a fotogramas
  def setTimeAnimation(self, waiting_time):
    self.waiting_time = waiting_time * 60
      