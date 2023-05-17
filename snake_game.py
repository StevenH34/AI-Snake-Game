import pygame
import random



def main():
    # Initialize Pygame
    pygame.init()

    # Set the width and height of the game window
    width = 640
    height = 480

    # Create the game window
    game_window = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Snake Game')

    # main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

     # Clear the game window
    game_window.fill(black)


if __name__=="__main__":
    # call the main function
    main()