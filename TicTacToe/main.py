import pygame
from pygame.locals import *
from sys import exit


def close_statement():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


def disp(screen):
    y_lines = pygame.Surface((6, 400))
    y_lines.fill('black')
    x_lines = pygame.Surface((400, 6))
    x_lines.fill('black')
    for p in range(0, 4):
        screen.blit(y_lines, (50 + 132 * p, 50))
        screen.blit(x_lines, (50, 50 + 132 * p))
    pygame.display.update()


def draw(screen, mx, my):
    print("draw, {0}, {1}".format(mx, my))


def main():
    array = [[0 for m in range(3)] for n in range(3)]

    pygame.init()
    pygame.display.set_caption('tictactoe')
    screen = pygame.display.set_mode((500, 500), 0, 32)
    screen.fill('White')
    tic = pygame.image.load('photos/Tic.png').convert()
    toe = pygame.image.load('photos/Toe.png').convert()
    disp(screen)
    while True:
        mx, my = 0, 0
        close_statement()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    draw(screen, mx, my)


if __name__ == '__main__':
    main()
