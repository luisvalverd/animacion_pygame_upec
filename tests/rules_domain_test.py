from unittest import TestCase, mock
from assertpy import assert_that

# libraries
from pygame.sprite import Sprite, Group

# modules
from domain import sprites_group_rule
from models.sprites_group import SpritesGroup
from models.validators.validation import ValidationError

# TODO hacer los test de las reglas de negocio de la intro


"""
* test de la reglas del negocio del manejo de los grupos de sprites

"""
class TestGroupRules(TestCase):

  @mock.patch.object(sprites_group_rule, "addIntroSpriteAGroup")
  def test_add_intro_sprite_group_is_called(self, mock_method):
    sprites_group_rule.addIntroSpriteAGroup(mock.MagicMock(spec=SpritesGroup), mock.MagicMock(spec=Sprite))
    
    assert_that(mock_method.assser_called).is_true()

  @mock.patch.object(Group, "sprites")
  def test_add_intro_sprite(self, mock_group):
    response = SpritesGroup()

    mock_group.return_value = ["sprite"]

    mock_sprite = mock.MagicMock(spec=Sprite)
    mock_sprite.return_value = "sprite"

    sprites_group_rule.addIntroSpriteAGroup(
      response, mock_sprite
    )

    assert_that(response.group.sprites()).is_equal_to(["sprite"])

  def test_get_exception_with_fail_group(self):

    mock_sprite = mock.MagicMock(spec=Sprite)

    error = sprites_group_rule.addIntroSpriteAGroup(
      None, mock_sprite
    )

    assert_that(error).is_type_of(ValidationError)

  @mock.patch.object(sprites_group_rule, "createSpritesGroup")
  def test_is_called_create_sprites_group(self, mock_method):
    sprites_group_rule.createSpritesGroup()

    assert_that(mock_method.called).is_true()

  def test_create_sprites_group(self):
    group = sprites_group_rule.createSpritesGroup()

    assert_that(group).is_type_of(SpritesGroup)

