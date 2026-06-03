
mass = float(input("What is the mass?"))
velocity = float(input("What is the velocity"))
K = 0.5 * mass * (velocity**2)

print("Kinetic Energy is", K )


import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Clock
clock = pygame.time.Clock()
FPS = 10

# Snake
snake = [(100, 100), (80, 100), (60, 100)]
direction = (CELL_SIZE, 0)

# Food
food = (
    random.randrange(0, WIDTH, CELL_SIZE),
    random.randrange(0, HEIGHT, CELL_SIZE)
)

# Font
font = pygame.font.SysFont(None, 36)

def draw():
    screen.fill(BLACK)

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

    # Draw food
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

    # Score
    score_text = font.render(f"Score: {len(snake) - 3}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

def game_over():
    text = font.render("Game Over!", True, WHITE)
    rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    screen.fill(BLACK)
    screen.blit(text, rect)
    pygame.display.flip()

    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                direction = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                direction = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                direction = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                direction = (CELL_SIZE, 0)

    # Move snake
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])

    # Collision with walls
    if (
        new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT
    ):
        game_over()

    # Collision with self
    if new_head in snake:
        game_over()

    snake.insert(0, new_head)

    # Eat food
    if new_head == food:
        food = (
            random.randrange(0, WIDTH, CELL_SIZE),
            random.randrange(0, HEIGHT, CELL_SIZE)
        )
    else:
        snake.pop()

    draw()
    clock.tick(FPS)