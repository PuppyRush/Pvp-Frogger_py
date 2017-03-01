#import turtle
import sys
import pygame
import time
import game
import enum
import random
import socket
from random import Random
from enum import Enum
from pygame.locals import *

from game import Player, Heckler, Map, Controller, ServerGameApp as SGA
from game.multi import Message , Server, MessagePacker as Packer

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
pygame.init()
pygame.display.set_caption("FROGGER")
    

def beginServerGameApp(playeres=[],level=int,speed=int,serverSocket=Server):
    maxHeightCount = Map.Map.getMaxHeightCount(GameInfo.HEIGHT_COUNT.value,level)
    ctl = Controller.Controller(maxHeightCount)
    gameApp = SGA(ctl,playeres,level,speed,maxHeightCount)
    
    gameInfoMsg = Message.GameInfo(maxHeightCount)
    serverSocket.putMessage(gameInfoMsg,Packer.MessageKind.GAME)

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
        
        
        for player in gameApp.players:
            playerMsg = Message.Player(Message.MessageKind.PLAYER, player.position, player.jumpcount, player.nickname, player.frogNumber)
            serverSocket.putMessage(playerMsg,Packer.MessageKind.GAME)
        
        
        mapMsg = Message.Map(Message.MessageKind.MAP,gameApp.map.earth,ctl.getLowerScreenIdx(),ctl.getUpperScreenIdx(),GameInfo.HEIGHT_COUNT.value)
        hecklerMsg =  Message.Heckler(Message.MessageKind.HECKLER,gameApp.hecklers,ctl.getLowerScreenIdx(), ctl.getUpperScreenIdx(),GameInfo.HEIGHT_COUNT.value)

        
        serverSocket.putMessage(mapMsg,Packer.MessageKind.GAME)
        serverSocket.putMessage(hecklerMsg,Packer.MessageKind.GAME)
        

def beginClientGameApp(clientSocket=socket.socket):

    maxHeightCount=0
 
    while True:
        msg = clientSocket.getMessage(Packer.MessageKind.GAME)
        if msg.header == Message.MessageKind.GAMEINFO:
            maxHeightCount = msg.heightFullSize
            break
        else:
            clientSocket.getPacker().packingMessage(msg,Packer.MessageKind.GAME)
        
    while True:
        msg = clientSocket.getMessage(Packer.MessageKind.GAME)
        if msg.header == Message.MessageKind.MAP:
            for m in msg.map:
                SURFACE.blit()

        elif msg.header == Message.


        