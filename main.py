# main.py

import pygame
from start_screen import start_screen
from level_1 import run_level_1
from level_2 import run_level_2

# Initialize pygame
pygame.init()

# Set up game window and other configurations
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Your Game Title')

# Main game loop
running = True
current_screen = 'start'  # Initially start with the start screen

while running:
    if current_screen == 'start':
        current_screen = start_screen(screen)
    elif current_screen == 'level_1':
        current_screen = run_level_1(screen)
    elif current_screen == 'level_2':
        current_screen = run_level_2(screen)

    # Handle game events, like quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
