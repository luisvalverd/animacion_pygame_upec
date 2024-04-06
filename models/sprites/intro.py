import pygame
import os
from domain.config import *

"""
Clase del Sprite usado para la introduccion 
* tiene la ruta de la imagen para ser cargada y donde va estar ubicada
"""
class Intro(pygame.sprite.Sprite):
  def __init__(self, image_path, x, y):
    super().__init__()
    self.image = pygame.image.load(image_path)
    self.rect =  self.image.get_rect() # obtiene area rectangular del sprite
    self.rect.topleft = (x, y) # asignamos la posicion de la esquna superior
    self.transition_done = False





