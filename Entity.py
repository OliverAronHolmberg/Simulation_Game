import pygame
import random

class Entity:
    def __init__(self, screen, game, type, state, x, y, moving, entity_image):
        self.screen = screen
        self.game = game
        self.type = type
        self.state = state
        self.x = x
        self.y = y
        self.entity_image = entity_image
        

        self.stats = {
            "Alive" : True,
            "Health" : 100,
            "Hungry" : random.choice([True, False]),
            "Runspeed" : random.randint(20, 25)/10,
            "Walkspeed" : random.randint(5, 10)/10,
            "Type" : self.type
        }
        

        


        
        self.rect = self.entity_image.get_rect()


        self.original_width, self.original_height = self.entity_image.get_size()
        
        self.new_width = self.original_width
        self.new_height = self.original_height


        self.boundry_x = self.game.screen_width*2
        self.boundry_y = self.game.screen_height*2

        self.timer = 0

        #Movement
        self.current_direction = [random.choice([-1, 1]), random.choice([-1, 1])]
        self.move_speed = self.stats["Walkspeed"]
        self.move_duration = random.randint(100, 300)
        self.moving = moving
        self.running = False

        #Animals
        self.flee = False


    def move(self):
        
        new_x = self.x + self.current_direction[0] * self.move_speed 
        new_y = self.y  + self.current_direction[1] * self.move_speed 
        
        self.x = max(0, min(self.game.world_width - self.new_width, new_x))
        self.y = max(0, min(self.game.world_height - self.new_height, new_y))

        if self.x == self.game.world_width-self.new_width or self.x == 0 or self.y == self.game.world_height-self.new_height or self.y == 0:
            if random.randint(0,1) == 1:
                self.current_direction = [random.choice([-1, 1]), random.choice([-1, 1])]
        

    def initmove(self):
        self.move_speed = 1 / self.game.zoom_level
        self.timer += 1
        
        

        
        if self.timer >= self.move_duration:
            self.current_direction = [random.choice([-1, 1]), random.choice([-1, 1])]
            self.moving = random.choice([False, True])
            self.move_duration = random.randint(100, 300)
            self.timer = 0

        
        if self.flee == False:
            self.move_speed = self.stats["Walkspeed"]
            if self.moving:
                self.move()
        else:
            self.move_speed = self.stats["Runspeed"]
            self.move()
                
            
            
        


    def Main_Entity(self):
        self.initmove()
        
        self.new_height = int(self.original_height * (1+ self.game.zoom_level))
        self.new_width = int(self.original_width * (1+ self.game.zoom_level ))

        


        screen_x = (self.x-self.game.camera_x) * self.game.zoom_level
        screen_y = (self.y-self.game.camera_y) * self.game.zoom_level


        scaled_image = pygame.transform.scale(self.entity_image, (self.new_width, self.new_height))
        self.screen.blit(scaled_image, (screen_x, screen_y))
        pygame.draw.rect(self.entity_image, (255,0,0), self.rect, 2)
        
        
        