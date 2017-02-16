import os
import pygame
from game import GameApp
from enum import Enum
import random




class MapEnum(Enum):
    RIVER=1
    SOIL=2
    CONCRETE=3
    ROCK=4

PATH = {}
PATH[MapEnum.CONCRETE] = "concrete.png"
PATH[MapEnum.RIVER] = "river.png"
PATH[MapEnum.ROCK] = "rock.png"
PATH[MapEnum.SOIL] = "soil.png"



class Map(object):
    

    class MapRow(object):
                

        def __init__(self,kind=MapEnum,widthCount=int,heightIdx=int):
            self.heightIdx = heightIdx
            self.rows = []
            self.mapKind = kind
            self.image = self.__loadImage(PATH.get(kind) ,-1)

            if(kind == MapEnum.ROCK):
                self.waterImage = self.__loadImage(PATH.get(MapEnum.RIVER),-1)
                
                rockCount = random.randrange(2,6)
                rockIdx = {}

                while len(rockIdx)< rockCount:
                    idx = random.randrange(0,widthCount)
                    rockIdx[idx] = idx

                for l in range(0,widthCount):
                    if(l in rockIdx):
                        self.rows.append(MapEnum.ROCK)
                    else:
                        self.rows.append(MapEnum.RIVER)
            else:
                for l in range(0,widthCount):
                        self.rows.append(kind)

        
        def __loadImage(self,file_name=str, colorkey=False, image_directory='images'):
        
            file = os.path.join(image_directory, file_name)
            _image = pygame.image.load(file)
            if colorkey:
                if colorkey == -1: 
                    # If the color key is -1, set it to color of upper left corner
                    colorkey = _image.get_at((0, 0))
                    _image.set_colorkey(colorkey)
                    _image = _image.convert()
                    _image.fill((255, 255, 255, 128), None, pygame.BLEND_RGBA_MULT)
            else: # If there is no colorkey, preserve the image's alpha per pixel.
                _image = _image.convert_alpha()
            return _image


    def __init__(self,MAX_HEIGHT_COUNT=int, gameInfo=object):
        self.earth = []
        self.__MAX_HEIGHT_COUNT = MAX_HEIGHT_COUNT
        self.__WIDTH_COUNT = gameInfo.WIDTH_COUNT.value
        self.__HEIGHT_COUNT = gameInfo.HEIGHT_COUNT.value

        for i in range(0,5):
            self.earth.append( self.MapRow( MapEnum.CONCRETE,gameInfo.WIDTH_COUNT.value,i))
        

        beginIdx = 5
        isSoil = True
        endIdx=0
        earthKind=0
        while beginIdx < self.__MAX_HEIGHT_COUNT-1:           
            
            endIdx = beginIdx + random.randrange(3,7)
            if(endIdx >= self.__MAX_HEIGHT_COUNT):
                endIdx = self.__MAX_HEIGHT_COUNT-1              
            
            if(isSoil):
                for i in range(beginIdx,endIdx):
                    self.earth.append( self.MapRow( MapEnum.SOIL, gameInfo.WIDTH_COUNT.value,i ))
            else:
                for i in range(beginIdx,endIdx):
                    kind = MapEnum.ROCK if random.randrange(0,5)==0 else MapEnum.RIVER
                    self.earth.append( self.MapRow( kind,gameInfo.WIDTH_COUNT.value,i))


            isSoil =not isSoil
            beginIdx = endIdx


