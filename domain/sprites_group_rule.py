from pygame.sprite import Sprite
from models.sprites_group import SpritesGroup
from models.validators.validation import ValidationError

"""
Esta funcion se manejara todos los sprites sobre la intro
 * agregar sprites en un grupo
"""  
def addSpriteAGroup(group: SpritesGroup, value: Sprite):
  if type(group) != SpritesGroup:
    return ValidationError("El grupo no coincide con el tipo esperado") 
  
  if not isinstance(value, Sprite):
    return ValidationError("El valor esperado del Sprite no valido")
  
  group.addSpriteGroup(value) 

  #return group

"""
Creacion de un grupo
"""
def createSpritesGroup():
  group = SpritesGroup()
  return group