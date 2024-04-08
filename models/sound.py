import pygame
from domain.config import *

class Sound:
  def __init__(self, sound_path):
    pygame.mixer.init()
    pygame.mixer_music.load(sound_path)
  