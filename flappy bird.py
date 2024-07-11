import pygame
import sys

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
BIRD_SIZE = 50
PIPE_WIDTH = 80
PIPE_HEIGHT = 600
PIPE_GAP = 150

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

bird_image = pygame.Surface((BIRD_SIZE, BIRD_SIZE))
bird_image.fill(RED)
pipe_image = pygame.Surface((PIPE_WIDTH, PIPE_HEIGHT))
pipe_image.fill(GREEN)

bird_x = SCREEN_WIDTH / 2
bird_y = SCREEN_HEIGHT / 2
pipe_x = SCREEN_WIDTH
pipe_y = SCREEN_HEIGHT / 2
score = 0
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                bird_y -= 40    
            elif event.key == pygame.K_SPACE and game_over:
                bird_x = SCREEN_WIDTH / 2
                bird_y = SCREEN_HEIGHT / 2
                pipe_x = SCREEN_WIDTH
                pipe_y = SCREEN_HEIGHT / 2
                score = 0
                game_over = False

    bird_y += 5

    pipe_x -= 5

    if (bird_x + BIRD_SIZE > pipe_x and bird_x < pipe_x + PIPE_WIDTH and
        (bird_y < pipe_y - PIPE_GAP / 2 or bird_y + BIRD_SIZE > pipe_y + PIPE_GAP / 2)):
        game_over = True

    if pipe_x + PIPE_WIDTH < bird_x and not game_over:
        score += 1

    screen.fill(BLACK)
    screen.blit(bird_image, (bird_x, bird_y))
    screen.blit(pipe_image, (pipe_x, pipe_y - PIPE_HEIGHT))
    screen.blit(pipe_image, (pipe_x, pipe_y + PIPE_GAP))
    pygame.display.update()

    clock.tick(60)