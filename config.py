import pygame

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Circle properties
CIRCLE_RADIUS = 200
CIRCLE_CENTER = (WIDTH // 2, HEIGHT // 2)

# Ball properties
BALL_RADIUS = 20
MAX_BALL_RADIUS = 200  # Maximum ball radius to match the circle's radius
BALL_COLOR = (255, 0, 0)

# Font
pygame.font.init()
FONT = pygame.font.Font(None, 36)

# Sound
BOUNCE_SOUND_PATH = 'assets/sounds/bounce.wav'
