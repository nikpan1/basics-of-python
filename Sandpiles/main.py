import pygame
from sys import exit

x_size, y_size = 140, 140  # rozmiar przestrzeni
opp = 4  # rozmiar jednej kratki w px

x = 12      # value = 2^x wartość początkowa w środku sandpile
option = 1      # option - zmienna odpowiedzialna za kształt

value = pow(2, x)
zeros = (255, 255, 111)
ones = (89, 70, 255)
twos = (255, 100, 0)
threes = (129, 0, 132)


def pick(arr):
    if option == 0:
        return square(arr)
    if option == 1:
        return triangle(arr)
    if option == 2:
        return 0


def square(arr):
    print("SQUARE")
    size = x_size

    for p in range(0, size + 1):
        arr[p][size] = -1
        arr[p][0] = -1
        arr[size][p] = -1
        arr[0][p] = -1

    mid = int(size/2)   # środek figury w punkcie arr[mid][mid]
    arr[mid][mid] = value
    return arr


def triangle(arr):
    print("TRIANGLE")

    size = x_size
    half = int(size / 2)
    k = 0

    for g in range(0, size + 1):
        for h in range(0, size + 1):
            arr[g][h] = -1

    for i in range(1, size + 1):
        for j in range(1, size + 1):
            if j == half:
                for t in range(j, k + 1 + j):
                    arr[i][t] = 10
                half -= 1
                k += 2

    arr[half][half] = value
    return arr


def is_done(arr):
    for i in range(0, x_size + 1):
        for j in range(0, y_size + 1):
            if arr[i][j] > 3:
                return False
    return True


def sandpile(arr):
    print("SANDPILE")
    mid = int(x_size / 2)

    while True:
        if is_done(arr) is True:
            return arr
        old = arr
        print(arr[mid][mid])
        for k in range(0, x_size + 1):
            for m in range(0, y_size + 1):
                if old[k][m] > 3:
                    arr[k][m] -= 4

                    if old[k - 1][m] != -1:
                        arr[k - 1][m] += 1

                    if old[k + 1][m] != -1:
                        arr[k + 1][m] += 1

                    if old[k][m + 1] != -1:
                        arr[k][m + 1] += 1

                    if old[k][m - 1] != -1:
                        arr[k][m - 1] += 1


def main():
    print("Wczytane wartości:")
    print("x_size = {0}, \ny_size = {1}, \noption = {2}, \nvalue = {3}.".format(x_size, y_size, option, value))
    arr = [[0 for mx_fi in range(x_size + 1)] for ny_ni in range(y_size + 1)]

    pick(arr)
    sandpile(arr)
    # done
    print(arr)

    pygame.init()
    height, width = y_size * opp, x_size * opp
    screen = pygame.display.set_mode((height, width))
    pygame.display.set_caption('Sandpile')
    screen.fill('black')

    a = pygame.Surface((opp, opp))
    b = pygame.Surface((opp, opp))
    c = pygame.Surface((opp, opp))
    d = pygame.Surface((opp, opp))
    a.fill(zeros)
    b.fill(ones)
    c.fill(twos)
    d.fill(threes)

    for i in range(0, len(arr[0])):
        for j in range(0, len(arr[0])):
            if arr[i][j] == 0 or arr[i][j] == -1:
                screen.blit(a, (opp * i, opp * j))
            elif arr[i][j] == 1:
                screen.blit(b, (opp * i, opp * j))
            elif arr[i][j] == 2:
                screen.blit(c, (opp * i, opp * j))
            elif arr[i][j] == 3:
                screen.blit(d, (opp * i, opp * j))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


if __name__ == '__main__':
    main()
