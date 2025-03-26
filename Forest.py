import pygame
import time
import random
import sys
import Spreadsheet

# Initializing Pygame
pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

# Setting up the screen
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Forest Runner")
clock = pygame.time.Clock()

# Loading background image
background_img = pygame.image.load("Forest_pic.JPG")
# Scaling to fit the screen
background_img = pygame.transform.scale(background_img, (1200, 600))

# Loading sheets for idle and running
sprite_sheet_image_idle = pygame.image.load("fighter_sheets/Idle.png").convert_alpha()
sprite_sheet_image_run = pygame.image.load("fighter_sheets/Run.png").convert_alpha()

# Getting and setting image of character sprite in spritesheets
sprite_sheet_idle = Spreadsheet.SpriteSheet(sprite_sheet_image_idle)
sprite_sheet_run = Spreadsheet.SpriteSheet(sprite_sheet_image_run)

# Sprite list that holds action spriteshees
sprite_list = [sprite_sheet_idle, sprite_sheet_run]

BLACK = (0, 0, 0)

# 130 x 127

# Creating animation list
animation_list = []
animation_steps = [1,8]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 150
frame = 0


# Handling controls and movement
keys = pygame.key.get_pressed()
vel_x = 0

# Looping through amount of steps within each sprite sheet
for i in range(len(animation_steps)):
    temp_list = []
    for j in range(animation_steps[i]):
        temp_list.append(sprite_list[i].get_image(j, 130, 127, 1.8, BLACK))
    
    animation_list.append(temp_list)


c_x = 0
c_y = 369
facing_right = True
speed = 5


running = True
while running:
    window.blit(background_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Storing key pressed state
    keys = pygame.key.get_pressed()

    action = 0 # Defualt action idle

    # Controlling the Fighter
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        c_x += speed
        action = 1
        facing_right = True
    elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
        c_x -= speed
        action = 1
        facing_right = False
    
    
    # Update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= animation_cooldown:
            frame = 0

    if frame >= animation_steps[action]:
        frame = 0

    # Getting current frame from animation list
    current_frame = animation_list[action][frame]

    # Flip the sprite
    if not facing_right:
        current_frame = pygame.transform.flip(current_frame, True, False).convert_alpha()
    
    window.blit(current_frame, (c_x, c_y))
    

    # Displaying Character
    pygame.display.update()
    clock.tick(60)


pygame.quit()
sys.exit()


