import pygame

class ChannelRules:
  def __init__(self, id, volume=1):
    self.channel = pygame.mixer.Channel(id)
    self.volume = volume

  def play(self, sound, loop=0):
    self.channel.play(sound)

  def stop(self):
    self.channel.stop()

  def set_volume(self):
    self.channel.set_volume(self.volume)

