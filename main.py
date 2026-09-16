import sys

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from logger import log_state
from player import Player
import pygame
from logger import log_event
from shot import Shot



def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    Player.containers = (updatable, drawable)
    player1 = Player( SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    shots = pygame.sprite.Group()
    Shot.containers = (shots, drawable, updatable)



    # gameloop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for astroid in asteroids:
            if astroid.collides_with(player1):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(astroid):
                    shot.kill()
                    astroid.split()
                    log_event("asteroid_shot")
        for drawme in drawable:
            drawme.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    # end gameloop

if __name__ == "__main__":
    main()


# comment #1 for boot.dev daily streak day off.
