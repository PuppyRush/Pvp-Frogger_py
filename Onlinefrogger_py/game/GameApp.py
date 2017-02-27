#import turtle
import sys
import pygame
import time
import game
import enum
import random
from random import Random
from enum import Enum
from pygame.locals import *

from game import Player, Heckler, Map, Controller
from game.multi import Message , Server, MessagePacker

if not pygame.font: print("Warning, fonts disabled")
if not pygame.mixer: print("Warning, sound disabled")



class GameInfo(Enum):
    WIDTH_COUNT= 20
    HEIGHT_COUNT = 30
    WIDTH_SIZE = 30
    HEIGHT_SIZE = 30
    FROG_SIZE = 15
    SCREEN_HEIGHT_SIZE = HEIGHT_COUNT * HEIGHT_SIZE
    SCREEN_WIDTH_SIZE = WIDTH_COUNT * WIDTH_SIZE

BACKGROUND_COLOR = (255,255,255)

CLOCK = pygame.time.Clock()
TICK = 30
DELTAT = CLOCK.tick(TICK)

SURFACE = pygame.display.set_mode((GameInfo.WIDTH_COUNT.value*GameInfo.WIDTH_SIZE.value, 
                                   GameInfo.HEIGHT_COUNT.value*GameInfo.HEIGHT_SIZE.value),DOUBLEBUF,32)
SURFACE.fill(BACKGROUND_COLOR)
#SURFACE.set_colorkey(BACKGROUND_COLOR )



class GameApp(object):

    def __init__(self,ctl=Controller.Controller, players=[],level=int,speed=int,maxHeightCount=int):
        self.ctl = ctl
        self.__GAP_OF_FROG = GameInfo.WIDTH_COUNT.value * GameInfo.WIDTH_SIZE.value /(len(players)+1)
        self.__level = level
        self.__speed = speed
        self.MAX_HEIGHT_COUNT = maxHeightCount
        self.__setPlayer(players)
        self.__setMap()
        self.__setHecklers()

    def __setPlayer(self,players=[]):

        self.players = []
        order =0
        for player in players:
            x = int((order+1)*GameInfo.WIDTH_COUNT.value/(len(players)+1))
            y = 0
            self.players.append( game.Player.Player(self.ctl,player[0], player[1], 
                                                    [ (order+1)*self.__GAP_OF_FROG, GameInfo.HEIGHT_COUNT.value], 
                                                    [ x,y ]) )
            order+=1
          
    def __setMap(self):
        
        self.map = Map.Map(self.ctl,self.MAX_HEIGHT_COUNT)

    def __setHecklers(self):
        
        self.hecklers = []    
        for i in self.map.earth:
            self.hecklers.append( Heckler.HecklerFactory(self.ctl, i.mapKind, i.heightIdx ,self.__speed).getHecklers())
       


def beginServerGameApp(playeres=[],level=int,speed=int,serverSocket=Server):
    
    
    pygame.init()
    pygame.display.set_caption("FROGGER")
    

    maxHeightCount = Map.Map.getMaxHeightCount(GameInfo.HEIGHT_COUNT.value,level)

    ctl = Controller.Controller(maxHeightCount)
    gameApp = GameApp(ctl,playeres,level,speed,maxHeightCount)
    
    
    while True:

        SURFACE.fill(BACKGROUND_COLOR)

        #preventing to full of queue
        pygame.event.get()

        for player in gameApp.players:
            player.updateKeyEvent(pygame.key.get_pressed())

        for i in range(ctl.getLowerScreenIdx(), ctl.getUpperScreenIdx()-1):

            for l in range(0,GameInfo.WIDTH_COUNT.value):
                if(gameApp.map.earth[i].mapKind == Map.MapEnum.ROCK):

                    if(gameApp.map.earth[i].rows[l] == Map.MapEnum.RIVER):
                        SURFACE.blit( gameApp.map.earth[i].waterImage, gameApp.map.getPosition(l,i) )
                    else:
                        SURFACE.blit( gameApp.map.earth[i].waterImage, gameApp.map.getPosition(l,i) )
                        SURFACE.blit( gameApp.map.earth[i].image, gameApp.map.getPosition(l,i))
                else:    
                    SURFACE.blit( gameApp.map.earth[i].image , gameApp.map.getPosition(l,i))
            

          
            hecklers = gameApp.hecklers[i]
            for l in hecklers:
                SURFACE.blit( l.image, l.getPosition())
                l.update(DELTAT)

            for l in gameApp.players:
                
                l.isCollision(gameApp.hecklers[l.idx[1]])    
                l.isFallinWater(gameApp.map.earth[l.idx[1]] )

            for l in gameApp.players:
                l.update()
                SURFACE.blit( l.image, l.getPosition(l,i))
        
        pygame.display.update()

        my = gameApp.players[0]
        myFrog = Message.Player(Message.MessageKind.PLAYER, my.position, my.jumpcount, my.nickname, my.frogNumber)
        gameInfoMsg = Message.GameInfo(Message.MessageKind.GAMEINFO,maxHeightCount,TICK)
        mapMsg = Message.Map(Message.MessageKind.MAP,gameApp.map.earth,ctl.getLowerScreenIdx(),ctl.getUpperScreenIdx(),GameInfo.HEIGHT_COUNT.value)
        hecklerMsg =  Message.Heckler(Message.MessageKind.HECKLER,gameApp.hecklers,ctl.getLowerScreenIdx(), ctl.getUpperScreenIdx(),GameInfo.HEIGHT_COUNT.value)

        serverSocket.putMessage(myFrog, MessagePacker.MessageKind.GAME)

def beginClientGameApp():

    pass