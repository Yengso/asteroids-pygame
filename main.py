import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
import sys



def main():
    pygame.init()
    pygame.display.set_mode()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Ateroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    

    clock_object = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable,)
    Shot.containers = (updateable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroid_field = AsteroidField()
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        updateable.update(dt)
        for drawables in drawable:
            drawables.draw(screen)
        for asteroid in asteroids:
            if  asteroid.collision_check(player):
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if asteroid.collision_check(shot):
                    pygame.sprite.Sprite.kill(shot)
                    split_result = asteroid.split()
                    if split_result:
                        asteroid1, asteroid2 = split_result
                        asteroids.add(asteroid1, asteroid2)
                        
        pygame.display.flip()
        clock_object.tick(60)
        dt = clock_object.tick(60) / 1000

    
if __name__ == "__main__":
    main()
