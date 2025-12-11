import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
import asteroidfield
import sys
from shot import Shot


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create a clock object to track time
    clock = pygame.time.Clock()

    # Initialize delta time
    dt = 0

    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Add player and asteroids to the groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    # Create new AsteroidField object
    asteroid = asteroidfield.AsteroidField()

    # Instantiate the player in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game loop
    while True:
        log_state()

        # Handle quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill the screen with solid black
        screen.fill("black")

        # Update player/group (rotation, movement)
        updatable.update(dt)

        # Player collision check
        for obj in asteroids:
            if obj.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        # Asteroid shot collision check
        for obj in asteroids:
            for shot in shots:
                if obj.collides_with(shot):
                    log_event("asteroid_shot")
                    obj.split()
                    shot.kill()

        # # Re-render the player on the screen each frame
        # player.draw(screen)

        # Draw all drawable objects
        for obj in drawable:
            obj.draw(screen)

        # Refresh the screen
        pygame.display.flip()

        # Limit the loop to 60 frames per second and calculate delta time
        # .tick(60) pauses the loop to maintain ~60 FPS
        # Returns the time elapsed since the last call in milliseconds
        # Dividing by 1000 converts it to seconds for frame-independent movement
        dt = clock.tick(60) / 1000
        #print(dt)

if __name__ == "__main__":
    main()
