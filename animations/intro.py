import pygame
import os
from domain.config import *

class Intro(pygame.sprite.Sprite):
  def __init__(self, image_path, x, y):
    super().__init__()
    self.image = pygame.image.load(image_path)
    self.rect =  self.image.get_rect() # obtiene area rectangular del sprite
    self.rect.topleft = (x, y) # asignamos la posicion de la esquna superior
    self.transition_done = False

  def setTransitionDone(self, transition_done):
    self.transition_done = transition_done




