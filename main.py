import pygame
from constants import SCREEN_HEIGHT,SCREEN_WIDTH,ASTEROID_KINDS,\
ASTEROID_MAX_RADIUS,ASTEROID_MIN_RADIUS,ASTEROID_SPAWN_RATE
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    while True:
        screen.fill((0,0,0))

        x = SCREEN_WIDTH / 2
        y = SCREEN_HEIGHT / 2
        player = Player(x,y)
        player.draw(screen)
        
        pygame.display.flip()
        clock = pygame.time.Clock()
        dt = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            delta_time = clock.tick(60)
            dt = delta_time / 1000


if __name__ == "__main__":
    main()
