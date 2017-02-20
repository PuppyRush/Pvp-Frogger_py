import game
import enum
from game import Player,Map,GameApp as GA
from enum import Enum

class ScreenState(Enum):
    BEGIN=1
    MIDDLE=2
    FINAL=3

class Controller(object):

    def __init__(self,MAX_HEIGHT_COUNT=int):

        self.MAX_HEIGHT_COUNT = MAX_HEIGHT_COUNT
        self.__gapIdx = 0
        self.gameInfo = GA.GameInfo
        
        self.__screenBeginIdx=0
        self.__screenEndIdx=31
        self.yIdx=0
        self.screenState=ScreenState.BEGIN

    def getScreenState(self):

        state = ScreenState

        if(self.screenState == ScreenState.BEGIN):
            if(self.yIdx >= self.gameInfo.HEIGHT_COUNT.value/2):
                self.screenState = ScreenState.MIDDLE
        elif self.screenState == ScreenState.MIDDLE:
            if self.yIdx >= self.MAX_HEIGHT_COUNT-self.gameInfo.HEIGHT_COUNT.value/2:
                self.screenState = ScreenState.FINAL

        return state
    
    def getUpperScreenIdx(self):
        return self.__screenEndIdx + self.__gapIdx

    def getLowerScreenIdx(self):
        return self.__screenBeginIdx + self.__gapIdx

    def setScreenIdx(self, upper=int, lower=int):
        self.__screenBeginIdx = lower
        self.__screenEndIdx = upper

    def setGapIdx(self,order):
        
        if self.screenState == ScreenState.MIDDLE:
            if(order == Player.Order.UP):
                self.__gapIdx+=1

    def getGapIdx(self):
        return self.__gapIdx
    