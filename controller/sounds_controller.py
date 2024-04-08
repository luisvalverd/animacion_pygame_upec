import pygame

class SoundController:
  def __init__(self, channel, sound, duration_sound, waiting_time):
    self.waiting_time = waiting_time * 60
    self.__waiting_done = False
    self.__transition_done = False
    self.sound = sound
    self.duration_sound = duration_sound * 60
    self.channel = channel
    self.__is_stop = False

  def set_volume(self, volume):
    pygame.mixer.Channel(self.channel).set_volume(volume)

  def setTimeSound(self, waiting_time):
    self.waiting_time = waiting_time * 60

  def waitingSound(self):
    if not self.__is_stop:
      if not self.__waiting_done:
        self.waiting_time -= 1
        if self.waiting_time <= 0:
          self.__waiting_done = True

      elif not pygame.mixer.Channel(self.channel).get_busy():
        pygame.mixer.Channel(self.channel).play(self.sound)
      elif not self.__transition_done:
        self.__transition_done = self.updateTimeDuration()
      elif self.__transition_done:
        self.stop()

  def updateTimeDuration(self):
    if self.duration_sound >= 0:
      self.duration_sound -= 1
      return False
    else:
      return True

  def stop(self):
    pygame.mixer.Channel(self.channel).stop()
    self.__is_stop = True

  def is_bussy(self):
    return pygame.mixer.Channel(self.channel).get_busy()