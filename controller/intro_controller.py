from controller.animation_controller import HandlerAnimation 

class IntroAnimation(HandlerAnimation):
  # logo_1, logo_2 son los sprites para manejar su tiempo y posision
  def __init__(self, logo_left, logo_rigth):
    super(IntroAnimation, self).__init__()
    self.__logo_left = logo_left 
    self.__logo_rigth = logo_rigth

  def waitingAnimation(self): 
    return self.waiting_time
      


