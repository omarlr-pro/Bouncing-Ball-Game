import pygame
import sys
from config import *
from menu import show_menu
from game import Game

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bouncing Ball Game')

# Show the menu and get user choice
speed = show_menu(screen, FONT)

# Start the game
game = Game(screen, speed)
game.run()

pygame.quit()
sys.exit()
