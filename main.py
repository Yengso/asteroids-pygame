import pygame
from constants import *



def main():
    pygame.init()
    pygame.display.set_mode()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        screen.fill((0, 0, 0))
        pygame.display.flip()

    print("Starting Ateroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    PRINT(f"Screen height: {SCREEN_HEIGHT}")
if __name__ == "__main__":
    main()
