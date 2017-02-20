import os
import pygame
import game
from game import GameApp as GA, Controller
from enum import Enum
import random




class MapEnum(Enum):
    RIVER=1
    LOAD=2
    CONCRETE=3
    ROCK=4

PATH = {}
PATH[MapEnum.CONCRETE] = "concrete.png"
PATH[MapEnum.RIVER] = "river.png"
PATH[MapEnum.ROCK] = "rock.png"
PATH[MapEnum.LOAD] = "load.png"




class Map(object):
    

    class MapRow(object):
                

        def __init__(self,kind=MapEnum,widthCount=int,heightIdx=int):
            self.heightIdx = heightIdx
            self.rows = []
            self.mapKind = kind
            self.image = self.__loadImage(PATH.get(kind))

            if(kind == MapEnum.ROCK):
                self.waterImage = self.__loadImage(PATH.get(MapEnum.RIVER))
                
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

        
        def __loadImage(self,file_name=str,image_directory='images'):
        
            file = os.path.join(image_directory, file_name)
            _image = pygame.image.load(file)
            #_image.set_colorkey((228,0,127))
            #_image.convert_alpha()
            return _image


    def __init__(self,ctl=object,MAX_HEIGHT_COUNT=int):
        self.ctl = ctl
        
        self.earth = []
        self.__MAX_HEIGHT_COUNT = MAX_HEIGHT_COUNT
        self.__WIDTH_COUNT = ctl.gameInfo.WIDTH_COUNT.value
        self.__HEIGHT_COUNT = ctl.gameInfo.HEIGHT_COUNT.value

        for i in range(0,5):
            self.earth.append( self.MapRow( MapEnum.CONCRETE,ctl.gameInfo.WIDTH_COUNT.value,i))
        
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
                    self.earth.append( self.MapRow( MapEnum.LOAD, ctl.gameInfo.WIDTH_COUNT.value,i ))
            else:
                for i in range(beginIdx,endIdx):
                    kind = MapEnum.ROCK if random.randrange(0,5)==0 else MapEnum.RIVER
                    self.earth.append( self.MapRow( kind,ctl.gameInfo.WIDTH_COUNT.value,i))


            isSoil =not isSoil
            beginIdx = endIdx

    def getPosition(self,x=int,y=int):
        return (x*self.ctl.gameInfo.WIDTH_SIZE.value, 
                self.ctl.gameInfo.SCREEN_HEIGHT_SIZE.value+ self.ctl.gameInfo.HEIGHT_SIZE.value*(self.ctl.getGapIdx() - y))

    @staticmethod
    def getMaxHeightCount(SCREEN_HEIGHT_COUNT=int,leven=int):
        return SCREEN_HEIGHT_COUNT*leven*10
