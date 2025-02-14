# Imports
import sys
import pygame
import constants
from asteroidfield import *
from player import *
from asteroid import Asteroid
from constants import *

def main():
    # Initilization
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Variables
    dt = 0

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()

    # Containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroid_group, updatable, drawable)
    AsteroidField.containers = (updatable)
    

    # Messages
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Player Initilization
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    # Asteroid Field Initilization
    asteroid_field = AsteroidField()


    # Gameplay Loop

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Update the player
        updatable.update(dt)

        # Check for Collisions
        for asteroid in asteroid_group:
            if player.collision(asteroid):
                print("Collision detected between player and asteroid")
                print("Game Over!")
                sys.exit()

        # Render the Display    
        screen.fill((0,0,0))

        # Render the Player
        for sprite in drawable:
            sprite.draw(screen)

        # Update the Game
        dt = clock.tick(60) / 1000 # divide by 1000 miliseconds to convert to seconds.
        fps = 1 / dt if dt > 0 else 0
        print(f"Frames per second: {fps}")
        pygame.display.flip()

if __name__ == "__main__":
    main()

