import turtle
import sys
import pygame
import math
import threading
import time
import game
import queue
from random import Random
from enum import Enum
from itertools import chain
from pygame.locals import *
from game import Player, Heckler, Map

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
DELTAT = CLOCK.tick(60)

SURFACE = pygame.display.set_mode((GameInfo.WIDTH_COUNT.value*GameInfo.WIDTH_SIZE.value, 
                                   GameInfo.HEIGHT_COUNT.value*GameInfo.HEIGHT_SIZE.value),DOUBLEBUF,32)
SURFACE.fill(BACKGROUND_COLOR)
#SURFACE.set_colorkey( (255,255,255,255) )


class GameApp(object):

    def __init__(self,players=[],level=int,speed=int):

        self.__GAP_OF_FROG = GameInfo.SCREEN_WIDTH_SIZE.value /(len(players)+1)
        self.__level = level
        self.__speed = speed
        self.MAX_HEIGHT_COUNT = GameInfo.HEIGHT_COUNT.value*self.__level*10
        self.__setPlayer(players)
        self.__setMap()
        self.__setHecklers()

    def __setPlayer(self,players=[]):

        self.players = []
        order =0
        for i in players:
            x = int((order+1)*GameInfo.WIDTH_COUNT.value/(len(players)+1))
            y = 0
            self.players.append( game.Player.Player(i[0], i[1], [ (order+1)*self.__GAP_OF_FROG - GameInfo.WIDTH_SIZE.value/2-3, GameInfo.HEIGHT_COUNT.value] , 
                                                    [ x,y ] ))
            order+=1
          
    def __setMap(self):
        
        self.map = Map.Map(self.MAX_HEIGHT_COUNT, GameInfo)

    def __setHecklers(self):
        
        self.hecklers = []    
        for i in self.map.earth:
            self.hecklers.append( Heckler.HecklerFactory( i.mapKind, GameInfo, i.heightIdx ,self.__speed).getHecklers())


def beginGameApp(playeres=[],level=int,speed=int):

    
    gameApp = GameApp(playeres,level,speed)

    pygame.init()
    pygame.display.set_caption("FROGGER")
    
    
    screenBeginIdx=0
    screenEndIdx=29

    startSection = True
    EndSection = False

    idxGap=0

    while True:

        for player in gameApp.players:
            key = player.updateKeyEvent(pygame.key.get_pressed())
            if(key == Player.Order.UP):
                if(startSection==False and EndSection==False):
                    idxGap+=1

            if(player.idx[1] == GameInfo.SCREEN_HEIGHT_SIZE.value/2):
                startSection = False
                EndSection = False
                     
        for i in range(screenBeginIdx ,screenEndIdx+1):

            for l in range(0,GameInfo.WIDTH_COUNT.value):
                if(gameApp.map.earth[i].mapKind == Map.MapEnum.ROCK):

                    if(gameApp.map.earth[i].rows[l] == Map.MapEnum.RIVER):
                        SURFACE.blit( gameApp.map.earth[i].waterImage, ( l*GameInfo.WIDTH_SIZE.value, GameInfo.SCREEN_HEIGHT_SIZE.value - i*GameInfo.HEIGHT_SIZE.value))
                    else:
                        SURFACE.blit( gameApp.map.earth[i].image, ( l*GameInfo.WIDTH_SIZE.value, GameInfo.SCREEN_HEIGHT_SIZE.value - i*GameInfo.HEIGHT_SIZE.value))
                else:
                    SURFACE.blit( gameApp.map.earth[i].image , ( l*GameInfo.WIDTH_SIZE.value, GameInfo.SCREEN_HEIGHT_SIZE.value - i*GameInfo.HEIGHT_SIZE.value))
            
            for l in gameApp.players:
                l.update()
                SURFACE.blit( l.image, (l.position[0], GameInfo.SCREEN_HEIGHT_SIZE.value -  l.position[1]))

            hecklers = gameApp.hecklers[i]
            for l in hecklers:
                SURFACE.blit( l.image, (l.position[0], GameInfo.SCREEN_HEIGHT_SIZE.value - l.position[1]) )
                l.update(DELTAT)

            #judgetment

                        
                

            #gameApp.players[0].decisionFrog(gameApp.hecklers[i],gameApp.map.earth[i])


        pygame.display.flip()
        pygame.display.update()

