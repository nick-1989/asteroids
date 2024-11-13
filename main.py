#! /usr/bin/env python
import sys
import pygame
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

def main():
	pygame.init()
	clock = pygame.time.Clock()

	asteroids = pygame.sprite.Group()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	shots = pygame.sprite.Group()

	Asteroid.containers = (asteroids, updatable, drawable)
	Shot.containers = (shots, updatable, drawable)
	AsteroidField.containers = updatable
	asteroid_field = AsteroidField()

	dt = 0
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
					return
		for obj in updatable:
			obj.update(dt)

		for asteroid in asteroids:
			if asteroid.collision(player):
				print("Game over!")
				sys.exit()

			for shot in shots:
				if asteroid.collision(shot):
					shot.kill()
					asteroid.split()
	
		pygame.Surface.fill(screen, (0, 0, 0))
		
		for obj in drawable:
			obj.draw(screen)
	
		pygame.display.flip()
		dt = clock.tick(60)/1000

if __name__ == "__main__":
	main()
