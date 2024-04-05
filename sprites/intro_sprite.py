from animations.intro import Intro
from types.sprites import Sprites

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