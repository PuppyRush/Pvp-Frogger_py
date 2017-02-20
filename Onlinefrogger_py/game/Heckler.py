import os
import pygame
import game
import random
from enum import Enum
from game import Map,GameApp as GA, Controller
from pygame import sprite
from threading import Timer




class Speed(Enum):
    CAR = 2
    BUS = 1
    Snake = 1
    SPORTCAR = 5
    LOG = 3

class Kind(Enum):
    CAR = 1
    BUS = 2
    Snake = 3
    SPORTCAR = 4 
    LOG = 5   


PATH = {}
PATH[Kind.CAR] = "car.png"
PATH[Kind.BUS] = "bus.png"
PATH[Kind.Snake] = "Snake.png"
PATH[Kind.SPORTCAR] = "sportcar.png"
PATH[Kind.LOG] = "log.png"

class HecklerFactory(object):

    def __init__(self,controller=Controller.Controller,mapKind=Map.MapEnum,heightIdx=int,speed=int):
        self.ctl =controller
        self.mapKind = mapKind
        self.heightIdx = heightIdx
        self.speed = speed
        self.__makeHecklers()

    def __makeHecklers(self):

        self.__hecklers = []
        
        direction = random.randrange(0,2)

        if(self.mapKind == Map.MapEnum.RIVER):
            count = random.randrange(2,6)
            gap = self.ctl.gameInfo.SCREEN_WIDTH_SIZE.value/count
            for i in range(0,count):
                self.__hecklers.append( Heckler(self.ctl,Kind.LOG , [ i*gap , self.ctl.gameInfo.HEIGHT_SIZE.value * self.heightIdx] , direction, self.speed) )
               
        elif self.mapKind == Map.MapEnum.LOAD :
            count = random.randrange(4,7)
            gap = self.ctl.gameInfo.SCREEN_WIDTH_SIZE.value/count
            kind = self.__getSoilHecklerKindRandomly() 
            begin = random.randrange(0,50)
            for i in range(0,count):
                self.__hecklers.append( Heckler(self.ctl,kind ,  [ begin+i*gap ,self.ctl.gameInfo.HEIGHT_SIZE.value * self.heightIdx], direction, self.speed) )


    def __getSoilHecklerKindRandomly(self):
        pos = random.randrange(0,3)
        kind = Kind
        if(pos==0):
            kind = Kind.BUS
        elif(pos==1):
            kind =  Kind.CAR
        elif(pos==2):
            kind = Kind.SPORTCAR
        else:
            kind = Kind.CAR
        return kind

    def getHecklers(self):
        return self.__hecklers


class Heckler(pygame.sprite.Sprite):
    def __init__(self,controller=Controller.Controller, name=Kind,position=[],direction=True,speed=int):
        self.ctl = controller
        self.speed = Speed[name.name].value+speed
        self.position = position
        self.direction = direction
        self.image = self.__loadImage(PATH[name],-1)
                

    def __loadImage(self,file_name=str, image_directory='images'):
        
        file = os.path.join(image_directory, file_name)
        _image = pygame.image.load(file)
        #_image.set_colorkey((228,0,127))
        #_image.convert_alpha()

        if not self.direction:
            _image = pygame.transform.flip(_image,True,False)

        return _image

        
    def getPosition(self,y=int):
        return (self.position[0] , self.ctl.gameInfo.SCREEN_HEIGHT_SIZE.value - self.position[1] + self.ctl.getGapIdx()*self.ctl.gameInfo.HEIGHT_SIZE.value )


    def update(self,deltat):
        if(self.direction):
            if self.position[0]-30 >= self.ctl.gameInfo.WIDTH_COUNT.value*self.ctl.gameInfo.WIDTH_SIZE.value:
                self.position[0] = 0
            self.position[0]+=self.speed
        else:
            if(self.position[0]+30<=0):
                self.position[0] = self.ctl.gameInfo.WIDTH_COUNT.value * self.ctl.gameInfo.WIDTH_SIZE.value
            self.position[0]-=self.speed

        

        self.rect = self.image.get_rect()
        self.rect.center = self.position