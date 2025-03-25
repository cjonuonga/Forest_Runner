import pygame
import time
import random
import sys

# Initializing Pygame
pygame.init()

# Setting up the screen
window = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Forest Runner")
clock = pygame.time.Clock()
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    window.fill((0, 0, 0))
    # Loading background image
    background_img = pygame.image.load("Forest_pic.JPG")
    # Scaling to fit the screen
    background_img = pygame.transform.scale(background_img, (1200, 600))
    window.blit(background_img, (0, 0))
    
    pygame.display.update()

