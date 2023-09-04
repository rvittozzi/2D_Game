import pygame
import sys

# Initialize Pygame
pygame.init()

# Define constants
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600

# Create the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Level 2")

# Define fonts and colors
font = pygame.font.Font(None, 36)
text_color = (255, 255, 255)

# Create a function to display the level 2 start message
def display_level_2_start_message():
    # Create a text surface with the level 2 start message
    level_2_start_text = font.render("Welcome to Level 2!", True, text_color)

    # Calculate the position to center the text on the screen
    text_x = (WINDOW_WIDTH - level_2_start_text.get_width()) // 2
    text_y = (WINDOW_HEIGHT - level_2_start_text.get_height()) // 2

    # Fill the screen with a background color (e.g., black)
    screen.fill((0, 0, 0))

    # Blit the level 2 start message onto the screen
    screen.blit(level_2_start_text, (text_x, text_y))

    pygame.display.flip()

# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Display the level 2 start message
        display_level_2_start_message()

if __name__ == "__main__":
    main()