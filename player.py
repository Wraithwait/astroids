import pygame
from circleshape import CircleShape
from constants import PLAYER_SHOOT_SPEED
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import PLAYER_RADIUS
from constants import PLAYER_SHOOT_COOLDOWN
import constants
import inspect

print("Loading constants from:", inspect.getfile(constants))
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):
        #print(f"Rotating with dt: {dt}, speed: {PLAYER_TURN_SPEED * dt}")
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt): # this should be on the bottom
        keys = pygame.key.get_pressed()
        # Rotate Left and Right
        if keys[pygame.K_a]:
            #print("A key pressed")
            self.rotate(-dt)
        if keys[pygame.K_d]:
            #print("D key pressed")
            self.rotate(dt)

        # Move Forward and backwards
        if keys[pygame.K_w]:
            #print("W key pressed")
            self.move(dt)
        if keys[pygame.K_s]:
            #print("S key pressed")
            self.move(-dt)

        # Decrement Shoot Timer
        if self.shoot_timer > 0:
            self.shoot_timer -= dt

    def shoot(self):
    # Debug PLAYER_SHOOT_SPEED
        #try:
        #    print(f"PLAYER_SHOOT_SPEED = {PLAYER_SHOOT_SPEED}")  # Test if it's accessible.
        #except NameError:
        #    print("PLAYER_SHOOT_SPEED is not accessible here!")
        if self.shoot_timer > 0:
            return None
        else:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            velocity = forward * PLAYER_SHOOT_SPEED
            shot = Shot(self.position.x, self.position.y, velocity)
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN
            return shot 