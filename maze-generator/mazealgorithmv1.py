import random


def a_sum(array):
    s = 0
    for i in range(0, len(array)):
        s += array[i]
    return s


def r_direction(array):
    r_arr = []
    for i in range(0, 4):
        if array[i] == 1:
            r_arr.append(i)

    x = random.randint(0, len(r_arr) - 1)
    return r_arr[x]


def maze(sx, sy, path, pointer, walls):
    print('def maze')
    path.append(pointer)
    raffle = r_direction(walls[0][0])

    ans = 0
    if raffle == 0 and pointer[1] == 0:
        ans = 1
    elif raffle == 1 and pointer[1] == sx - 1:
        ans = 1
    elif raffle == 2 and pointer[0] == 0:
        ans = 1
    elif raffle == 3 and pointer[0] == sy - 1:
        ans = 1
    else:
        print("Error(0)")

    if ans == 1:
        path.pop(-1)
        maze(sx, sy, path, pointer, walls)

    # jeżeli nie mamy gdzie iść we go back
    # jeżeli klocki dookoła należą do path albo są borderem
    if ans == 2:
        path.pop(-1)
        pointer[0] = path[-1][0]
        pointer[1] = path[-1][1]
        maze(sx, sy, path, pointer, walls)

    walls[pointer[0]][pointer[1]][raffle] = 0
    if raffle == 0:
        walls[pointer[0]][pointer[1] + 1][3 - raffle] = 0
        pointer[1] += 1
    elif raffle == 1:
        walls[pointer[0] + 1][pointer[1]][3 - raffle] = 0
        pointer[1] += 1
    elif raffle == 2:
        walls[pointer[0]][pointer[1] - 1][3 - raffle] = 0
        pointer[0] += 1
    elif raffle == 3:
        walls[pointer[0] - 1][pointer[1]][3 - raffle] = 0
        pointer[0] += 1
    else:
        print("Error(1)")

    # pointer = point()
    # jeżeli wróciło do punktu wejścia to elo? albo jak path długości 4x


def main():
    print('def main')
    ax_x, ax_y = 5, 5           # rozmiar labiryntu
    path = []                   # jakie miejsca były mijane - ścieżka
    pointer = [0, 0]            # gdzie się znajduje program w danym momencie
    walls = [[[1, 1, 1, 1] for m in range(ax_y)] for n in range(ax_y)]
    maze(ax_x, ax_y, path, pointer, walls)


if __name__ == '__main__':
    main()
