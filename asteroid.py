import pygame
import random
from circleshape import CircleShape
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            asteroid_1_velocity = self.velocity.rotate(angle)
            asteroid_2_velocity = self.velocity.rotate(angle * -1)
            new_asteroids_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position[0], self.position[1], new_asteroids_radius)
            asteroid_2 = Asteroid(self.position[0], self.position[1], new_asteroids_radius)
            asteroid_1.velocity = asteroid_1_velocity * 1.2
            asteroid_2.velocity = asteroid_2_velocity * 1.2