import pygame
import time
import random

# Set up some constants
WIDTH = 600
HEIGHT = 400
SNAKE_SIZE = 20
SNAKE_SPEED = 20
APPLE_SIZE = 20

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([ (0, -1), (0, 1), (1, 0), (-1, 0)])
        self.color = (0, 255, 0)

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (SNAKE_SPEED * x)) % WIDTH), ((cur[1] + (SNAKE_SPEED * y)) % HEIGHT))
        if new in self.positions[2:]:
            return False
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
        return True

    def draw(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], SNAKE_SIZE, SNAKE_SIZE))

def draw_apple(surface, pos):
    pygame.draw.rect(surface, (255, 0, 0), (pos[0], pos[1], APPLE_SIZE, APPLE_SIZE))

def random_apple():
    return (random.randint(0, WIDTH//APPLE_SIZE - 1)*APPLE_SIZE, random.randint(0, HEIGHT//APPLE_SIZE - 1)*APPLE_SIZE)

def collision_with_apple(snake_head, apple_position):
    return snake_head[0] == apple_position[0] and snake_head[1] == apple_position[1]

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    snake = Snake()
    apple_pos = random_apple()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.direction = (0, -1)
                elif event.key == pygame.K_DOWN:
                    snake.direction = (0, 1)
                elif event.key == pygame.K_LEFT:
                    snake.direction = (-1, 0)
                elif event.key == pygame.K_RIGHT:
                    snake.direction = (1, 0)

        if not snake.update():
            break

        snake_head = snake.get_head_position()
        if collision_with_apple(snake_head, apple_pos):
            snake.length += 1
            apple_pos = random_apple()

        surface.fill((0, 0, 0))
        snake.draw(surface)
        draw_apple(surface, apple_pos)
        screen.blit(surface, (0, 0))
        pygame.display.update()
        clock.tick(12)

if __name__ == "__main__":
    main()
