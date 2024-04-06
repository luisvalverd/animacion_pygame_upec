from domain.config import *

"""
Clase base manejadora de las animaciones
! __waiting_done verifica si la animacion ya realizo su tiempo de espera
! __transition_done verifica si la transicion de la animacion esta hecha
! __animation_done verifica si ya fue realizada, si esta fue realizada se para la animacion 
"""
class HandlerAnimation:
  def __init__(self):
    self.waiting_time= 0 # los frames de espera de la animacion
    self.__waiting_done = False
    self.__transition_done = False
    self.__animation_done = False

  def get_waiting_done(self):
    return self.__waiting_done

  # transformamos los segundos a fotogramas
  def setTimeAnimation(self, waiting_time):
    self.waiting_time = waiting_time * 60

  # detener la animacion
  def stop(self):
    if self.__transition_done and not self.__animation_done:
      self.__animation_done = True
      