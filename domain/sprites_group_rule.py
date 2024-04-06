from pygame.sprite import Sprite
from models.sprites_group import SpritesGroup
from models.validators.validation import ValidationError

"""
Esta funcion se manejara todos los sprites sobre la intro
 * agregar sprites en un grupo
"""  
def addIntroSpriteAGroup(group: SpritesGroup, value: Sprite):
  if not isinstance(group, type(SpritesGroup)):
    return ValidationError("El grupo no coincide con el tipo esperado") 
  
  if not isinstance(value, type(Sprite)):
    return ValidationError("El valor esperado del Sprite no valido")
  
  group.addSpriteGroup(value) 

"""
Creacion de un grupo
"""
def createSpritesGroup():
  group = SpritesGroup()
  return group