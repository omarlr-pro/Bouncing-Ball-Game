import pygame
import sys
from config import BLACK, WHITE, WIDTH, HEIGHT

def show_menu(screen, font):
    speed = 2
    choosing = True
    while choosing:
        screen.fill(BLACK)
        menu_text = [
            "Select Speed:",
            "1. Slow",
            "2. Medium",
            "3. Fast"
        ]
        
        for i, line in enumerate(menu_text):
            text = font.render(line, True, WHITE)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 4 + i * 40))
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    speed = 1
                    choosing = False
                elif event.key == pygame.K_2:
                    speed = 2
                    choosing = False
                elif event.key == pygame.K_3:
                    speed = 3
                    choosing = False

    return speed
