import os, sys
import pygame

class ClietGameApp(object):
    def __init__(self):
        pass

    def __loadImage(self,file_name=str,image_directory='images'):
        
        file = os.path.join(image_directory, file_name)
        _image = pygame.image.load(file)
        _image.set_colorkey((228,0,127))
        _image.convert_alpha()
        return _image
