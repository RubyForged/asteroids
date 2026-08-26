import random
from typing import override

import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x,y,radius)

    @override
    def draw(self, screen: pygame.Surface ) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    @override
    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        random_angle = random.uniform(20,50)
        first_astroid_angle = self.velocity.rotate(random_angle)
        second_astroid_angle = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_astroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_astroid = Asteroid(self.position.x, self.position.y, new_radius)
        first_astroid.velocity = first_astroid_angle * 1.2
        second_astroid.velocity = second_astroid_angle * 1.2
