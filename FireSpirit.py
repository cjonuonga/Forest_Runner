import pygame
import Spritesheet

class FireSpirit:
    def __init__(self, window):
        self.window = window

        # Loading sheets
        self.spirte_sheet_image_idle = pygame.image.load("Forest_Runner_Sprites/random_enemies/FireSpirit/Idle.png").convert_alpha()
        self.sprite_sheet_image_idle_2 = pygame.image.load("Forest_Runner_Sprites/random_enemies/FireSpirit/Idle_2.png").convert_alpha()
        self.sprite_sheet_image_run = pygame.image.load("Forest_Runner_Sprites/random_enemies/FireSpirit/Run.png").convert_alpha()
        self.sprite_sheet_image_shot = pygame.image.load("Forest_Runner_Sprites/random_enemies/FireSpirit/Shot.png").convert_alpha()
        self.sprite_sheet_image_walk = pygame.image.load("Forest_Runner_Sprites/random_enemies/FireSpirit/Walk.png").convert_alpha()
        self.sprite_sheet_image_attack = pygame.image.load("Forest_Runner_Sprites/random_enemies/FireSpirit/Attack.png").convert_alpha()
        self.sprite_sheet_image_charge = pygame.image.load("Forest_Runner_Sprites/random_enemies/FireSpirit/Charge.png").convert_alpha()
        self.sprite_sheet_image_dead = pygame.image.load("Forest_Runner_Sprites/random_enemies/FireSpirit/Dead.png").convert_alpha()
        self.sprite_sheet_image_explosion = pygame.image.load("Forest_Runner_Sprites/random_enemies/FireSpirit/Explosion.png").convert_alpha()
        self.sprite_sheet_image_flame = pygame.image.load("Forest_Runner_Sprites/random_enemies/FireSpirit/Flame.png").convert_alpha()
        self.sprite_sheet_image_hurt = pygame.image.load("Forest_Runner_Sprites/random_enemies/FireSpirit/Hurt.png").convert_alpha()


        # Getting and setting image of character sprite in spritesheets
        self.sprite_sheet_idle = Spritesheet.SpriteSheet(self.spirte_sheet_image_idle)
        self.sprite_sheet_idle_2 = Spritesheet.SpriteSheet(self.sprite_sheet_image_idle_2)
        self.sprite_sheet_run = Spritesheet.SpriteSheet(self.sprite_sheet_image_run)
        self.sprite_sheet_shot = Spritesheet.SpriteSheet(self.sprite_sheet_image_shot)
        self.sprite_sheet_walk = Spritesheet.SpriteSheet(self.sprite_sheet_image_walk)
        self.sprite_sheet_attack = Spritesheet.SpriteSheet(self.sprite_sheet_image_attack)
        self.sprite_sheet_charge = Spritesheet.SpriteSheet(self.sprite_sheet_image_charge)
        self.sprite_sheet_dead = Spritesheet.SpriteSheet(self.sprite_sheet_image_dead)
        self.sprite_sheet_explosion = Spritesheet.SpriteSheet(self.sprite_sheet_image_explosion)
        self.sprite_sheet_flame = Spritesheet.SpriteSheet(self.sprite_sheet_image_flame)
        self.sprite_sheet_hurt = Spritesheet.SpriteSheet(self.sprite_sheet_image_hurt)


        # Sprite list that holds action spritesheets
        self.sprite_list = [
            self.sprite_sheet_idle, 
            self.sprite_sheet_idle_2, 
            self.sprite_sheet_run, 
            self.sprite_sheet_shot, 
            self.sprite_sheet_walk, 
            self.sprite_sheet_attack, 
            self.sprite_sheet_charge, 
            self.sprite_sheet_dead, 
            self.sprite_sheet_explosion, 
            self.sprite_sheet_flame,
            self.sprite_sheet_hurt
        ]

        self.animation_list = [] 
        self.animation_steps = [6, 6, 7, 8, 7, 14, 8, 5, 11, 13, 3] # Number of frames in each animation
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 150
        self.frame = 0
        self.BLACK = (0, 0, 0)
        self.action = 0
        self.c_x = -540
        self.c_y = -369
        self.screen_width = self.window.get_width()
        self.character_width = 150
        self.facing_right = True
        self.is_jumping = False
        self.jump_height = 10
        self.is_falling = False
        self.is_attacking = False
        self.is_shot = False
        self.is_dead = False
        self.is_hurt = False
        self.current_attack = 0
        self.max_frames = 0
        self.attack_timer = 0
        self.attack_duration = 20
        self.speed = 5
        self.is_charging = False



        # Populating animation list
        for i in range(len(self.animation_steps)):
            self.temp_list = []
            for j in range(self.animation_steps[i]):
                self.temp_list.append(self.sprite_list[i].get_image(j, 130, 127, 1.8, self.BLACK))

            self.animation_list.append(self.temp_list)


    

    #### WORK ON ENEMY BEHAVIOR ####


