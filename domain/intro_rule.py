import os
from animations.intro import Intro
from models.validators.validation import ValidationError
from domain.config import WIN_WIDTH
from controller.intro_controller import IntroAnimation

def createIntroSprite(image_path, x, y):
  if not os.path.isfile(image_path):
    return ValidationError(f"archivo no encontrado en la ruta {image_path}")

  if x < 0 or y < 0:
    return ValidationError(f"la posicion asignada no debe ser negativa")
  
  intro_sprite = Intro(image_path, x, y)

  return intro_sprite

"""
* crea la clase de la animacion de la intro y devuelve el objeto
"""
def createAnimation(logo_sprite_left: Intro, logo_sprite_rigth: Intro, time_animation, transition_speed = 5):
  intro_animation = IntroAnimation(logo_sprite_left, logo_sprite_rigth, transition_speed)
  intro_animation.setTimeAnimation(time_animation)

  return intro_animation 