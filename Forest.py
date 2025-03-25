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

# Loading background image
background_img = pygame.image.load("Forest_pic.JPG")
# Scaling to fit the screen
background_img = pygame.transform.scale(background_img, (1200, 600))


def get_image(sheet, x, y, width, height, scale):
    image = pygame.Surface((width, height), pygame.SRCALPHA)
    image.blit(sheet, (0, 0), (x, y, width, height))

    if scale != 1:
        new_width = int(width * scale)
        new_height = int(height * scale)
        image = pygame.transform.scale(image,(new_width, new_height))
    return image

# Loading sprite sheet
sprite_sheet = pygame.image.load("Idle.png").convert_alpha()

class Runner(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Setting up sprite height and width
        self.sprite_width = 130
        self.sprite_height = 127
        
        # Loading running frames
        self.running_frames = []
        scale = 1.8
        for i in range(6):
            frame = get_image(sprite_sheet, i * self.sprite_width, 0, self.sprite_width, self.sprite_height, scale)
            self.running_frames.append(frame)
        self.current_frame = 0
        self.image = self.running_frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0, 600) # Posiitions the character.

        self.position = self.rect.bottomleft


        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 100
    
    def update(self):   # Animation Settings
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update > self.frame_rate:
            self.last_update = current_time
            
            # Saving bottom position (ensuring idle position)
            bottom = self.rect.bottom
            left = self.rect.left
            
            # Updating the frame
            self.current_frame = (self.current_frame + 1) % len(self.running_frames)
            self.image = self.running_frames[self.current_frame]

            # Getting the new rect and restoring the position
            self.rect = self.image.get_rect()
            self.rect.bottomleft = self.position


all_sprites = pygame.sprite.Group()
player = Runner()

all_sprites.add(player)
    

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    all_sprites.update()
    window.blit(background_img, (0, 0))
    all_sprites.draw(window)

    pygame.display.update()
    clock.tick(60)
pygame.quit()
sys.exit()

