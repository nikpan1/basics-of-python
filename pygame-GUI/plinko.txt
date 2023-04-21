import random

import pygame
import pymunk
from sys import exit

BCKG = (100, 100, 100)
BLACK = (0, 0, 80)
ball_size = 8
plinko_size = 8
turn = 0
print(random.randint(0, 1))


def create_apple(space):
    a = random.randint(0, 1)
    pos = [-1, 1]
    a = pos[a]
    body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
    body.position = (400 + a, 0)
    shape = pymunk.Circle(body, ball_size)
    space.add(body, shape)
    return shape


def draw_apples(apples):
    for apple in apples:
        pygame.draw.circle(screen, BLACK, apple.body.position, ball_size)


def static_ball(space):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (400, 50)
    shape = pymunk.Circle(body, plinko_size)
    space.add(body, shape)
    return shape


def draw_static_ball(balls):
    for ball in balls:
        pygame.draw.circle(screen, BLACK, ball.body.position, plinko_size)


screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
pygame.display.set_caption("plinko")

space = pymunk.Space()
space.gravity = (0, 280)
apples = []
apples.append(create_apple(space))

balls = []
balls.append(static_ball(space))


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill(BCKG)
    draw_apples(apples)
    draw_static_ball(balls)
    space.step(1/50)
    pygame.display.update()
    clock.tick(120)

#   pygame.draw.ellipse(screen, (200, 200, 200), [20, 20, 250, 100], 2)
# apples.append(create_apples(space, event.pos