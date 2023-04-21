import random
import time
import pygame
from pygame.locals import *


WINDOW_HEIGHT, WINDOW_WIDTH = 600, 800  # window resolution
GAME_SPEED = 0.25  # in seconds
BLOCK_SIZE = 30

# colors:
SNAKE_COLOR = (100, 255, 0)
APPLE_COLOR = (255, 20, 0)
BACKGROUND_COLOR = (100, 100, 0)
WHITE = (255, 255, 255)


class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.apple_block = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.apple_block.fill(APPLE_COLOR)
        self.apple_x, self.apple_y = 0, 0
        self.move()

    def draw(self):
        self.parent_screen.blit(self.apple_block, (self.apple_x, self.apple_y))
        pygame.display.flip()

    def move(self):
        self.apple_x = random.randint(1, int(WINDOW_WIDTH / BLOCK_SIZE) - 1) * BLOCK_SIZE
        self.apple_y = random.randint(1, int(WINDOW_HEIGHT / BLOCK_SIZE) - 1) * BLOCK_SIZE


class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block_x = [random.randint(1, int(WINDOW_WIDTH/BLOCK_SIZE) - 1) * BLOCK_SIZE] * length
        self.block_y = [random.randint(1, int(WINDOW_HEIGHT/BLOCK_SIZE) - 1) * BLOCK_SIZE] * length

        self.block = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.block.fill(SNAKE_COLOR)
        self.direction = 'down'

    def add_length(self):
        self.length += 1
        self.block_x.append(-1)
        self.block_y.append(-1)

    def draw(self):
        self.parent_screen.fill(BACKGROUND_COLOR)
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.block_x[i], self.block_y[i]))
        pygame.display.update()

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def walk(self):
        for i in range(self.length - 1, 0, -1):
            self.block_x[i] = self.block_x[i - 1]
            self.block_y[i] = self.block_y[i - 1]

        if self.direction == 'up':
            self.block_y[0] -= BLOCK_SIZE
        if self.direction == 'down':
            self.block_y[0] += BLOCK_SIZE
        if self.direction == 'left':
            self.block_x[0] -= BLOCK_SIZE
        if self.direction == 'right':
            self.block_x[0] += BLOCK_SIZE
        self.draw()


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.surface.fill(BACKGROUND_COLOR)

        self.snake = Snake(self.surface, 3)
        self.apple = Apple(self.surface)

        self.snake.draw()
        self.apple.draw()

    def is_collision(self, x1, y1, x2, y2):
        if (x1 >= x2) and (x1 < x2 + BLOCK_SIZE):
            if (y1 >= y2) and (y1 < y2 + BLOCK_SIZE):
                return True
        elif (x1 <= x2) and (x1 > x2 + BLOCK_SIZE):
            if (y1 <= y2) and (y1 > y2 + BLOCK_SIZE):
                return True

        return False

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()

        if self.is_collision(self.snake.block_x[0], self.snake.block_y[0], self.apple.apple_x, self.apple.apple_y):
            self.snake.add_length()
            self.apple.move()

        for i in range(1, self.snake.length):
            if self.is_collision(self.snake.block_x[0], self.snake.block_y[0], self.snake.block_x[i], self.snake.block_y[i]):
                raise "game over"

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f'Score: {self.snake.length}', True, WHITE)
        self.surface.blit(score, (20, 20))
        pygame.display.flip()

    def show_game_over(self):
        self.surface.fill(BACKGROUND_COLOR)
        font = pygame.font.SysFont("arial", 30)

        line1 = font.render(f'GAME OVER. Your score is {self.snake.length}', True, WHITE)
        line2 = font.render(f'To try again press ENTER.', True, WHITE)
        line3 = font.render(f'In other case press ESCAPE.', True, WHITE)

        self.surface.blit(line1, (100, 100))
        self.surface.blit(line2, (100, 150))
        self.surface.blit(line3, (100, 200))
        pygame.display.flip()

    def reset_game(self):
        self.snake = Snake(self.surface, 3)
        self.apple = Apple(self.surface)

    def run(self):
        running = True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        pause = False
                    if event.key == K_ESCAPE:
                        running = False
                    if not pause:
                        if event.key == K_UP:
                            self.snake.move_up()
                        if event.key == K_DOWN:
                            self.snake.move_down()
                        if event.key == K_LEFT:
                            self.snake.move_left()
                        if event.key == K_RIGHT:
                            self.snake.move_right()

            time.sleep(GAME_SPEED)

            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset_game()


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
