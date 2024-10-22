#! /usr/bin/env python
import pygame
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
from constants import *
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

def main():
	pygame.init()
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	while True:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return
		pygame.Surface.fill(screen, (0, 0, 0))
		pygame.display.flip()
if __name__ == "__main__":
	main()
