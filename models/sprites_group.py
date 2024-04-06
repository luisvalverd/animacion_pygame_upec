import pygame

"""
Clase base para manejar cada grupo de animacion de los sprites
"""
class SpritesGroup:
  def __init__(self):
    # grupo de sprites de la intro
    self.group = pygame.sprite.Group() 

  # agrega a un grupo de sprites
  def addSpriteGroup(self, sprite):
    self.group.add(sprite) 

  # muestra por pantalla los sprites
  def showSprite(self, screen):
    self.group.draw(screen)

  def clearSprites(self):
    self.group.empty()
