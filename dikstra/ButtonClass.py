# Button
import pygame


class Button:
    def __init__(self, parent_screen, x_pos, y_pos, x_size, y_size, color):
        self.color = color
        self.screen = parent_screen
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_size = x_size
        self.y_size = y_size

    def draw(self):
        pygame.draw.rect(self.screen, self.color, [self.x_pos, self.y_pos, self.x_size, self.y_size])

    # czy mouse pos może tak być?
    def is_interaction(self, mouse_pos):
        if mouse_pos[0] in range(self.x_pos, self.x_pos + self.x_size + 1):
            if mouse_pos[1] in range(self.y_pos, self.y_pos + self.y_size + 1):
                # print("Jest interakcja!")
                return True
        return False

# https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/
