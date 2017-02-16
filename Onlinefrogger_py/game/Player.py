import os
import pygame
import time
import sched

from game import GameApp as GA
from enum import Enum

class Order(Enum):
    UP=1
    DOWN=2
    LEFT=3
    RIGHT=4


class Player(object):
    '''
    coord = (x,y) int

    '''
    def __init__(self, frogNumber=int, nickname=str,coord=list,idx=list):
        self.nickname = nickname
        self.idx = idx
        self.position = coord
        self.jumpcount=0
        self.isMoving = False
        self.presentOrder = Order.UP
        self.gap = 30
        self.now = 0

        file = os.path.join("images", "frog.png")
        _image = pygame.image.load(file)
        _image.set_colorkey((228,0,127))
        _image.convert_alpha()
        self.image = _image
        
        
    def move(self,order=Order):
        
        if not self.isValidMoving(order):
            return
        
        if not self.isMoving:    
            self.isMoving = True
            self.now = 0

            self.__rotate(self.presentOrder, order)
            self.presentOrder = order
            
    def isValidMoving(self,order=Order):
        if order ==Order.LEFT :
            if self.idx[0]==0:
                return False
            else:
                self.idx[0]-=1
        elif order ==Order.RIGHT :
            if self.idx[0]==GA.GameInfo.WIDTH_COUNT.value-1:
                return False
            else:
                self.idx[0]+=1
        elif order ==Order.UP :
            if self.idx[1]==0:
                return False
            else:
                self.idx[1]-=1
        elif order ==Order.DOWN :
            if self.idx[1]==GA.GameInfo.HEIGHT_COUNT.value-1:
                return False
            else:
                self.idx[1]+=1

        return True

    def __rotate(self,prev=Order,next=Order):

        if(prev==Order.UP):
            if(next == Order.LEFT):
                self.image = pygame.transform.rotate(self.image, 90)
            elif(next == Order.RIGHT):
                self.image = pygame.transform.rotate(self.image, 270)
            elif(next == Order.DOWN):
                self.image = pygame.transform.rotate(self.image, 180)
        elif(prev==Order.DOWN):
            if(next == Order.UP):
                self.image = pygame.transform.rotate(self.image, 180)
            elif(next == Order.LEFT):
                self.image = pygame.transform.rotate(self.image, 270)
            elif(next == Order.RIGHT):
                self.image = pygame.transform.rotate(self.image, 90)
        elif(prev==Order.RIGHT):
            if(next == Order.UP):
                self.image = pygame.transform.rotate(self.image, 90)
            elif(next == Order.LEFT):
                self.image = pygame.transform.rotate(self.image, 180)
            elif(next == Order.DOWN):
                self.image = pygame.transform.rotate(self.image, 270)
        elif prev==Order.LEFT :
            if next == Order.UP :
                self.image = pygame.transform.rotate(self.image, 270)
            elif(next == Order.RIGHT):
                self.image = pygame.transform.rotate(self.image, 180)
            elif(next == Order.DOWN):
                self.image = pygame.transform.rotate(self.image, 90)        

    def update(self):
        
        if self.isMoving:
            if(self.presentOrder == Order.UP):
                self.position[1] +=1
            elif(self.presentOrder == Order.DOWN):
                self.position[1] -=1
            elif(self.presentOrder == Order.LEFT):
                self.position[0] -=1
            elif(self.presentOrder == Order.RIGHT):
                self.position[0] +=1

            self.now+=1

            if(self.now == self.gap):
                self.isMoving = False
                self.now = 0