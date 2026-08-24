from constants import *
from logger import log_state
from player import Player
import pygame


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    player1 = Player( SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # gameloop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player1.update(dt)
        player1.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    # end gameloop

if __name__ == "__main__":
    main()
