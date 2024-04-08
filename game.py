import pygame
from controller.sounds_controller import SoundController # type: ignore
from domain.config import *
from domain.intro_rule import createAnimation, createIntroSprite
from domain.sprites_group_rule import createSpritesGroup, addSpriteAGroup
from domain.firework import FireworkRules 
from domain.firework_rule import createFireworkAnimation # type: ignore
from domain.people_rule import createPeopleSprite, createAnimationPeopleEntrance
import random


class Game:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    self.clock = pygame.time.Clock()
    self.font = pygame.font.Font(FONT_BIG_BLUE, 50)
    self.font.set_bold(True)
    self.running = True

    self.background = pygame.image.load(BG_BUILDING)
    self.screen.blit(self.background, (0, 0))

    # fuegos artificiales
    self.fireworks = []

    self.text_index = 0
    self.rendered_text = "" 
    self.time_waiting = 5 * 60
    self.time_show_letter = 100

    # sprites de intro
    self.sprites_intro_group = createSpritesGroup()
    self.logo_intro_1 = None
    self.logo_intro_2 = None

    # sprites de people
    self.sprite_people_group = createSpritesGroup() 
    self.people_1 = None
    self.people_2 = None

    self.sprite_neon_group = createSpritesGroup()
    self.neon = None
    
    pygame.mixer.init(devicename="Realtek(R) Audio")    

    # sounds
    self.bg_music = pygame.mixer.Sound(BG_MUSIC)

    self.people_entrance_sound = pygame.mixer.Sound(PEOPLE_ENTRANCE) 
    self.mixer_people = SoundController(1, self.people_entrance_sound, 10, 5)
    self.mixer_people.set_volume(0.2)

    self.people_celebraing_sound = pygame.mixer.Sound(PEOPLE_CELEBRATING)
    self.mixer_people_celebrating = SoundController(2, self.people_celebraing_sound, 15, 16)
    self.mixer_people.set_volume(0.2)

    self.switch_sound = pygame.mixer.Sound(SWITCH_DOWN)
    self.mixer_switch = SoundController(1, self.switch_sound, 4, 1)
    self.mixer_switch.set_volume(0.8)

    self.neon_sound = pygame.mixer.Sound(NEON_SOUND)
    self.mixer_neon = SoundController(2, self.neon_sound, 5, 1)

    # channel de musica de fondo
    pygame.mixer.Channel(0).set_volume(0.01)
    pygame.mixer.Channel(0).play(self.bg_music, -1)

    #handlers
    self.handleSpriteIntro()
    self.handler_animation_intro = createAnimation(self.logo_intro_1, self.logo_intro_2, 4)
    self.handler_fireworks = createFireworkAnimation(self.fireworks, 15, self.screen)

    self.handleSpritePoeple()
    self.handler_people = createAnimationPeopleEntrance(self.people_1, self.people_2, 5)

    self.handleSpriteNeon()

    self.is_bg_img = True
    self.bg_time = 31 * 60

    self.switch_time = 30

    self.stop = 4 * 60

  def handleSpriteNeon(self):
    self.neon = createIntroSprite(NEON_IMG, 0, 0)
    addSpriteAGroup(self.sprite_neon_group, self.neon)
  
  """
  maneja la construccion de los sprites 
  agrega los sprites de la intro a un grupo de sprites
  """
  def handleSpriteIntro(self):
    self.logo_intro_1 = createIntroSprite(LOGO_UPEC_LEFT, 0, 0)
    self.logo_intro_2 = createIntroSprite(LOGO_UPEC_RIGHT, WIN_WIDTH // 2 + 37, 0)
    addSpriteAGroup(self.sprites_intro_group, self.logo_intro_1)
    addSpriteAGroup(self.sprites_intro_group, self.logo_intro_2)

  def handleSpritePoeple(self):
    self.people_1 = createPeopleSprite(PEOPLE_1, 0, WIN_HEIGHT - 20)
    self.people_2 = createPeopleSprite(PEOPLE_2, 0, WIN_HEIGHT)
    addSpriteAGroup(self.sprite_people_group, self.people_1)
    addSpriteAGroup(self.sprite_people_group, self.people_2)

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

      
      if self.handler_fireworks.waiting_time <= 0:
        if random.randint(0, 20) == 1:
          self.fireworks.append(FireworkRules())

      self.handler_fireworks.waitingAnimation()      

      if self.bg_time <= 0:
        self.is_bg_img = False
      else:
        self.bg_time -= 1

      if self.is_bg_img:
        self.screen.blit(self.background, (0, 0))
      else:
        self.screen.fill((0, 0, 0))
        

      # people group
      if self.is_bg_img:
        self.handler_people.waitingAnimation()
        if not self.handler_people.get_waiting_done():
          self.sprite_people_group.showSprite(self.screen) 

      # people sound
      self.mixer_people_celebrating.waitingSound()
      self.mixer_people.waitingSound()

      
      if self.time_waiting <= 0:
        if self.time_show_letter == 0:
          if self.text_index < len(TEXT_UPEC):
            self.rendered_text += TEXT_UPEC[self.text_index]
            self.text_index += 1
        elif self.time_show_letter < 0:
          self.time_show_letter = 0
        else: 
          self.time_show_letter -= 1
      self.time_waiting -= 1

      if self.is_bg_img:
        # Renderizar texto con contorno
        outline = self.font.render(self.rendered_text, True, (0, 0, 0))
        outline_text_rect = outline.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))
        self.screen.blit(outline, outline_text_rect.move(2, 2))

        # Renderizar texto
        rendered_text_surface = self.font.render(self.rendered_text, True, (56, 176, 0))
        text_rect = rendered_text_surface.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))
        self.screen.blit(rendered_text_surface, text_rect)
        
        # maneja todo de la animacion
        self.handler_animation_intro.waitingAnimation()      
        if not self.handler_animation_intro.get_waiting_done():
          self.sprites_intro_group.showSprite(self.screen)
      else :
        pygame.mixer.Channel(0).stop()
        self.mixer_switch.waitingSound()
        self.mixer_neon.waitingSound()
        self.sprite_neon_group.showSprite(self.screen)

        if self.stop >= 0:
          self.stop -= 1
        else:
          break
        
        

      pygame.display.flip()
    pygame.mixer.Channel(0).stop()
    pygame.quit()

if __name__ == "__main__":
  game = Game() 
  game.start()