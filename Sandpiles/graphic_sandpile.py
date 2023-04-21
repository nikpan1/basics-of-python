import pygame
from sys import exit
zeros = (0, 0, 0)
ones = (240, 108, 108)
twos = (152, 62, 232)
threes = (30, 213, 36)


def main():
    arr = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [-1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, -1], [-1, 0, 0, 0, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, -1], [-1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, -1], [-1, 0, 0, 0, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, -1], [-1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, -1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

    pygame.init()
    height, width = 800, 800
    screen = pygame.display.set_mode((height, width))
    pygame.display.set_caption('Sandpile')
    screen.fill('black')

    a = pygame.Surface((3, 3))
    b = a
    c = b
    d = c
    a.fill(zeros)
    b.fill(ones)
    c.fill(twos)
    d.fill(threes)

    for i in range(0, len(arr[0])):
        for j in range(0, len(arr[0])):
            if arr[i][j] == 0:
                screen.blit(a, (3 * i + 1, 3 * j + 1))
            elif arr[i][j] == 1:
                screen.blit(b, (3 * i, 3 * j + 1))
            elif arr[i][j] == 2:
                screen.blit(c, (3 * i + 1, 3 * j + 1))
            elif arr[i][j] == 3:
                screen.blit(d, (3 * i, 3 * j + 1))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


if __name__ == '__main__':
    main()


"""    f = open('plik.txt', 'w')
    f.write(arr)

    with open('plik.txt', 'w') as f:
        for item in arr:
            f.write("%s\n" % item)"""
