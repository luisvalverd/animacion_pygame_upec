import pygame
from domain.config import *
from domain.intro_rule import createAnimation, createIntroSprite
from domain.sprites_group_rule import createSpritesGroup, addSpriteAGroup
from domain.firework import FireworkRules 
from domain.firework_rule import createFireworkAnimation # type: ignore
from domain.people_rule import createPeople, createAnimationPeopleEntrance
import random


class Game:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    self.clock = pygame.time.Clock()
    self.font = pygame.font.SysFont("micro", 27)
    self.running = True

    self.background = pygame.image.load("img/center_building.jpeg")
    self.screen.blit(self.background, (0, 0))

    # fuegos artificiales
    self.fireworks = [FireworkRules() for _ in range(4)]

    self.text_surface = self.font.render("Feliz Aniversario UPEC", True, (255, 255, 255))
    self.text_rect = self.text_surface.get_rect(center=(WIN_WIDTH/2, WIN_HEIGHT/2))  

    # sprites de intro
    self.sprites_intro_group = createSpritesGroup()
    self.logo_intro_1 = None
    self.logo_intro_2 = None

    # sprites de people
  

    #handlers
    self.handleSpriteIntro()
    self.handler_animation_intro = createAnimation(self.logo_intro_1, self.logo_intro_2, 2)
    self.handler_fireworks = createFireworkAnimation(self.fireworks, 5, self.screen)



  """
  maneja la construccion de los sprites 
  agrega los sprites de la intro a un grupo de sprites
  """
  def handleSpriteIntro(self):
    self.logo_intro_1 = createIntroSprite(LOGO_UPEC_LEFT, 0, 0)
    self.logo_intro_2 = createIntroSprite(LOGO_UPEC_RIGHT, WIN_WIDTH // 2 + 37, 0)
    addSpriteAGroup(self.sprites_intro_group, self.logo_intro_1)
    addSpriteAGroup(self.sprites_intro_group, self.logo_intro_2)

  def start(self):
    while self.running:
      self.clock.tick(60)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False

        # generar fuegos artificiales 
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_1:
            self.fireworks.append(FireworkRules()) 

          if event.key == pygame.K_2:
            for _ in range(7):
              self.fireworks.append(FireworkRules())

      if random.randint(0, 20) == 1:
        self.fireworks.append(FireworkRules())

      self.handler_fireworks.waitingAnimation()      



      self.screen.blit(self.background, (0, 0))
      # title
      self.screen.blit(self.text_surface, self.text_rect)  

      # maneja todo de la animacion
      self.handler_animation_intro.waitingAnimation()      

      if not self.handler_animation_intro.get_waiting_done():
        self.sprites_intro_group.showSprite(self.screen)

      pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
  game = Game() 
  game.start()