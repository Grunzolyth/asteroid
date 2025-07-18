# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# import the connect_database function
# and the database_version variable
# from database.py into the current file

# from database import connect_database, database_version
import constants
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    while True:
        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
