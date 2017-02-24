import threading
import queue
import enum

HEADER, BODY = 0,1

class MessageKind(enum.Enum):
    GUI = 0
    NETWORK = 1
    GAME = 2

class GameKind(enum.Enum):
    SEND_MAP=1
    SEND_PLAYERS=2
    SEND_HECKLERS=3

class Message(object):
    def __init__(self):
        self.header = 0
        self.body = object

class MessageParser(object):
    
    def __init__(self):
        self.__messageQ = queue.Queue
        self.__guiQ = queue.Queue
        self.__networkQ = queue.Queue
        self.__gameQ = queue.Queue
        
    def loader(self,data):
        msg = Message()
        msg.header = data.header
        msg.body = data.body    

        self.__messageQ.put(msg)

            
    def getGuiMessage(self):
        if self.__guiQ.empty():
            return False
        else:
            return self.__guiQ.get()
        
    def getGameMessage(self):
        if self.__gameQ.empty():
            return False
        else:
            return self.__gameQ.get()

    def getNetworkMessage(self):
        if self.__networkQ.empty():
            return False
        else:
            return self.__networkQ.get()

