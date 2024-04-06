from pygame.sprite import Sprite
from models.sprites_group import SpritesGroup

"""
Esta funcion se manejara todos los sprites sobre la intro
 * agregar sprites en un grupo
"""  
def addIntroSpriteAGroup(group: SpritesGroup, value: Sprite):
  group.addSpriteGroup(value) 

"""
Creacion de un grupo
"""
def createSpritesGroup():
  group = SpritesGroup()
  return group