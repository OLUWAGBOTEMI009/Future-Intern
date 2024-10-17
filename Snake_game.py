# Create a snake game.


# IMPORT THE MODUES NEED 
import pygame
import random

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Screen dimensions
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Block size (size of the snake and food)
BLOCK_SIZE = 20

# Frames per second (speed of the game)
FPS = 8

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Define the snake class
class Snake:
    def __init__(self):
        self.size = BLOCK_SIZE
        self.body = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = pygame.K_RIGHT  # Initial direction is right
        self.grow = False

    def move(self):
        # Get the current head position
        head_x, head_y = self.body[0]

        # Move the snake in the direction it is facing
        if self.direction == pygame.K_RIGHT:
            head_x += BLOCK_SIZE
        elif self.direction == pygame.K_LEFT:
            head_x -= BLOCK_SIZE
        elif self.direction == pygame.K_UP:
            head_y -= BLOCK_SIZE
        elif self.direction == pygame.K_DOWN:
            head_y += BLOCK_SIZE

        # Insert the new head position at the front of the snake
        self.body = [(head_x, head_y)] + self.body

        # If snake grows, do not remove the tail (it extends)
        if not self.grow:
            self.body.pop()  # Remove the last segment if not growing
        else:
            self.grow = False  # Reset growth after one step

    def grow_snake(self):
        self.grow = True

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, BLOCK_SIZE, BLOCK_SIZE))

    def check_collision(self):
        # Check if the snake has collided with the screen boundaries
        head_x, head_y = self.body[0]
        if head_x < 0 or head_x >= SCREEN_WIDTH or head_y < 0 or head_y >= SCREEN_HEIGHT:
            return True

        # Check if the snake has collided with itself
        if len(self.body) > 1 and (head_x, head_y) in self.body[1:]:
            return True

        return False

# Define the food class
class Food:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        return (
            random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
            random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        )

    def draw(self):
        pygame.draw.rect(screen, RED, (*self.position, BLOCK_SIZE, BLOCK_SIZE))

# Main game loop
def game_loop():
    snake = Snake()
    food = Food()

    clock = pygame.time.Clock()
    score = 0
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Control the snake with arrow keys
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                    snake.direction = event.key

        snake.move()

        # Check if the snake eats the food
        if snake.body[0] == food.position:
            food.position = food.random_position()
            snake.grow_snake()
            score += 1

        # Check for collisions
        if snake.check_collision():
            game_over = True

        # Fill the screen with black (background color)
        screen.fill(BLACK)

        # Draw the snake and the food
        snake.draw()
        food.draw()

        # Display the score
        font = pygame.font.SysFont(None, 35)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, [0, 0])

        # Update the screen
        pygame.display.update()

        # Control the speed of the game
        clock.tick(FPS)

    # Display game over message
    screen.fill(BLACK)
    game_over_text = font.render("Game Over! Press R to Restart or Q to Quit", True, WHITE)
    screen.blit(game_over_text, [SCREEN_WIDTH // 6, SCREEN_HEIGHT // 2])
    pygame.display.update()

    # Wait for the player to restart or quit
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_loop()  # Restart the game
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

if __name__ == "__main__":
    game_loop()
