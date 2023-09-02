import pygame

def start_screen(screen, window_width, window_height):
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    text = font.render("Press SPACE to begin", True, (255, 255, 255))
    text_rect = text.get_rect(center=(window_width / 2, window_height / 2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return  # Exit the start screen function

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            return  # Exit the start screen function and transition to the game

        screen.fill((0, 0, 0))  # Clear the screen with black
        screen.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(60)
