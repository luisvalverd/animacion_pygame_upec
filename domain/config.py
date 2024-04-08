import pygame

# tamaño de la ventana
WIN_WIDTH = 1020
WIN_HEIGHT = 970 

# rutas de las imagenes
LOGO_UPEC_LEFT = "img/logo_upec_left.jpeg"
LOGO_UPEC_RIGHT = "img/logo_upec_right.jpeg"
PEOPLE_1 = "img/people_group_1.png"

# ruta de los audios
BG_MUSIC ="sounds/background_music.mp3"

# vector 
VECTOR = pygame.math.Vector2

# gravedad
GRAVITY = VECTOR(0, 0.26)

# colores de la cola del fuego artificial
TRAIL_COLORS = [(45, 45, 45), (60, 60, 60), (75, 75, 75), (125, 125, 125), (150, 150, 150)]

# movimientos dinamicos 
DYNAIC_OFFSET = 2
STATIC_OFFSET = 5