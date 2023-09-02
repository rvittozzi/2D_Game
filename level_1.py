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
enemy_sprite = pygame.image.load("sprites/enemy_sprite.png")

# Scale factor for the player and enemy sprites
scaling_factor = 3

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
    "scaled_width": 50 * scaling_factor,  # Scaled width
    "scaled_height": 100 * scaling_factor,  # Scaled height
    "is_jumping": False,  # Flag to track if the player is jumping
    "jump_height": 10,  # Adjust this value to control jump height
    "jump_velocity": 0,  # Vertical velocity during jump
}

# Define enemy variables
enemy = {
    "x": 600,
    "y": 300,
    "width": 50,
    "height": 100,
    "speed": 200,
    "health": 100,
    "hits": 0,
    "punchCooldown": 0,
    "facing_left": False,  # Flag to track enemy's facing direction
    "scaled_width": 50 * scaling_factor,  # Scaled width
    "scaled_height": 100 * scaling_factor,  # Scaled height
}

# Game state
gameState = GAME_STATE_START

# Main game loop
clock = pygame.time.Clock()

while True:
    keys = pygame.key.get_pressed()

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
            gameState = GAME_STATE_PLAY

    left_boundary = 0
    right_boundary = WINDOW_WIDTH - player1["width"]

    if gameState == GAME_STATE_PLAY:
        screen.blit(scaled_background, (0, 0))  # Draw the background

        # Handle player input
        if keys[pygame.K_LEFT]:
            player1["x"] -= player1["speed"] * animationSpeed * 0.1
            if player1["x"] < left_boundary:
                player1["x"] = left_boundary

        if keys[pygame.K_RIGHT]:
            player1["x"] += player1["speed"] * animationSpeed * 0.1
            if player1["x"] > right_boundary:
                player1["x"] = right_boundary

        # Check if the player is on the ground (not jumping)
        if not player1["is_jumping"]:
            # Handle jumping
            if keys[pygame.K_SPACE]:
                player1["is_jumping"] = True
                player1["jump_velocity"] = -player1["jump_height"]  # Negative velocity for upward motion

        else:
            # Apply gravity to the player
            player1["jump_velocity"] += 0.5  # Adjust this value for gravity strength
            player1["y"] += player1["jump_velocity"]

            # Check if the player has landed on the ground
            if player1["y"] >= 300:  # Adjust this value based on your ground level
                player1["y"] = 300
                player1["is_jumping"] = False
                player1["jump_velocity"] = 0

        # Render the player character with scaled size
        screen.blit(pygame.transform.scale(idle, (player1["scaled_width"], player1["scaled_height"])), (player1["x"], player1["y"]))

        # Render the enemy character with scaled size
        screen.blit(pygame.transform.scale(enemy_sprite, (enemy["scaled_width"], enemy["scaled_height"])), (enemy["x"], enemy["y"]))

    pygame.display.flip()
    clock.tick(60)