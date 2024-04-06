import pygame
from domain.config import *
from domain.intro_rule import createAnimation, createIntroSprite
from domain.sprites_group_rule import createSpritesGroup
import random
from fireworks import Fireworks

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
    self.fireworks = Fireworks()

    self.text_surface = self.font.render("Feliz Aniversario UPEC", True, (255, 255, 255))
    self.text_rect = self.text_surface.get_rect(center=(WIN_WIDTH/2, WIN_HEIGHT/2))  

    # sprites of intro
    self.sprites_intro_group = createSpritesGroup()
    self.logo_intro_1 = None
    self.logo_intro_2 = None

    #handlers
    self.handleSpriteIntro()
    self.handler_animation_intro = createAnimation(self.logo_intro_1, self.logo_intro_2, 2)
  

  """
  maneja la construccion de los sprites 
  agrega los sprites de la intro a un grupo de sprites
  """
  def handleSpriteIntro(self):
    self.logo_intro_1 = createIntroSprite(LOGO_UPEC_LEFT, 0, 0)
    self.logo_intro_2 = createIntroSprite(LOGO_UPEC_RIGHT, WIN_WIDTH // 2 + 37, 0)
    self.sprites_intro_group.addSpriteGroup(self.logo_intro_1)
    self.sprites_intro_group.addSpriteGroup(self.logo_intro_2)

  def start(self):
    while self.running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False

      # generar fuegos artificiales 
      if random.random() < 0.02: 
        self.fireworks.createFirework()

      for firework in self.fireworks.fireworks:
        self.fireworks.updateFirework(firework)

      for particle in self.fireworks.particles:
        particle["position"][0] += particle["velocity"][0]
        particle["position"][1] += particle["velocity"][1]
        particle["ttl"] -= 1
        if particle['ttl'] <= 0:
          self.fireworks.particles.remove(particle)
      
      self.screen.blit(self.background, (0, 0))
      for firework in self.fireworks.fireworks:
        pygame.draw.circle(self.screen, firework['color'], (int(firework["position"][0]), int(firework["position"][1])), 3)
      for particle in self.fireworks.particles:
        pygame.draw.circle(self.screen, particle['color'], (int(particle['position'][0]), int(particle['position'][1])), 2)

      self.screen.blit(self.text_surface, self.text_rect)  

      # maneja todo de la animacion
      self.handler_animation_intro.waitingAnimation()      

      if not self.handler_animation_intro.get_waiting_done():
        self.sprites_intro_group.showSprite(self.screen)

      pygame.display.flip()

      self.clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
  game = Game() 
  game.start()