import pygame
import time
import random
from sys import exit


def close_statement():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


def text(screen, width, t, xsize, ysize):
    fontone = pygame.font.Font(None, 50)
    fonttwo = pygame.font.Font(None, 30)
    title = fontone.render('Project', False, 'white')
    textone = fonttwo.render('Maze generator', False, 'White')
    texttwo = fonttwo.render(f'xsize = {xsize}', False, 'White')
    textthree = fonttwo.render(f'ysize = {ysize}', False, 'White')

    screen.blit(title, (width, t))
    screen.blit(textone, (width, t + 40))
    screen.blit(texttwo, (width, t + 70))
    screen.blit(textthree, (width, t + 110))


def maze_surface(screen, height, width, xsize, ysize):
    mazeyline = pygame.Surface((width - 100, 2))
    mazexline = pygame.Surface((2, width - 100))

    surface = pygame.Surface((width - 100, width - 100))
    surface.fill('gold1')

    screen.blit(surface, (50, 50))

    for i in range(0, ysize + 1):
        screen.blit(mazeyline, (50, 50 + i * ((width - 100) / ysize)))
    for i in range(0, xsize + 1):
        screen.blit(mazexline, (50 + i * ((width - 100) / xsize), 50))


def main():
    path = [[0, 0], [0, 1], [0, 2], [1, 2]]
    t = 50
    a = 0

    pygame.init()
    xsize, ysize = 25, 25
    height, width = 1000, 800

    screen = pygame.display.set_mode((height, width))
    pygame.display.set_caption('Maze generator')
    screen.fill('firebrick1')
    clock = pygame.time.Clock()

    # jako punktów surface program bierze mniejszy wymiar
    if xsize >= ysize:
        a = int(((width - 100)/ysize) - 2)
    elif xsize < ysize:
        a = int(((width - 100)/xsize) - 2)

    wherenow = pygame.Surface((a, a))
    wherenow.fill('red')

    pointpath = pygame.Surface((a, a))
    pointpath.fill('yellow')

    # współrzędne w kratce zerowej:
    xcord, ycord = 2, 2
    # rozmiar o ile się punkty od siebie mieszczą
    arrlen = (width - 100)/ysize

    maze_surface(screen, height, width, xsize, ysize)
    text(screen, width, t, xsize, ysize)
    pygame.display.update()

    while True:
        close_statement()
        time.sleep(0.5)
        screen.blit(wherenow, (50 + xcord, 50 + ycord))
        pygame.display.update()

        screen.blit(pointpath, (50 + xcord, 50 + ycord))
        clock.tick(10)


if __name__ == '__main__':
    main()
