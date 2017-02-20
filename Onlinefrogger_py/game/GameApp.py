#import turtle
import sys
import pygame
import math
import threading
import time
import game
import queue
import enum
import random
from random import Random
from enum import Enum
from itertools import chain
from pygame.locals import *
from game import Player, Heckler, Map, Controller

if not pygame.font: print("Warning, fonts disabled")
if not pygame.mixer: print("Warning, sound disabled")



class GameInfo(Enum):
    WIDTH_COUNT= 20
    HEIGHT_COUNT = 30
    WIDTH_SIZE = 30
    HEIGHT_SIZE = 30
    SCREEN_HEIGHT_SIZE = HEIGHT_COUNT * HEIGHT_SIZE
    SCREEN_WIDTH_SIZE = WIDTH_COUNT * WIDTH_SIZE



BACKGROUND_COLOR = (255,255,255)

CLOCK = pygame.time.Clock()
DELTAT = CLOCK.tick(30)

SURFACE = pygame.display.set_mode((GameInfo.WIDTH_COUNT.value*GameInfo.WIDTH_SIZE.value, 
                                   GameInfo.HEIGHT_COUNT.value*GameInfo.HEIGHT_SIZE.value),DOUBLEBUF,32)
SURFACE.fill(BACKGROUND_COLOR)
#SURFACE.set_colorkey( (255,255,255,255) )


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
        for i in players:
            x = int((order+1)*GameInfo.WIDTH_COUNT.value/(len(players)+1))
            y = 0
            self.players.append( game.Player.Player(self.ctl,i[0], i[1], 
                                                    [ (order+1)*self.__GAP_OF_FROG, GameInfo.HEIGHT_COUNT.value], 
                                                    [ x,y ]) )
            order+=1
          
    def __setMap(self):
        
        self.map = Map.Map(self.ctl,self.MAX_HEIGHT_COUNT)

    def __setHecklers(self):
        
        self.hecklers = []    
        for i in self.map.earth:
            self.hecklers.append( Heckler.HecklerFactory(self.ctl, i.mapKind, i.heightIdx ,self.__speed).getHecklers())


def beginGameApp(playeres=[],level=int,speed=int):
    
    
    pygame.init()
    pygame.display.set_caption("FROGGER")
    

    maxHeightCount = Map.Map.getMaxHeightCount(GameInfo.HEIGHT_COUNT.value,level)

    ctl = Controller.Controller(maxHeightCount)
    gameApp = GameApp(ctl,playeres,level,speed,maxHeightCount)
    
    
    while True:

        #preventing to full of queue
        pygame.event.get()

        for player in gameApp.players:
            player.updateKeyEvent(pygame.key.get_pressed())

        for i in range(ctl.getLowerScreenIdx(), ctl.getUpperScreenIdx()):

            for l in range(0,GameInfo.WIDTH_COUNT.value):
                if(gameApp.map.earth[i].mapKind == Map.MapEnum.ROCK):

                    if(gameApp.map.earth[i].rows[l] == Map.MapEnum.RIVER):
                        SURFACE.blit( gameApp.map.earth[i].waterImage, gameApp.map.getPosition(l,i) )
                    else:
                        SURFACE.blit( gameApp.map.earth[i].image, gameApp.map.getPosition(l,i))
                else:
                    SURFACE.blit( gameApp.map.earth[i].image , gameApp.map.getPosition(l,i))
            
            for l in gameApp.players:
                l.update()
                SURFACE.blit( l.image, l.getPosition(l,i))

            hecklers = gameApp.hecklers[i]
            for l in hecklers:
                SURFACE.blit( l.image, l.getPosition(i))
                l.update(DELTAT)

        pygame.display.flip()
        pygame.display.update()

