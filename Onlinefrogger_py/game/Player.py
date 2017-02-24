import os
import pygame
import time
import sched

from game import GameApp as GA, Controller, Heckler, Map
from enum import Enum

class Order(Enum):
    UP=1
    DOWN=2
    LEFT=3
    RIGHT=4
    NONE=5

class Player(object):
    '''
    coord = (x,y) int

    '''

    def __init__(self,controller=Controller.Controller, frogNumber=int, nickname=str,coord=list,idx=list):
        
        self.ctl = controller
        self.frogNumber = frogNumber
        self.nickname = nickname
        self.idx = idx
        self.position = coord
        self.jumpcount=0
        
        self.boardingDirection = False
        self.isBoarding = False
        self.isMoving = False
        self.presentOrder = Order.UP
        
        self.playerSpeed = 0.3
        self.now = 0
        self.GAP=100


        file = os.path.join("images", "frog2.png")
        _image = pygame.image.load(file)
        _image.set_colorkey((228,0,127))
        _image.convert_alpha()
        self.image = _image
        

    def getPosition(self,x=int, y=int):
        return [self.position[0]+5,  self.ctl.gameInfo.SCREEN_HEIGHT_SIZE.value + self.ctl.gameInfo.HEIGHT_SIZE.value*self.ctl.getGapIdx() - self.position[1]+5]
        
    def updateKeyEvent(self,press=list):
        
        if(self.frogNumber>1):
            return 
            #from getting message
            #press = pygame.key.get_pressed()
            
        key = Order

        if self.isMoving:
            return

        if(press[pygame.K_w] == 1):
            key = self.__move(Order.UP)
        elif(press[pygame.K_s] == 1):
            key = self.__move(Order.DOWN)
        elif(press[pygame.K_a] == 1):
            key = self.__move(Order.LEFT)
        elif(press[pygame.K_d] == 1):
            key = self.__move(Order.RIGHT)

        if(self.ctl.getScreenState()==Controller.ScreenState.MIDDLE and key==Order.UP):
            self.setGapIdx(Order.UP)

        
    def __move(self,order=Order):
        
        if not self.__isValidMoving(order):
            return Order.NONE

        if not self.isMoving:    

            self.__setPosition(order)

            self.isMoving = True
            self.now = 0

            self.__rotate(self.presentOrder, order)
            self.presentOrder = order
            return order
        return Order.NONE


    def __setPosition(self,order=Order):
        if order == Order.LEFT:
            self.idx[0]-=1
        elif order == Order.RIGHT:
            self.idx[0]+=1
        elif order == Order.UP:
            self.ctl.setGapIdx(order)
            self.ctl.yIdx+=1
            self.idx[1]+=1
        elif order == Order.DOWN:
            self.ctl.yIdx-=1
            self.idx[1]-=1
        else:
            print("error")


    def __isValidMoving(self,order=Order):
        if order == Order.LEFT :
            if self.idx[0]==0:
                return False
                
        elif order == Order.RIGHT :
            if self.idx[0]==self.ctl.gameInfo.WIDTH_COUNT.value-1:
                return False
                
        elif order == Order.UP :
            if self.idx[1]- self.ctl.getGapIdx()  == self.ctl.gameInfo.HEIGHT_COUNT.value-1:
                return False
                    
        elif order == Order.DOWN :
            if self.idx[1]== 0:
                return False
    
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
       
        if self.isBoarding:
            if self.boardingDirection:
                self.position[0]+=  Heckler.Speed[Heckler.Kind.LOG.name].value/30
            else:
                self.position[0]-=  Heckler.Speed[Heckler.Kind.LOG.name].value/30

        if self.isMoving:
            if(self.presentOrder == Order.UP):
                self.position[1] += self.playerSpeed
            elif(self.presentOrder == Order.DOWN):
                self.position[1] -= self.playerSpeed
            elif(self.presentOrder == Order.LEFT):
                self.position[0] -= self.playerSpeed
            elif(self.presentOrder == Order.RIGHT):
                self.position[0] += self.playerSpeed

            self.now+=1
            if(self.now >= self.GAP):
                self.isMoving = False
                self.now = 0

    def isCollision(self, hecklers=[]):
             
        if(len(hecklers)!=0):
                        
            if(hecklers[0].kind != Heckler.Kind.LOG):
                self.isBoarding = False

                for heckler in hecklers:
                    pass
                    #h_pos = heckler.getPosition( self.idx[1])
                    #frog_width = GA.GameInfo.FROG_SIZE.value
                    #heckler_width = GA.GameInfo.WIDTH_SIZE.value

                    #if(h_pos[0] < self.position[0] ):
                    #    if h_pos[0]+heckler_width > self.position[0]:
                    #        print("l_col")
                    #elif h_pos[0] > self.position[0]:
                    #    if h_pos[0] < self.position[0]+frog_width:
                    #        print("r_col")
                                  
            else:
                logCollision = False
                for heckler in hecklers:

                    h_pos = heckler.getPosition()
                    frog_width = GA.GameInfo.FROG_SIZE.value
                    heckler_width = GA.GameInfo.WIDTH_SIZE.value

                    if(h_pos[0] < self.position[0] ):
                        if h_pos[0]+heckler_width > self.position[0]:
                            logCollision = True
                           
                    elif h_pos[0] > self.position[0]:
                        if h_pos[0] < self.position[0]+frog_width:
                            logCollision = True
    
                    if logCollision:
                        #self.position =  [heckler.getPosition()[0],self.getPosition(0, heckler.heightIdx)[1]]
                        self.isBoarding = True
                        self.boardingDirection = True if heckler.direction == True else False
                        break

                if not logCollision:
                    self.isBoarding = False
                    
                    
    def isFallinWater(self,map=Map):

        for m in map.rows: 
            if m == Map.MapEnum.RIVER:
                if not self.isBoarding:
                    pass
        