import pygame
import sys

# Set up some constants
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 10
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
BALL_VELOCITY = 3
PADDLE_VELOCITY = 3

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()

# Set up drawing window
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# Create ball and paddles
ball = pygame.Rect(WIDTH / 2, HEIGHT / 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
paddle1 = pygame.Rect(0, HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(WIDTH - PADDLE_WIDTH, HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Create velocities
ball_vel = [BALL_VELOCITY, BALL_VELOCITY]
paddle1_vel = [0, PADDLE_VELOCITY]
paddle2_vel = [0, PADDLE_VELOCITY]

# Create scores
score1 = 0
score2 = 0

# Run until the user asks to quit
while True:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Add the keyboard controls for the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1_vel[1] = -PADDLE_VELOCITY
    elif keys[pygame.K_s]:
        paddle1_vel[1] = PADDLE_VELOCITY
    else:
        paddle1_vel[1] = 0

    if keys[pygame.K_UP]:
        paddle2_vel[1] = -PADDLE_VELOCITY
    elif keys[pygame.K_DOWN]:
        paddle2_vel[1] = PADDLE_VELOCITY
    else:
        paddle2_vel[1] = 0

    # Move the ball
    ball.move_ip(ball_vel)

    # Move the paddles
    if paddle1.top + paddle1_vel[1] >= 0 and paddle1.bottom + paddle1_vel[1] <= HEIGHT:
        paddle1.move_ip(paddle1_vel)
    if paddle2.top + paddle2_vel[1] >= 0 and paddle2.bottom + paddle2_vel[1] <= HEIGHT:
        paddle2.move_ip(paddle2_vel)

    # Collide with edges
    if ball.left < 0:
        score2 += 1
        ball.center = (WIDTH / 2, HEIGHT / 2)
    if ball.right > WIDTH:
        score1 += 1
        ball.center = (WIDTH / 2, HEIGHT / 2)
    if ball.top < 0 or ball.bottom > HEIGHT:
        ball_vel[1] *= -1

    # Collide with paddles
    if ball.colliderect(paddle1) and ball_vel[0] < 0:
        ball_vel[0] *= -1
    elif ball.colliderect(paddle2) and ball_vel[0] > 0:
        ball_vel[0] *= -1

    # Fill the background
    screen.fill(BLACK)

    # Draw the ball and paddles
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH / 2, 0), (WIDTH / 2, HEIGHT))

    # Draw the scores
    font = pygame.font.Font(None, 36)
    text = font.render(f"{score1} - {score2}", True, WHITE)
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, 10))

    # Flip the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
