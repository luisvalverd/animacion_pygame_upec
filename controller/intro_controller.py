from controller.animation_controller import HandlerAnimation 
from models.sprites.intro import Intro
from domain.config import *

"""
IntroAnimation es la clase encargada de manejar la animacion de la introduccion
esta hereda de la clase manejadorea de animaciones (HandlerAnimation)
En este caso esta clase necesita de los 2 logos necesarios para realizar la animacion
* la velocidad de transicion por defecto es 5
"""
class IntroAnimation(HandlerAnimation):
  # logo_1, logo_2 son los sprites para manejar su tiempo y posision
  def __init__(self, logo_left: Intro, logo_rigth: Intro, transition_speed=5):
    super(IntroAnimation, self).__init__()
    self.__logo_left = logo_left 
    self.__logo_rigth = logo_rigth
    self.transition_speed = transition_speed

    # llamado de variables privadas
    self.__waiting_done = self._HandlerAnimation__waiting_done
    self.__animation_done = self._HandlerAnimation__animation_done
    self.__transition_done = self._HandlerAnimation__transition_done

  """
  Esta es la espera para realizar la animacion
  """
  def waitingAnimation(self): 
    if not self.__waiting_done:
      self.waiting_time -= 1
      if self.waiting_time <= 0:
        self.__waiting_done = True
        # Reiniciar la posicion de la intro

    elif not self.__transition_done:
      self.__transition_done = self.updatePositionIntroSprites()
    
    self.stop()

  """
    actualiza la posicion de los sprites y retorna el estado
    de la animacion
  """
  def updatePositionIntroSprites(self):
    self.__logo_left.rect.x -= (self.transition_speed + 1)
    self.__logo_rigth.rect.x += self.transition_speed

    if self.__logo_left.rect.x <= -37 and self.__logo_rigth.rect.x >= WIN_WIDTH:
      return True # retorno de estado de la animacion

    return False

