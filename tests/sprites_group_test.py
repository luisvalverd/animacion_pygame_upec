from unittest import TestCase, mock 
from assertpy import assert_that
from pygame.sprite import Group, Sprite 
from pygame.surface import Surface


# modules
from models.sprites_group import SpritesGroup
from domain.config import *
from models.sprites.intro import Intro

class TestSpritesGroup(TestCase):
  def setUp(self):
    self.mock_screen = mock.MagicMock(spec=Surface)

  @mock.patch.object(Group, "sprites")
  def test_get_sprites_of_group(self, mock_group):
    mock_group.return_value = ["sprite 1", "sprite 2"]
    response = SpritesGroup().group.sprites()
    assert_that(response).is_equal_to(["sprite 1", "sprite 2"])

  def test_add_sprite_of_group(self):
    mock_group = SpritesGroup()

    # simulacion de sprite
    sprite = mock.MagicMock(spec=Sprite)

    mock_group.addSpriteGroup(sprite)

    #self.assertTrue(sprite in mock_group.group.sprites())
    assert_that(mock_group.group.sprites()).contains(sprite)

  @mock.patch.object(SpritesGroup, "showSprite")
  def test_show_sprite(self, mock_method):

    SpritesGroup.showSprite(self.mock_screen) # mostrar pantalla

    assert_that(mock_method.called).is_true() # revisar si el metodo es llamado correctamente

  @mock.patch.object(Group, "sprites")
  def test_clear_sprites_of_group(self, mock_group):
    mock_group.return_value = []


    response = SpritesGroup()
     
    mock_sprite_1 = mock.MagicMock(spec=Sprite)
    mock_sprite_2 = mock.MagicMock(spec=Sprite)

    response.addSpriteGroup(mock_sprite_1)
    response.addSpriteGroup(mock_sprite_2)

    response.clearSprites()

    response = response.group.sprites()

    assert_that(response).is_equal_to([])

  @mock.patch.object(SpritesGroup, "clearSprites")
  def test_call_clear_sprites_method_of_sprites_group(self, mock_method):
    SpritesGroup().clearSprites()

    assert_that(mock_method.called).is_true()