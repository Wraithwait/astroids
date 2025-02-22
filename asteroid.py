import pygame
import random
from circleshape import CircleShape
from player import Player
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            return self.kill()
        else:   
            new_asteroid = max(self.radius // 2, ASTEROID_MIN_RADIUS)
            random_angle = random.uniform(20, 50)

            new_velocity1 = self.velocity.rotate(random_angle).normalize() * self.velocity.length() * 1.2
            new_velocity2 = self.velocity.rotate(-random_angle).normalize() * self.velocity.length() * 1.2

            asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroid)
            asteroid1.velocity = new_velocity1

            asteroid2 = Asteroid(self.position.x, self.position.y, new_asteroid)
            asteroid2.velocity = new_velocity2

            self.kill()

            return [asteroid1, asteroid2]
            
            


        



