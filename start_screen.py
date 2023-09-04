import pygame

def start_screen(screen, window_width, window_height):
    clock = pygame.time.Clock()
    background_color = (30, 30, 30)  # Define a blackish grey color
    screen.fill(background_color)  # Fill the screen with the chosen color
    
    # Load and display a game title or logo
    title_font = pygame.font.Font(None, 72)
    title_text = title_font.render("2D Fighter Game", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(window_width / 2, window_height / 4))

    # Instructions
    instruction_font = pygame.font.Font(None, 36)
    instruction_text1 = instruction_font.render("Press SPACE to begin", True, (255, 255, 255))
    instruction_text2 = instruction_font.render("Use arrow keys to move", True, (255, 255, 255))
    instruction_rect1 = instruction_text1.get_rect(center=(window_width / 2, window_height / 2))
    instruction_rect2 = instruction_text2.get_rect(center=(window_width / 2, window_height / 2 + 50))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return  # Exit the start screen function

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            return  # Exit the start screen function and transition to the game

        screen.blit(title_text, title_rect)
        screen.blit(instruction_text1, instruction_rect1)
        screen.blit(instruction_text2, instruction_rect2)
        pygame.display.flip()
        clock.tick(60)