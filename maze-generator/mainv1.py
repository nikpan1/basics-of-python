import pygame
import time
import random
from sys import exit


def close_statement():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


def move(x, y, add):
    y += add
    return x, y


def main():

    path = [[0, 0], [0, 1], [0, 2], [1, 2]]
    xsize, ysize = 13, 13
    t = 50
    height, width = 1000, 800

    pygame.init()

    screen = pygame.display.set_mode((height, width))
    pygame.display.set_caption('Maze generator')
    surface = pygame.Surface((width - 100, width - 100))
    screen.fill('firebrick1')
    surface.fill('gold1')

    # ____________________________
    a = 0
    if xsize >= ysize:
        a = int(((width - 100)/ysize) - 2)
    elif xsize < ysize:
        a = int(((width - 100)/xsize) - 2)

    wherenow = pygame.Surface((a, a))
    wherenow.fill('red')

    pointpath = pygame.Surface((a, a))
    pointpath.fill('yellow')
    # ____________________________

    mazeyline = pygame.Surface((width - 100, 2))
    mazexline = pygame.Surface((2, width - 100))

    fontone = pygame.font.Font(None, 50)
    fonttwo = pygame.font.Font(None, 30)
    title = fontone.render('Project', False, 'white')
    textone = fonttwo.render('Maze generator', False, 'White')
    texttwo = fonttwo.render(f'xsize = {xsize}', False, 'White')
    textthree = fonttwo.render(f'ysize = {ysize}', False, 'White')

    clock = pygame.time.Clock()
    # no to teraz ogarniamy współrzędne w kratce zerowej:
    xcord, ycord = 2, 2
    arrlen = (width - 100)/ysize
    # ____________________________

    screen.blit(surface, (50, 50))

    for i in range(0, ysize + 1):
        screen.blit(mazeyline, (50, 50 + i * ((width - 100) / ysize)))
    for i in range(0, xsize + 1):
        screen.blit(mazexline, (50 + i * ((width - 100) / xsize), 50))

    screen.blit(title, (width, t))
    screen.blit(textone, (width, t + 40))
    screen.blit(texttwo, (width, t + 70))
    screen.blit(textthree, (width, t + 110))
    pygame.display.update()
    while True:
        time.sleep(1)

        screen.blit(wherenow, (50 + xcord, 50 + ycord))

        close_statement()
        pygame.display.update()

        screen.blit(pointpath, (50 + xcord, 50 + ycord))
        xcord, ycord = move(xcord, ycord, arrlen)

        clock.tick(10)


if __name__ == '__main__':
    main()
