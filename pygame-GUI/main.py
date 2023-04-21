import pygame
from sys import exit

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Projekt')
    clock = pygame.time.Clock()
    screen.fill(WHITE)

    # BLACK = (0, 0, 0)
    thickness = 2       # thickness
    pos = [100, 100]    # place to generate
    line_length = 200   # length of the scroll bar
    end_height = 10     # height of the ends

    # scroll
    scroll_size = [end_height, end_height]
    scroll_pos = [pos[0] + line_length // 2, pos[1] - (end_height - 2) // 2]

    #

    line = pygame.Surface((line_length, thickness))
    line.fill(BLACK)

    end_line = pygame.Surface((thickness, end_height))
    end_line.fill(BLACK)

    scroll = pygame.Rect(scroll_pos, scroll_size)

    screen.blit(line, pos)
    pos[1] -= (end_height - 2) // 2
    screen.blit(end_line, pos)
    pos[0] += line_length
    screen.blit(end_line, pos)

    pygame.draw.rect(screen, BLACK, scroll)

    done = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == pygame.KEYDOWN:
                print(pygame.key.name(event.key))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("wciskam")
                done = False
            elif event.type == pygame.MOUSEBUTTONUP:
                print("puszczam")
                done = True
            if done:
                print("click!", pygame.mouse.get_pos())
                if scroll.collidepoint(pygame.mouse.get_pos()):
                    print("trafiłeś")

        pygame.display.update()
        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()

"""                print("click!", pygame.mouse.get_pos())
                if scroll.collidepoint(pygame.mouse.get_pos()):
                    print("trafiłeś")
"""