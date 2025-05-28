import pygame
import Spreadsheet

class Fighter:
    def __init__(self, window):

        self.window = window
        # Loading sheets for idle and running
        self.sprite_sheet_image_idle = pygame.image.load("Forest_Runner_Sprites/Fighter/Idle.png").convert_alpha()
        self.sprite_sheet_image_run = pygame.image.load("Forest_Runner_Sprites/Fighter/Run.png").convert_alpha()
        self.sprite_sheet_image_jump = pygame.image.load("Forest_Runner_Sprites/Fighter/Jump.png").convert_alpha()
        self.sprite_sheet_image_attack_1 = pygame.image.load("Forest_Runner_Sprites/Fighter/Attack_1.png").convert_alpha()
        self.sprite_sheet_image_attack_2 = pygame.image.load("Forest_Runner_Sprites/Fighter/Attack_2.png").convert_alpha()
        self.sprite_sheet_image_attack_3 = pygame.image.load("Forest_Runner_Sprites/Fighter/Attack_3.png").convert_alpha()
        self.sprite_sheet_image_shield = pygame.image.load("Forest_Runner_Sprites/Fighter/Shield.png").convert_alpha()

        # Getting and setting image of character sprite in spritesheets
        self.sprite_sheet_idle = Spreadsheet.SpriteSheet(self.sprite_sheet_image_idle)
        self.sprite_sheet_run = Spreadsheet.SpriteSheet(self.sprite_sheet_image_run)
        self.sprite_sheet_jump = Spreadsheet.SpriteSheet(self.sprite_sheet_image_jump)
        self.sprite_sheet_attack_1 = Spreadsheet.SpriteSheet(self.sprite_sheet_image_attack_1)
        self.sprite_sheet_attack_2 = Spreadsheet.SpriteSheet(self.sprite_sheet_image_attack_2)
        self.sprite_sheet_attack_3 = Spreadsheet.SpriteSheet(self.sprite_sheet_image_attack_3)
        self.sprite_sheet_shield = Spreadsheet.SpriteSheet(self.sprite_sheet_image_shield)

        # Sprite list that holds action spritesheets
        self.sprite_list = [self.sprite_sheet_idle, self.sprite_sheet_run, self.sprite_sheet_jump, self.sprite_sheet_attack_1, self.sprite_sheet_attack_2, self.sprite_sheet_attack_3, self.sprite_sheet_shield]

        self.animation_list = [] # List that holds animations
        self.animation_steps = [1, 8, 10, 4, 3, 4, 2] # List that holds the amount of frames within each animation
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 150 # Cooldown time between each animation
        self.frame = 0 # Init Frame counter so we start at the beginning of each animation
        self.BLACK = (0, 0, 0)
        self.action = 0 # Action number represents animation type (run, jump etc.)
        self.c_x = 540 # Player positioning
        self.c_y = 369 # Player positioning
        self.screen_width = self.window.get_width()
        self.character_width = 150
        self.facing_right = True # Tracking facing position state
        self.is_jumping = False # Tracking jumping state
        self.jump_height = 10 # Initialize inital jump height
        self.is_falling = False # Tracking falling state
        self.is_attacking = False # Tracking attack state
        self.is_shielding = False
        self.current_attack = 0 # Tracking attack type (jab l, jab r, kick)
        self.max_frames = 0 # Tracking maximum amount of frames in animation
        self.attack_timer = 0 # Tracking amount of time for each attack animation
        self.attack_duration = 20 # length of attack milliseconds
        self.speed = 5 # Player running speed


        # Populating animation list
        for i in range(len(self.animation_steps)):
            self.temp_list = []
            for j in range(self.animation_steps[i]):
                self.temp_list.append(self.sprite_list[i].get_image(j, 130, 127, 1.8, self.BLACK))

            self.animation_list.append(self.temp_list)
    
    
    
    
    def update(self, events):
        self.keys = pygame.key.get_pressed()

        self.action = 0


        # Shield Functionality
# Shielding when holding V
        if self.keys[pygame.K_v]:
            self.is_shielding = True
            self.action = 6
            self.frame %= self.animation_steps[6]  # Loop shield animation
        else:
            self.is_shielding = False

    
        

        # Attack 1,2 and 3 Functionality
        if not self.is_attacking:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        self.is_attacking = True
                        self.current_attack = 1
                        self.action = 3
                        self.attack_timer = 0
                        self.frame = 0
                    elif event.key == pygame.K_e:
                        self.is_attacking = True
                        self.current_attack = 2
                        self.action = 4
                        self.attack_timer = 0
                        self.frame = 0
                    elif event.key == pygame.K_c:
                        self.is_attacking = True
                        self.current_attack = 3
                        self.action = 5
                        self.attack_timer = 0
                        self.frame = 0


        
        if self.is_attacking:
            if self.current_attack == 1:
                self.action = 3
                self.max_frames = self.animation_steps[3]
            elif self.current_attack == 2:
                self.action = 4
                self.max_frames = self.animation_steps[4]
            elif self.current_attack == 3:
                self.action = 5
                self.max_frames = self.animation_steps[5]

            self.attack_timer += 1


            
            if self.attack_timer >= self.attack_duration or self.frame >= self.max_frames - 1:
                self.is_attacking = False
                self.attack_timer = 0
                self.current_attack = 0


        # Jumping Functionality
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_w:
                    self.is_jumping = True
                    self.jump_height = 10
                    
        if self.is_jumping:
            self.action = 2
            self.neg = 1
            if self.jump_height >= -10:
                self.neg = 1
                if self.jump_height < 0:
                    self.neg = -1
                self.c_y -= (self.jump_height ** 2) * 0.5 * self.neg  # Parabolic jump
                self.jump_height -= 1

                if self.jump_height < -10:
                    self.is_jumping = False
                    self.jump_height = 10
                    self.c_y = 369

        

        # Running Functionality
        if self.keys[pygame.K_d] or self.keys[pygame.K_RIGHT]:
            self.c_x += self.speed
            self.action = 1
            self.facing_right = True
        elif self.keys[pygame.K_a] or self.keys[pygame.K_LEFT]:
            self.c_x -= self.speed
            self.action = 1
            self.facing_right = False

            
        # Screen boundary functionality
        if self.c_x < -80:
            self.c_x = -80
        if self.c_x > self.screen_width - self.character_width:
            self.c_x = self.screen_width - self.character_width

        
        # Updating animation
        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.last_update >= self.animation_cooldown:
            self.frame += 1
            self.last_update = self.current_time
            if self.frame >= self.animation_cooldown:
                self.frame = 0
        
        if self.frame >= self.animation_steps[self.action]:
            self.frame = 0

            if self.action >=3 and self.action <=5:
                self.is_attacking = False
                self.current_attack = 0

    # Drawing character on the screen
    def draw(self):
        self.current_frame = self.animation_list[self.action][self.frame]

        # facing direction logic
        if not self.facing_right:
            self.current_frame = pygame.transform.flip(self.current_frame, True, False).convert_alpha()

        self.window.blit(self.current_frame, (self.c_x, self.c_y))
    
    
    

    
        

            
