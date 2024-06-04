import pygame
import sys
from config import WIDTH, HEIGHT, FONT
from menu import show_menu
from game import Game
from authentication import MySQLAuthentication

pygame.init()

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bouncing Ball Game')

# Function to display the login screen
def display_login_screen(screen, font, auth):
    username = ''
    password = ''
    input_rect_username = pygame.Rect(300, 200, 200, 30)
    input_rect_password = pygame.Rect(300, 250, 200, 30)  # Define a rectangle for the password input
    username_active = True
    password_active = False
    login_button_rect = pygame.Rect(300, 300, 100, 50)
    login_button_color = pygame.Color('dodgerblue')
    login_button_text_color = pygame.Color('white')

    while True:
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, pygame.Color('gray'), input_rect_username, 2)  # Render the username input field
        pygame.draw.rect(screen, pygame.Color('gray'), input_rect_password, 2)  # Render the password input field

        login_button = pygame.draw.rect(screen, login_button_color, login_button_rect)
        font_surface = font.render('Login', True, login_button_text_color)
        screen.blit(font_surface, (login_button.x + 10, login_button.y + 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect_username.collidepoint(event.pos):
                    username_active = True
                    password_active = False
                elif input_rect_password.collidepoint(event.pos):  # Check if password input field is clicked
                    username_active = False
                    password_active = True
                elif login_button.collidepoint(event.pos):
                    # Attempt to log in
                    logged_in = auth.login(username, password)
                    if logged_in:
                        return True
                else:
                    username_active = False
                    password_active = False
            if event.type == pygame.KEYDOWN:
                if username_active:
                    if event.key == pygame.K_RETURN:
                        username_active = False
                        password_active = True
                    elif event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        username += event.unicode
                elif password_active:
                    if event.key == pygame.K_RETURN:
                        password_active = False
                        # Attempt to log in
                        logged_in = auth.login(username, password)
                        if logged_in:
                            return True
                    elif event.key == pygame.K_BACKSPACE:
                        password = password[:-1]
                    else:
                        password += event.unicode

        input_text_surface_username = font.render(username, True, pygame.Color('black'))
        input_text_surface_password = font.render('*' * len(password), True, pygame.Color('black'))  # Display '*' for password characters
        screen.blit(input_text_surface_username, (input_rect_username.x + 5, input_rect_username.y + 5))
        screen.blit(input_text_surface_password, (input_rect_password.x + 5, input_rect_password.y + 5))  # Render password input text

        pygame.display.flip()

# Create an instance of MySQLAuthentication
auth = MySQLAuthentication("localhost", "root", "", "pypy")

# Display login screen and attempt to log in
if display_login_screen(screen, FONT, auth):
    # Show the menu and get user choice
    speed = show_menu(screen, FONT)

    # Get the username from the authentication object
    username = auth.username

    # Start the game with the username parameter
    game = Game(screen, speed, username)
    game.run()

pygame.quit()
sys.exit()
