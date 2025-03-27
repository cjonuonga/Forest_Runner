import pygame
import Spreadsheet

class Fighter:
    def __init__(self, window):

        self.window = window
        # Loading sheets for idle and running
        self.sprite_sheet_image_idle = pygame.image.load("fighter_sheets/Idle.png").convert_alpha()
        self.sprite_sheet_image_run = pygame.image.load("fighter_sheets/Run.png").convert_alpha()

        # Getting and setting image of character sprite in spritesheets
        self.sprite_sheet_idle = Spreadsheet.SpriteSheet(self.sprite_sheet_image_idle)
        self.sprite_sheet_run = Spreadsheet.SpriteSheet(self.sprite_sheet_image_run)

        # Sprite list that holds action spritesheets
        self.sprite_list = [self.sprite_sheet_idle, self.sprite_sheet_run]

        # Creating animation list
        self.animation_list = []
        self.animation_steps = [1,8]
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 150
        self.frame = 0
        self.BLACK = (0, 0, 0)
        self.action = 0
        # Fighter (character position)
        self.c_x = 0
        self.c_y = 369
        self.facing_right = True
        self.speed = 5

        vel_x = 0

        for i in range(len(self.animation_steps)):
            self.temp_list = []
            for j in range(self.animation_steps[i]):
                self.temp_list.append(self.sprite_list[i].get_image(j, 130, 127, 1.8, self.BLACK))

            self.animation_list.append(self.temp_list)
    
    
    
    
    def update(self):
        self.keys = pygame.key.get_pressed()

        self.action = 0

        if self.keys[pygame.K_d] or self.keys[pygame.K_RIGHT]:
            self.c_x += self.speed
            self.action = 1
            self.facing_right = True
        elif self.keys[pygame.K_a] or self.keys[pygame.K_LEFT]:
            self.c_x -= self.speed
            self.action = 1
            self.facing_right = False
        
        
        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.last_update >= self.animation_cooldown:
            self.frame += 1
            self.last_update = self.current_time
            if self.frame >= self.animation_cooldown:
                self.frame = 0
        
        if self.frame >= self.animation_steps[self.action]:
            self.frame = 0

    def draw(self):
        self.current_frame = self.animation_list[self.action][self.frame]

        if not self.facing_right:
            self.current_frame = pygame.transform.flip(self.current_frame, True, False).convert_alpha()

        self.window.blit(self.current_frame, (self.c_x, self.c_y))
    
    
    

    
        

            
