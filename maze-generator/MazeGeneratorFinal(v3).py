# maze generator algorithm - Nikodem Panknin
import random


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
def r_direction(walls, pnt, ax_x, ax_y):
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
def maze(ax_x, ax_y, path, pointer, walls):
    a = r_direction(walls, pointer, ax_x, ax_y)

    if a != -1:
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

    else: # if a == -1 - cofanie się
        if len(path) == 0:
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

    return maze(ax_x, ax_y, path, pointer, walls)


def main():
    print('def main')
    ax_x, ax_y = 5, 5           # rozmiar labiryntu
    path = []                   # jakie miejsca były mijane - ścieżka
    pointer = [0, 0]            # gdzie się znajduje program w danym momencie
    walls = [[[1, 1, 1, 1] for m in range(ax_y)] for n in range(ax_y)]
    walls = maze(ax_x, ax_y, path, pointer, walls) # przechowująca labirynt tablica 3d o rozmiarach ax_x X ax_y X 4

    for i in range(0, ax_y):
        for j in range(0, ax_x):
            print(walls[j][i], end='')
        print(" ")
    #zapisanie do pliku tekstowego ^


if __name__ == '__main__':
    main()



