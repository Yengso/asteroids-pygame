import pygame
import random
from constants import *
from circleshape import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            vector1 = self.velocity.rotate(random_angle)
            vector2 = self.velocity.rotate(-random_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

            new_asteroid_1.velocity = vector1 * 1.2
            new_asteroid_2.velocity = vector2 * 1.2
            return new_asteroid_1, new_asteroid_2


    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        return pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)