from controller.animation_controller import HandlerAnimation
from models.sprites.people import People # type: ignore

class PeopleEntranceAnimation(HandlerAnimation):
  def __init__(self, people_1: People, people_2: People,transition_speed = 2, duration_animation=5):
    super(PeopleEntranceAnimation, self).__init__()
    self.__peolple_1 = people_1
    self.__peolple_2 = people_2
    self.transition_speed = transition_speed
    self.duration_animation = duration_animation * 60

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
    self.__peolple_1.rect.y -= self.transition_speed
    self.__peolple_2.rect.y -= self.transition_speed

    if self.duration_animation >= 0:
      self.duration_animation -= 1
      return False
    else:
      return True

     