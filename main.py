import pygame
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    updatable  = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)
    asteroid_field = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        dt = clock.tick(60) / 1000.0
        updatable.update(dt)
        screen.fill((255, 192, 203))

        for obj in asteroids:
            if player.check_for_collision(obj):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if obj.check_for_collision(shot):
                    obj.split()
                    shot.kill()

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()   


if __name__ == "__main__":
    main()
