import pygame
import random
from config import *
from utils import get_random_color

class Game:
    def __init__(self, screen, speed, username):  # Accept username as a parameter
        self.screen = screen
        self.speed = speed
        self.username = username  # Store the username
        self.ball_velocity = self.set_ball_velocity(speed)
        self.ball_pos = self.set_initial_ball_position()
        self.ball_radius = BALL_RADIUS
        self.element_color = BALL_COLOR
        self.counter = 0
        self.lines = []
        self.game_over = False
        self.bounce_sound = pygame.mixer.Sound(BOUNCE_SOUND_PATH)

    def set_ball_velocity(self, speed):
        if speed == 1:
            return [2, 2]
        elif speed == 2:
            return [4, 4]
        elif speed == 3:
            return [6, 6]

    def set_initial_ball_position(self):
        return [
            random.randint(CIRCLE_CENTER[0] - CIRCLE_RADIUS + BALL_RADIUS, CIRCLE_CENTER[0] + CIRCLE_RADIUS - BALL_RADIUS),
            random.randint(CIRCLE_CENTER[1] - CIRCLE_RADIUS + BALL_RADIUS, CIRCLE_CENTER[1] + CIRCLE_RADIUS - BALL_RADIUS)
        ]

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif self.game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    self.reset_game()

            if not self.game_over:
                self.update_game()
                self.draw_game()
            else:
                self.show_game_over()

            pygame.display.flip()
            pygame.time.delay(10)

    def reset_game(self):
        self.ball_radius = BALL_RADIUS
        self.ball_pos = self.set_initial_ball_position()
        self.element_color = BALL_COLOR
        self.counter = 0
        self.game_over = False
        self.lines = []

    def update_game(self):
        self.ball_pos[0] += self.ball_velocity[0]
        self.ball_pos[1] += self.ball_velocity[1]

        distance_from_center = ((self.ball_pos[0] - CIRCLE_CENTER[0]) ** 2 + (self.ball_pos[1] - CIRCLE_CENTER[1]) ** 2) ** 0.5
        if distance_from_center >= CIRCLE_RADIUS - self.ball_radius:
            self.bounce_sound.play()
            self.element_color = get_random_color()
            self.reflect_ball_velocity(distance_from_center)
            self.add_contact_point(distance_from_center)
            if self.ball_radius < MAX_BALL_RADIUS:
                self.ball_radius += 1
            self.counter += 1

            if self.ball_radius >= CIRCLE_RADIUS:
                self.game_over = True

    def reflect_ball_velocity(self, distance_from_center):
        if self.ball_velocity[0] * (self.ball_pos[0] - CIRCLE_CENTER[0]) > 0:
            self.ball_velocity[0] = -self.ball_velocity[0] + random.choice([-1, 1])
        if self.ball_velocity[1] * (self.ball_pos[1] - CIRCLE_CENTER[1]) > 0:
            self.ball_velocity[1] = -self.ball_velocity[1] + random.choice([-1, 1])

    def add_contact_point(self, distance_from_center):
        contact_point = (
            CIRCLE_CENTER[0] + (self.ball_pos[0] - CIRCLE_CENTER[0]) * CIRCLE_RADIUS / distance_from_center,
            CIRCLE_CENTER[1] + (self.ball_pos[1] - CIRCLE_CENTER[1]) * CIRCLE_RADIUS / distance_from_center
        )
        self.lines.append(contact_point)

    def draw_game(self):
        self.screen.fill(BLACK)
        pygame.draw.circle(self.screen, self.element_color, CIRCLE_CENTER, CIRCLE_RADIUS, 1)
        pygame.draw.circle(self.screen, self.element_color, self.ball_pos, self.ball_radius)
        
        # Draw line following the center of the ball
        pygame.draw.line(self.screen, self.element_color, CIRCLE_CENTER, (self.ball_pos[0] + self.ball_radius, self.ball_pos[1] + self.ball_radius), 1)

        for point in self.lines:
            pygame.draw.line(self.screen, self.element_color, CIRCLE_CENTER, point, 1)

        counter_text = FONT.render(f"Counter: {self.counter}", True, WHITE)
        self.screen.blit(counter_text, (10, 10))

        # Display the username
        username_text = FONT.render(f"Logged in as: {self.username}", True, WHITE)
        self.screen.blit(username_text, (WIDTH - username_text.get_width() - 10, 10))  # Align to the top right corner

    def show_game_over(self):
        self.screen.fill(BLACK)
        game_over_text = FONT.render("Game Over! Press 'R' to Restart", True, WHITE)
        self.screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))


