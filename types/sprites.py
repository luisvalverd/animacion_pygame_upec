import pygame

class Sprites:
  def __init__(self):
    # grupo de sprites de la intro
    self.group = pygame.sprite.Group() 

  def addSpriteGroup(self, sprite):
    self.group.add(sprite) 

  def showSprite(self, screen):
    self.group.draw(screen)


