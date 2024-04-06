import os
from models.sprites.intro import Intro
from models.validators.validation import ValidationError
from domain.config import WIN_WIDTH
from controller.intro_controller import IntroAnimation


"""
* creacion de los sprites de la intro Valida si las
rutas dados son validos si no devuelve un Error
"""
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
  intro_animation.setTimeAnimation(time_animation) # se agrega el tiempo de duracion en segundos de la animacion

  return intro_animation 