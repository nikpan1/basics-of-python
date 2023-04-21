# maze generator algorithm - Nikodem Panknin
import pygame
import random
import time
from sys import exit


ax_x, ax_y = 35, 35  # rozmiar labiryntu
height, width = 1000, 800
screen = pygame.display.set_mode((height, width))


def close_statement():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


def text():
    fontone = pygame.font.Font(None, 50)
    fonttwo = pygame.font.Font(None, 30)
    title = fontone.render('Project', False, 'white')
    textone = fonttwo.render('Maze generator', False, 'White')
    texttwo = fonttwo.render(f'xsize = {ax_x}', False, 'White')
    textthree = fonttwo.render(f'ysize = {ax_y}', False, 'White')

    t = 50
    screen.blit(title, (width, t))
    screen.blit(textone, (width, t + 40))
    screen.blit(texttwo, (width, t + 70))
    screen.blit(textthree, (width, t + 110))


def maze_surface():
    mazeyline = pygame.Surface((width - 100, 2))
    mazexline = pygame.Surface((2, width - 100))

    surface = pygame.Surface((width - 100, width - 100))
    surface.fill('gold1')

    screen.blit(surface, (50, 50))

    for i in range(0, ax_y + 1):
        screen.blit(mazeyline, (50, 50 + i * ((width - 100) / ax_y)))
    for i in range(0, ax_x + 1):
        screen.blit(mazexline, (50 + i * ((width - 100) / ax_x), 50))


def move(pointer, path):
    a = 0
    if ax_x >= ax_y:
        a = (width - 100) / ax_y - 2
    elif ax_x < ax_y:
        a = (width - 100) / ax_x - 2

    where_now = pygame.Surface((a, a))
    where_now.fill('red')

    xcord, ycord = 2 + 50, 2 + 50
    length = (width - 100) / ax_y

    if path[-1] == 0:
        point_path = pygame.Surface((a, a + 2))
        point_path.fill('yellow')
        screen.blit(point_path, (xcord + pointer[0] * length, ycord + (pointer[1] + 1) * length - 2))
    elif path[-1] == 1:
        point_path = pygame.Surface((a + 2, a))
        point_path.fill('yellow')
        screen.blit(point_path, (xcord + (pointer[0] - 1) * length, ycord + pointer[1] * length))
    elif path[-1] == 2:
        point_path = pygame.Surface((a, a + 2))
        point_path.fill('yellow')
        screen.blit(point_path, (xcord + pointer[0] * length, ycord + (pointer[1] - 1) * length))
    elif path[-1] == 3:
        point_path = pygame.Surface((a + 2, a))
        point_path.fill('yellow')
        screen.blit(point_path, (xcord + (pointer[0] + 1) * length - 2, ycord + pointer[1] * length))

    screen.blit(where_now, (xcord + pointer[0]*length, ycord + pointer[1]*length))
    pygame.display.update()
    time.sleep(0.05)


def go_back(pointer):
    a = 0
    if ax_x >= ax_y:
        a = (width - 100) / ax_y - 2
    elif ax_x < ax_y:
        a = (width - 100) / ax_x - 2

    where_now = pygame.Surface((a, a))
    where_now.fill('yellow')

    xcord, ycord = 2 + 50, 2 + 50
    length = (width - 100) / ax_y

    screen.blit(where_now, (xcord + pointer[0]*length, ycord + pointer[1]*length))

    pygame.display.update()


# suma
# funkcja sumuje wszystkie ścianki danego boku i sprawdza i zwraca tą wartość
def a_sum(array):
    s = 0
    for i in range(0, len(array)):
        s += array[i]
    return s


# losowanie, w którą stronę ma pójść spośród możliwych
# pnt [0] - współrzędne x
# pnt [1] - współrzędne y
def r_direction(walls, pnt):
    r_arr = [0, 1, 2, 3]

    # nie może pójść w lewo
    if pnt[0] == 0:
        r_arr.remove(3)
    elif a_sum(walls[pnt[0] - 1][pnt[1]]) != 4:
        r_arr.remove(3)

    # nie może pójść w prawo
    if pnt[0] == ax_x - 1:
        r_arr.remove(1)
    elif a_sum(walls[pnt[0] + 1][pnt[1]]) != 4:
        r_arr.remove(1)

    # nie może pójść w górę
    if pnt[1] == 0:
        r_arr.remove(0)
    elif a_sum(walls[pnt[0]][pnt[1] - 1]) != 4:
        r_arr.remove(0)

    # nie może pójść w dół
    if pnt[1] == ax_y - 1:
        r_arr.remove(2)
    elif a_sum(walls[pnt[0]][pnt[1] + 1]) != 4:
        r_arr.remove(2)

    if len(r_arr) == 0:
        return -1
    # jeżeli okaże się, że punkt nie ma gdzie się ruszyć, to cofaj się
    else:
        x = random.randint(0, len(r_arr) - 1)
        return r_arr[x]


# główna funkcja generatora
def maze(path, pointer, walls):
    a = r_direction(walls, pointer)

    if a != -1:
        # move(...)
        walls[pointer[0]][pointer[1]][a] = 0
        path.append(a)

        if a == 0:
            pointer = [pointer[0], pointer[1] - 1]
            walls[pointer[0]][pointer[1]][2] = 0
        elif a == 1:
            pointer = [pointer[0] + 1, pointer[1]]
            walls[pointer[0]][pointer[1]][3] = 0
        elif a == 2:
            pointer = [pointer[0], pointer[1] + 1]
            walls[pointer[0]][pointer[1]][0] = 0
        elif a == 3:
            pointer = [pointer[0] - 1, pointer[1]]
            walls[pointer[0]][pointer[1]][1] = 0

    else:  # if a == -1 - cofanie się
        go_back(pointer)
        if len(path) == 0:
            end = pygame.Surface((50, 50))  # ostatni pointer narysuj i 0, 0 na zielono
            end.fill('red')
            screen.blit(end, (52, 52))
            return walls

        b = path[-1]
        path.pop()
        if b == 0:
            pointer = [pointer[0], pointer[1] + 1]
        elif b == 1:
            pointer = [pointer[0] - 1, pointer[1]]
        elif b == 2:
            pointer = [pointer[0], pointer[1] - 1]
        elif b == 3:
            pointer = [pointer[0] + 1, pointer[1]]
    if a == -1:
        go_back(pointer)
    if len(path) != 0 and a != -1:
        move(pointer, path)
    return maze(path, pointer, walls)


def main():
    pygame.init()
    pygame.display.set_caption('Maze generator')
    screen.fill('firebrick1')
    maze_surface()
    text()
    pygame.display.update()

    path = []
    pointer = [0, 0]
    walls = [[[1, 1, 1, 1] for m in range(ax_y)] for n in range(ax_y)]
    walls = maze(path, pointer, walls)  # przechowująca labirynt tablica 3d o rozmiarach ax_x X ax_y X 4

    print(walls)
    while True:
        close_statement()


if __name__ == '__main__':
    main()
