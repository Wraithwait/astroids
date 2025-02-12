# Imports
import pygame
import constants

from constants import *

def main():
    # Initilization
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Gameplay Loop

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Player Inputs

        # Render the Display
        screen.fill((0,0,0))

        # Update the Game
        pygame.display.flip()

if __name__ == "__main__":
    main()

