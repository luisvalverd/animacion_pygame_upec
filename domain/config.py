import pygame

# tamaño de la ventana
WIN_WIDTH = 1020
WIN_HEIGHT = 970 

# rutas de las imagenes
LOGO_UPEC_LEFT = "img/logo_upec_left.jpeg"
LOGO_UPEC_RIGHT = "img/logo_upec_right.jpeg"

# vector 
VECTOR = pygame.math.Vector2

# gravedad
GRAVITY = VECTOR(0, 0.3)

# colores de la cola del fuego artificial
TRAIL_COLORS = [(45, 45, 45), (60, 60, 60), (75, 75, 75), (125, 125, 125), (150, 150, 150)]