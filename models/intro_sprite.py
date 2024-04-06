from models.sprites.intro import Intro
from models.sprites_group import SpritesGroup

"""
Esta clase se manejara todos los sprites sobre la intro
 * agregar sprites en un grupo
 * mostrar los sprites en pantalla
"""  
class SpritesIntro(SpritesGroup):
  def __init__(self):
    super().__init__()
  
  def addIntroSprite(self, path_image, x, y):
    intro_sprite = Intro(path_image, x, y)
    self.addSpriteGroup(intro_sprite)
    return intro_sprite