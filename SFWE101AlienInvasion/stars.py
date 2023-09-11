import pygame
import random

from pygame.sprite import Sprite

class Stars(Sprite):
    # background elements

    def __init__(self, ai_game):
        #Create a star object at a position
        #Inherit properly from Sprite by calling super method
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = (255, 255, 255)

        # Create a star rect at (random value, 0).
        self.rect = pygame.Rect(random.randrange(0, self.settings.screen_width - self.settings.star_size, 10), self.settings.screen_height, self.settings.star_size, self.settings.star_size)

        # Store the star's position as a decimal value.
        self.y = float(self.rect.y)
    
    def update(self):
        #Move the star up the screen
        #Update the decimal point of the star.
        self.y -= self.settings.star_speed
        
        #Update the rect position
        self.rect.y = self.y

    def draw_star(self):
        #Draw the star to the screen
        pygame.draw.rect(self.screen, self.color, self.rect)