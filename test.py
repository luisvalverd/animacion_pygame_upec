import pygame
import sys
from types.config import *

# Inicializa Pygame
pygame.init()

# Dimensiones de la pantalla
WIDTH = WIN_WIDTH
HEIGHT = WIN_HEIGHT 
SCREEN_SIZE = (WIDTH, HEIGHT)

# Colores
WHITE = (255, 255, 255)

# Clase para el sprite de la imagen
class Image(pygame.sprite.Sprite):
  def __init__(self, image_path, x, y):
    super().__init__()
    self.image = pygame.image.load(image_path)
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)

# Configuración de la pantalla
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Transición de Imágenes")

# Carga de imágenes
image1_sprite = Image(LOGO_UPEC_LEFT, -WIDTH // 2, 0)
image2_sprite = Image(LOGO_UPEC_RIGHT, WIDTH, 0)

# Grupo de sprites
all_sprites = pygame.sprite.Group(image1_sprite, image2_sprite)

# Velocidad de transición
transition_speed = 5

# Tiempo de espera antes de iniciar la transición (en segundos)
waiting_time = 2
waiting_frames = waiting_time * 60  # Convertir segundos a fotogramas (60 fps)

clock = pygame.time.Clock()

# Variables de control
waiting_done = False
transition_done = False

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  if not waiting_done:
    # Espera durante waiting_frames antes de iniciar la transición
    waiting_frames -= 1
    if waiting_frames <= 0:
      waiting_done = True
      # Reiniciar la posición de las imágenes para la transición
      image1_sprite.rect.x = -WIDTH // 2
      image2_sprite.rect.x = WIDTH

  elif not transition_done:
    # Actualiza las posiciones de las imágenes para lograr el efecto de transición
    image1_sprite.rect.x += transition_speed
    image2_sprite.rect.x -= transition_speed

    # Si la transición ha terminado, marca transition_done como True
    if image1_sprite.rect.x >= 0 and image2_sprite.rect.x <= 0:
      transition_done = True

  # Dibuja los sprites en la pantalla
  screen.fill(WHITE)
  all_sprites.draw(screen)

  # Actualiza la pantalla
  pygame.display.flip()

  # Controla la velocidad del bucle
  clock.tick(60)

  # Si la transición ha terminado, sal del bucle
  if transition_done:
    break

pygame.quit()
sys.exit()