import pygame
from constants import *



def main():
    pygame.init()
    pygame.display.set_mode()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock_object = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        pygame.display.flip()
        clock_object.tick(60)
        dt = clock_object.tick(60) / 1000

    print("Starting Ateroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    PRINT(f"Screen height: {SCREEN_HEIGHT}")
if __name__ == "__main__":
    main()
