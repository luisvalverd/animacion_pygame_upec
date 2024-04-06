from unittest import TestCase
from assertpy import assert_that

# libraries
import pygame

# modules de la introduccion
from models.validators.validation import ValidationError
from domain.intro_rule import createIntroSprite
from domain.config import *

class TestIntroAnimation(TestCase):
  def test_get_exception_create_Intro_with_file_incorret(self):
    intro = createIntroSprite("test.png", 0, 0)
    assert_that(intro).is_type_of(ValidationError)
  
  def test_get_position_image(self):
    intro = createIntroSprite(LOGO_UPEC_LEFT, 0, 0)
    assert_that(intro.image.get_rect().topleft).is_equal_to((0, 0))

  def test_get_rect_of_image(sefl):
    intro = createIntroSprite(LOGO_UPEC_LEFT, 0, 0)
    assert_that(intro.rect).is_type_of(pygame.Rect)