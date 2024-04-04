from animations.intro import Intro
import pygame

class Sprites:
  def __init__(self):
    # grupo de sprites de la intro
    self.group = pygame.sprite.Group() 

  def addSpriteGroup(self, sprite):
    self.group.add(sprite) 

  def showSprite(self, screen):
    self.group.draw(screen)


"""
Esta clase se manejara todos los sprites sobre la intro
 * agregar sprites en un grupo
 * mostrar los sprites en pantalla
"""  
class SpritesIntro(Sprites):
  def __init__(self):
    super().__init__()
  
  def addIntroSprite(self, path_image, x, y):
    intro_sprite = Intro(path_image, x, y)
    self.addSpriteGroup(intro_sprite)
    return intro_sprite
