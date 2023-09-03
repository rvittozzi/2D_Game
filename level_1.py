import pygame
import sys
import random

from start_screen import start_screen

# Initialize Pygame
pygame.init()

# Define constants
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
GAME_STATE_START, GAME_STATE_PLAY = 1, 2
PUNCH_DAMAGE, PUNCH_HITBOX_WIDTH, PUNCH_HITBOX_HEIGHT, PUNCH_COOLDOWN = 25, 20, 40, 60
animationSpeed = 0.2

# Create the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("2D Fighter")

# Load individual sprite images and other assets
idle = pygame.image.load("sprites/Player1/idle/idle.png")
run = pygame.image.load("sprites/Player1/run/run.png")
background = pygame.image.load("sprites/background_assets/background.png")
start_screen_background = pygame.image.load("sprites/background_assets/start_screen_background.png")
enemy_sprite = pygame.image.load("sprites/enemy/enemy_sprite.png")

# Scale factor for the player and enemy sprites
scaling_factor = 2

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
    "scaled_width": 50 * scaling_factor,
    "scaled_height": 100 * scaling_factor,
    "is_jumping": False,
    "jump_height": 10,
    "jump_velocity": 0,
    "is_punching": False,
    "punch_cooldown": 0,
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
    "facing_left": False,
    "scaled_width": 50 * scaling_factor,
    "scaled_height": 100 * scaling_factor,
}

# Game state
gameState = GAME_STATE_START

# Define the draw_health_bar function
def draw_health_bar(surface, x, y, current_health, max_health, width=100, height=10):
    health_width = (current_health / max_health) * width

    if current_health > 0.6 * max_health:
        color = (0, 255, 0)
    elif current_health > 0.3 * max_health:
        color = (255, 255, 0)
    else:
        color = (255, 0, 0)

    pygame.draw.rect(surface, (255, 0, 0), (x, y, width, height))
    pygame.draw.rect(surface, color, (x, y, health_width, height))

# Load individual sprite images for idle and run
idle_frames = [pygame.image.load(f"sprites/Player1/idle/idle{i}.png") for i in range(1, 5)]
run_frames = [pygame.image.load(f"sprites/Player1/run/run{i}.png") for i in range(1, 5)]
current_animation = idle_frames
animation_index = 0

# Create a boolean variable to track whether the player is moving
is_moving = False

# Define ground variables
ground_width = WINDOW_WIDTH
ground_height = 100
ground_color = (100, 100, 100)

# Create a ground surface
ground_surface = pygame.Surface((ground_width, ground_height))
ground_surface.fill(ground_color)

# Define enemy respawn variables and constants
enemy_respawn_timer = 0
enemy_respawn_delay = 5  # 5 seconds respawn delay
enemy_respawned = False


# Define enemy patrol variables
patrol_points = [(600, 300), (400, 300), (200, 300)]  # Define patrol points here
current_patrol_point = 0
patrol_speed = 0.9  # Adjust the speed as needed

# Initialize the player's score
score = 0

# Main game loop
clock = pygame.time.Clock()

# Define a list of spawn points for the enemy
enemy_spawn_points = [(600, 300), (400, 300), (200, 300), (300, 300), (500, 300)]  # Add more spawn points as needed

while True:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    if gameState == GAME_STATE_START:
        scaled_background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))
        screen.blit(scaled_background, (0, 0))

        # Use the start_screen function to display the start screen
        start_screen(screen, WINDOW_WIDTH, WINDOW_HEIGHT)

        if keys[pygame.K_SPACE]:
            gameState = GAME_STATE_PLAY

    left_boundary = 0
    right_boundary = WINDOW_WIDTH - player1["width"]

    if gameState == GAME_STATE_PLAY:
        screen.blit(ground_surface, (0, WINDOW_HEIGHT - ground_height))
        screen.blit(scaled_background, (0, 0))

        if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
            is_moving = True
        else:
            is_moving = False

        if keys[pygame.K_LEFT]:
            player1["x"] -= player1["speed"] * animationSpeed * 0.1
            if player1["x"] < left_boundary:
                player1["x"] = left_boundary

        if keys[pygame.K_RIGHT]:
            player1["x"] += player1["speed"] * animationSpeed * 0.1
            if player1["x"] > right_boundary:
                player1["x"] = right_boundary

        if not player1["is_jumping"]:
            if keys[pygame.K_SPACE]:
                player1["is_jumping"] = True
                player1["jump_velocity"] = -player1["jump_height"]

        else:
            player1["jump_velocity"] += 0.5
            player1["y"] += player1["jump_velocity"]

            if player1["y"] >= 300:
                player1["y"] = 300
                player1["is_jumping"] = False
                player1["jump_velocity"] = 0

        if keys[pygame.K_v] and player1["punch_cooldown"] <= 0:
            player1["is_punching"] = True
            player1["punch_cooldown"] = PUNCH_COOLDOWN

        if player1["punch_cooldown"] > 0:
            player1["punch_cooldown"] -= 1

        if player1["is_punching"]:
            current_animation = idle_frames
            if (
                player1["x"] + player1["scaled_width"] >= enemy["x"]
                and player1["x"] <= enemy["x"] + enemy["scaled_width"]
                and player1["y"] + player1["scaled_height"] >= enemy["y"]
                and player1["y"] <= enemy["y"] + enemy["scaled_height"]
            ):
                enemy["health"] -= PUNCH_DAMAGE
                if enemy["health"] <= 0:
                    # Randomly select a spawn point for the enemy
                    random_spawn_point = random.choice(enemy_spawn_points)
                    enemy["x"], enemy["y"] = random_spawn_point
                    enemy["health"] = 100  # Set enemy health to full HP
                    # Increase the player's score
                    score += 50  # Add 50 points for each defeated enemy
                # Reset the punch animation here (added)
                player1["is_punching"] = False
        else:
            if is_moving:
                animation_index = (animation_index + 1) % len(run_frames)
                current_animation = run_frames
            else:
                current_animation = idle_frames

        # Draw the enemy at the new position
        screen.blit(pygame.transform.scale(enemy_sprite, (enemy["scaled_width"], enemy["scaled_height"])), (enemy["x"], enemy["y"]))

        screen.blit(pygame.transform.scale(current_animation[animation_index], (player1["scaled_width"], player1["scaled_height"])), (player1["x"], player1["y"]))
        draw_health_bar(screen, player1["x"], player1["y"] - 20, player1["health"], 100)
        draw_health_bar(screen, enemy["x"], enemy["y"] - 20, enemy["health"], 100)

        # Display the player's score on the screen
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)