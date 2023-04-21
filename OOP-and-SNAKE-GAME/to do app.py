import pygame
from sys import exit


class Button:
    def __init__(self, x_cord, y_cord, wtd):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.wtd = wtd


class Tab:
    limit = 5
    times = 0

    pt = pygame.Surface((800, 80))
    pt.fill('gold')

    def __init__(self, screen):
        x_cord, y_cord = 80, self.times * 84 + 86
        time += 1
        screen.blit(self.pt, (80, self.times * 84 + 86))
        pass


def main():
    pygame.init()
    height, width = 1000, 800
    screen = pygame.display.set_mode((height, width))
    pygame.display.set_caption('To Do App')
    screen.fill('firebrick1')

    font_one = pygame.font.Font(None, 50)
    title = font_one.render('To do App', False, 'white')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pass
        screen.blit(title, (100, 50))
        screen.blit(pt, (80, times * 84 + 86))
        screen.blit(pt, (80, 1 * 84 + 86))
        screen.blit(pt, (80, 2 * 84 + 86))
        screen.blit(pt, (80, 3 * 84 + 86))
        pygame.display.update()


if __name__ == '__main__':
    main()

