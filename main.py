import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


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

        # Re-render the player on the screen each frame
        player.draw(screen)

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
