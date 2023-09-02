import pygame
import sys
import start_screen

# Initialize Pygame
pygame.init()

# Define constants
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
GAME_STATE_START, GAME_STATE_PLAY = 1, 2
PUNCH_DAMAGE, PUNCH_HITBOX_WIDTH, PUNCH_HITBOX_HEIGHT, PUNCH_COOLDOWN = 20, 20, 40, 1
animationSpeed = 0.2

# Create the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Your Game Title")

# Load individual sprite images
idle = pygame.image.load("sprites/idle.png")
run = pygame.image.load("sprites/run.png")
background = pygame.image.load("sprites/background.png")
start_screen_background = pygame.image.load("sprites/start_screen_background.png")

# Define player variables
player1 = {
    "x": 100,
    "y": 300,
    "width": 50,
    "height": 100,
    "speed": 200,
    "health": 100,
    "hits": 0,
    "punchCooldown": 0,
    "currentFrame": 1,
    "animationTimer": 2,
    "idleFrame": 1,
}

player2 = {
    "x": 600,
    "y": 300,
    "width": 50,
    "height": 100,
    "speed": 200,
    "health": 100,
    "hits": 0,
    "punchCooldown": 0,
}

# Game state
gameState = GAME_STATE_START

# Main game loop
clock = pygame.time.Clock()

# Inside your main game loop:

while True:
    keys = pygame.key.get_pressed()  # Initialize keys at the beginning of the loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))  # Clear the screen with black

    if gameState == GAME_STATE_START:
        # Scale the background image to fit the window size
        scaled_background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))
        # Display the start screen
        start_screen.start_screen(screen, WINDOW_WIDTH, WINDOW_HEIGHT)

        # Draw the start screen background
        screen.blit(scaled_background, (0, 0))

        if keys[pygame.K_SPACE]:
            # Reset player and game variables when transitioning to play state
            player1["x"] = 100
            player1["y"] = 300
            player1["health"] = 100
            player1["hits"] = 0
            player1["punchCooldown"] = 0
            player1["currentFrame"] = 1
            player1["animationTimer"] = 2
            player1["idleFrame"] = 1

            gameState = GAME_STATE_PLAY

    # Define leftmost and rightmost boundaries based on your window size and character's dimensions
    left_boundary = 0  # The left edge of the window
    right_boundary = WINDOW_WIDTH - player1["width"]  # The right edge of the window, considering character's width

    if gameState == GAME_STATE_PLAY:
        screen.blit(scaled_background, (0, 0))  # Draw the background

        # Handle player input
        if keys[pygame.K_LEFT]:
            # Move left
            player1["x"] -= player1["speed"] * animationSpeed * 0.1

            # Ensure the player stays within the left boundary
            if player1["x"] < left_boundary:
                player1["x"] = left_boundary

        if keys[pygame.K_RIGHT]:
            # Move right
            player1["x"] += player1["speed"] * animationSpeed * 0.1

            # Ensure the player stays within the right boundary
            if player1["x"] > right_boundary:
                player1["x"] = right_boundary

        # Animate the player (you can implement animation logic here)

        # Render the player character (draw "idle.png" sprite at player1["x"], player1["y"])
        screen.blit(idle, (player1["x"], player1["y"]))

    pygame.display.flip()
    clock.tick(60)