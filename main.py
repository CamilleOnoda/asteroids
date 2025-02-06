import pygame
from constants import SCREEN_HEIGHT,SCREEN_WIDTH,ASTEROID_KINDS,\
ASTEROID_MAX_RADIUS,ASTEROID_MIN_RADIUS,ASTEROID_SPAWN_RATE


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    while True:
        screen.fill((0,0,0))
        pygame.display.flip()



if __name__ == "__main__":
    main()
