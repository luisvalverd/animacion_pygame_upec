from unittest import TestCase

# modules de la introduccion
from controller.intro_controller import IntroAnimation
from animations.intro import Intro
from domain.config import *

class TestIntroAnimation(TestCase):
  def setUp(self):
    self.IntroAnimation = IntroAnimation(self.addClassCleanup, self.addClassCleanup)
  
  def test_intro_handler_waiting(self):
    self.assertEqual(self.IntroAnimation.waitingAnimation(), 0)

class TestIntro(TestCase):
  def setUp(self):
    self.intro = Intro(LOGO_UPEC_LEFT, 0, 0)

  def test_get_image(self):
    self.assertEqual(self.intro.image.get_rect().topleft, (0, 0), "Error al obtener las coordenadas superiores") 

  def tearDown(self):
    self.assertRaises(Intro("test.jpg", 0, 0))

  def test_transition_done(self):
    self.assertIsNotNone(self.intro.image, "Error no se encontro la imagen")

  
