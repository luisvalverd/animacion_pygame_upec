from controller.animation_controller import HandlerAnimation 
from domain.firework import FireworkRules, update
from typing import List

class FireworkAnimation(HandlerAnimation):
  def __init__(self, fireworks: List[FireworkRules], transition_speed, screen):
    super(FireworkAnimation, self).__init__()
    self.__fireworks = fireworks
    self.transition_speed = transition_speed
    self.screen = screen

    # llamado de variables privadas
    self.__waiting_done = self._HandlerAnimation__waiting_done
    self.__animation_done = self._HandlerAnimation__animation_done
    self.__transition_done = self._HandlerAnimation__transition_done

  def waitingAnimation(self):
    if not self.__waiting_done:
      self.waiting_time -= 1
      if self.waiting_time <= 0:
        self.__waiting_done = True

    elif not self.__transition_done:
      self.__transition_done = self.updatePositionFirework()

    self.stop()

  def updatePositionFirework(self):
    update(self.screen, self.__fireworks)
    

