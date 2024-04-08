import os
from models.sprites.people import People # type: ignore
from models.validators.validation import ValidationError
from controller.people_controller import PeopleEntranceAnimation # type: ignore

def createPeopleSprite(image_path, x, y):
  if not os.path.isfile(image_path):
    return ValidationError(f"Error archivo {image_path} no encontrado")

  if x < 0:
    return ValidationError(f"la posicion asignada de x no debe ser negativa")

  people_sprite = People(image_path, x, y)

  return people_sprite

def createAnimationPeopleEntrance(people_1: People, people_2: People,time_animation):
  people_entrance_animation = PeopleEntranceAnimation(people_1, people_2, duration_animation=3.2)
  people_entrance_animation.setTimeAnimation(time_animation)

  return people_entrance_animation

