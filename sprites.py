from animations.intro import Intro
import pygame

class Sprites:
  def __init__(self):
    # grupo de sprites de la intro
    self.intro_group = pygame.sprite.Group() 

    
  
  def addIntro(self, path_image, x, y):
    intro_sprite = Intro(path_image, x, y)
    self.addSpriteIntroGroup(intro_sprite)

    return intro_sprite

  def addSpriteIntroGroup(self, sprite):
    self.intro_group.add(sprite) 

  def showSpriteIntro(self, screen):
    self.intro_group.draw(screen)