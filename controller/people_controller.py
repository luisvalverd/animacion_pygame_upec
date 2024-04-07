from controller.animation_controller import HandlerAnimation
from models.sprites.people import People # type: ignore

class PeopleEntranceAnimation(HandlerAnimation):
  def __init__(self, people: People, transition_speed = 15):
    super(PeopleEntranceAnimation, self).__init__()
    self.__peolple = people
    self.transition_speed = transition_speed

    self.__waiting_done = self._HandlerAnimation__waiting_done
    self.__animation_done = self._HandlerAnimation__animation_done
    self.__transition_done = self._HandlerAnimation__transition_done

  def waitingAnimation(self):
    if not self.__waiting_done:
      self.waiting_time -= 1
      if self.waiting_time <= 0:
        self.__waiting_done = True
    
    elif not self.__transition_done:
      self.__transition_done = self.updatePositionPeolpleEntranceSprite()

    self.stop()
  
  def updatePositionPeolpleEntranceSprite(self):
    self.__peolple.rect.y += self.transition_speed

     