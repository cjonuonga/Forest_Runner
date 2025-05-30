import pygame
import time
import random
import sys
import Spritesheet
from Fighter import Fighter

# Initializing Pygame
pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

# Setting up the screen
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Forest Fighter")
clock = pygame.time.Clock()

# Loading background image
background_img = pygame.image.load("Forest_pic.JPG")
# Scaling to fit the screen
background_img = pygame.transform.scale(background_img, (1200, 600))


fighter = Fighter(window)
running = True
while running:
    window.blit(background_img, (0, 0))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Update character/fighter movements and draw in window
    fighter.update(events)
    fighter.draw()
    

    # Displaying Character
    pygame.display.update()
    clock.tick(60)


