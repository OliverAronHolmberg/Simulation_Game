import pygame
import os
import sys
import random
from Entity import Entity
from UI import UI

class Game:
    def __init__(self):
        pygame.init()
        info = pygame.display.Info()
        self.screen_width = info.current_w
        self.screen_height = info.current_h
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.keydown = False

        self.clock = pygame.time.Clock()
        self.fps = 60


        #Entities
        self.entities = []
        
        for entity in range(random.randint(5,15)):
            cow = Entity(self.screen, self, "Cow", "Friendly", random.randint(0, self.screen_width),random.randint(0, self.screen_height), random.choice([True, False]), pygame.image.load("Images\Entities\Cow.png").convert_alpha())
            self.entities.append(cow)
        for entity in range(random.randint(1,5)):
            Wolf = Entity(self.screen, self, "Enemy", "Unfriendly", random.randint(0, self.screen_width),random.randint(0, self.screen_height), random.choice([True, False]), pygame.image.load("Images\Entities\Wolf.png").convert_alpha())
            self.entities.append(Wolf)

        #UI
        self.UI = []
        self.statsmenu = UI(self,self.screen,self.screen_width-500,100, pygame.image.load("Images\\UI\\Stats.png").convert_alpha())
        self.UI.append(self.statsmenu)
        

        #Player
        self.world_width, self.world_height = self.screen_width*2, self.screen_height*2
        self.clicked = True
        self.zoom_level = 1
        self.camera_x = 0
        self.camera_y = 0
        
    def exit_game(self):
        pygame.quit()
        sys.exit() 


    #Player

    def Main_Player(self):
        keys = pygame.key.get_pressed()
        events = pygame.event.get()
        

        for event in events:
                if event.type == pygame.QUIT:
                    self.exit_game()


                
                        
                
                    
                if event.type == pygame.MOUSEWHEEL:
                    
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    
                    world_mouse_x = self.camera_x + mouse_x / self.zoom_level
                    world_mouse_y = self.camera_y + mouse_y / self.zoom_level

                    prev_zoom = self.zoom_level
                    self.zoom_level += event.y*0.1
                    self.zoom_level = max(0.5, min(self.zoom_level, 5))
                    zoom_factor = self.zoom_level/prev_zoom

                    self.camera_x = world_mouse_x - (mouse_x/self.zoom_level)
                    self.camera_y = world_mouse_y - (mouse_y/self.zoom_level)

                self.camera_x = max(0, min(self.world_width-self.screen_width/self.zoom_level, self.camera_x))
                self.camera_y = max(0, min(self.world_height-self.screen_height/self.zoom_level, self.camera_y))

                

                
                button = pygame.mouse.get_pressed()
                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button[0]:
                        
                        for entity in self.entities:
                            screen_rect = pygame.Rect(
                                (entity.x-self.camera_x) * self.zoom_level,          
                                (entity.y-self.camera_y) * self.zoom_level,
                                entity.new_width,
                                entity.new_height
                            )
                            
                            if screen_rect.collidepoint(mouse_pos):
                                if self.clicked == True:
                                    self.clicked = False
                                else:
                                    self.clicked = True
                                break
                            else:
                                self.clicked = False
                            
                        if self.clicked == True:
                            self.UI[0].open = True
                        else:
                            self.UI[0].open = False
                    
                

                


        if keys[pygame.K_ESCAPE] == True:
            self.exit_game()
        
            
                
                


        


    def Main_loop(self):
        while True:
            self.clock.tick(self.fps)
            self.screen.fill((150,220,150))


            for entity in self.entities:
                entity.Main_Entity()

            self.Main_Player()

            
            for ui in self.UI:
                if ui.open == True:
                    self.screen.blit(ui.image, (ui.x, ui.y))
            

            pygame.display.flip()
                





Game().Main_loop()