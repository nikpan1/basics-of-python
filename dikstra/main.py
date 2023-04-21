# main
import pygame
from ButtonClass import Button


WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
BUTTON_SIZE = 20

BACKGROUND_COLOR = (60, 25, 60)
BUTTON_COLOR_ONE = (100, 100, 100)
BUTTON_COLOR_TWO = (170, 170, 170)
BLACK = (0, 0, 0)
RED = (200, 10, 0)
GREEN = (20, 200, 0)


class Page:
    def __init__(self, x_axis, y_axis):
        self.x_axis = x_axis
        self.y_axis = y_axis

        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.screen.fill(BACKGROUND_COLOR)

        # init main array
        x_zero = int((WINDOW_WIDTH - x_axis * (BUTTON_SIZE + 2)) / 2)
        y_zero = (WINDOW_HEIGHT - y_axis * (BUTTON_SIZE + 2))

        self.buttons = [
            [Button(self.screen, x_zero + a * (BUTTON_SIZE + 2),
                    y_zero + b * (BUTTON_SIZE + 2), BUTTON_SIZE, BUTTON_SIZE, BUTTON_COLOR_ONE) for b in range(self.y_axis)]
            for a in range(self.x_axis)]

        for a in range(self.x_axis):
            self.buttons[a][0].color = BLACK
            self.buttons[a][self.y_axis - 1].color = BLACK
        for b in range(self.y_axis):
            self.buttons[0][b].color = BLACK
            self.buttons[self.x_axis - 1][b].color = BLACK

        self.buttons[1][1].color = RED
        self.buttons[self.x_axis - 2][self.y_axis - 2].color = RED

    def gen(self):
        for a in range(self.x_axis):
            for b in range(self.y_axis):
                self.buttons[a][b].draw()
        pygame.display.update()

    def change_to_green(self, a, b):
        if self.buttons[a][b].color == BUTTON_COLOR_ONE:
            self.buttons[a][b].color = GREEN
            self.buttons[a][b].draw()
            pygame.display.update()

        """
        elif self.buttons[a][b].color == GREEN:
            self.buttons[a][b].color = BUTTON_COLOR_ONE
            self.buttons[a][b].draw()
            pygame.display.update()
        """

    def run(self):
        self.gen()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                    running = False

                if event.type == pygame.K_SPACE:
                    # tu się będzie zaczynać program
                    pass

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    clicked = True
                    while clicked:
                        mouse_pos = pygame.mouse.get_pos()
                        for a in range(self.x_axis):
                            for b in range(self.y_axis):
                                if self.buttons[a][b].is_interaction(mouse_pos):
                                    self.change_to_green(a, b)
                        for e in pygame.event.get():
                            if e.type == pygame.MOUSEBUTTONUP:
                                clicked = False
                if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                    print("nadusiles prawy")
        pygame.quit()


def automate(x_zero, y_zero):
    x = int((WINDOW_WIDTH - x_zero) / (BUTTON_SIZE + 2))
    y = int((WINDOW_HEIGHT - y_zero) / (BUTTON_SIZE + 2))
    return x, y


def main():
    # u can also change the size of the array manually x, y = ...
    x, y = automate(0, 0)
    app = Page(x, y)
    app.run()


if __name__ == '__main__':
    main()


