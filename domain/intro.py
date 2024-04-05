import os
from animations.intro import Intro

def createIntroSprite(image_path, x, y):
  if not os.path.isfile(image_path):
    return Exception # TODO make a custom Exception

  if x < 0 or y < 0:
    return Exception # TODO make a custom Exception to handler Sprite
  
  intro_sprite = Intro(image_path, x, y)

  return intro_sprite
  