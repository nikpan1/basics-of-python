import time

import pygame
import random

height, width = 800, 800
screen = pygame.display.set_mode((height, width))
screen.fill('black')


def close_statement():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


def pr_arr(arr, title):
    back = pygame.Surface((400, 50))
    back.fill('black')
    screen.blit(back, (0, 0))
    font = pygame.font.Font(None, 30)
    text = font.render(title, False, 'Green')
    screen.blit(text, (55, 28))
    surface = pygame.Surface((width - 100, width - 100))
    surface.fill('white')
    screen.blit(surface, (50, 50))

    position = [54, 750]
    th = 6  # thickness
    for k in range(1, len(arr)):
        pos = pygame.Surface((th, th*arr[k]))
        pos.fill('red')
        position[1] = 750 - th*arr[k]
        screen.blit(pos, position)
        position[0] += th + 1

    pygame.display.update()
    time.sleep(0.01)


def bubble_sort(our_list):
    # We go through the list as many times as there are elements
    for i in range(len(our_list)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(our_list) - 1):
            if our_list[j] > our_list[j+1]:
                # Swap
                our_list[j], our_list[j+1] = our_list[j+1], our_list[j]
                pr_arr(our_list, "bubble_sort")


def min(arr):
    minimum = 100
    index = 0
    for h in range(len(arr)):
        if minimum > arr[h]:
            minimum = arr[h]
            index = h
    return index


# sortowanie przez wybor
def selection_sort(arr):
    a = 0
    for p in range(0, len(arr)):
        index = p + min(arr[p:len(arr)])
        a = arr[index]
        arr[index] = arr[p]
        arr[p] = a
        pr_arr(arr, "sort")


def main():
    pygame.init()
    pygame.display.set_caption('Sorting_Algorithm')

    surface = pygame.Surface((width - 100, width - 100))
    surface.fill('white')
    screen.blit(surface, (50, 50))
    pygame.display.update()

    arr = []
    for i in range(0, 100):
        n = random.randint(1, 100)
        arr.append(n)

    pr_arr(arr, "sorting")

    choice = "1"
    if choice == "0":
        bubble_sort(arr)
    elif choice == "1":
        selection_sort(arr)

    while True:
        close_statement()


if __name__ == '__main__':
    main()
