#pygame exercise
import sys

import pygame

class BlueBackground:
    """class to note the blue properties"""
    
    def __init__(self):
        """initialize the blue background properties."""
        pygame.init()
        
        #intializing the screen
        self.screen = pygame.display.set_mode((1200,800))
        
        #setting the caption
        pygame.display.set_caption("Blue Background")
        
        #initializing the background color
        self.bg_color = (0,0,255)
                    
        #Applying the color initialized to the screen
        self.screen.fill(self.bg_color)
                                
        #Make the most recently drawn screen visible
        pygame.display.flip()
            
            
if __name__=="__main__":
            #Make a game instance and run the game
            bb = BlueBackground()      