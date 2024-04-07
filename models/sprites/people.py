import pygame
from domain.config import *


class People(pygame.sprite.Sprite):
  def __init__(self, image_path, x, y):
    super().__init__()
    self.image = pygame.image.load(image_path)
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)
    """
    self.rect.centerx = WIN_WIDTH // 2
    self.rect.bottom = WIN_HEIGHT
    """