import threading
import queue
import game
from game.multi import MessagePacker,Message

class MessageParser(object):
    
    def __init__(self):
        self.__guiQ = queue.Queue()
        self.__networkQ = queue.Queue()
        self.__gameQ = queue.Queue()
        
    def loader(self,data=object):
        msg = MessagePacker.Message()
        msg.header = data.header
        msg.body = data.body    

        if msg.header ==MessagePacker.MessageKind.GAME:
            self.__gameQ.put(msg.body)

        elif msg.header ==MessagePacker.MessageKind.GUI:
            self.__guiQ.put(msg.body)

        elif msg.header ==MessagePacker.MessageKind.NETWORK:
            self.__networkQ.put(msg.body)
            
    def empty(self,kind=object):
        if kind==MessagePacker.MessageKind.GAME:
            return self.__gameQ.empty()
        elif kind==MessagePacker.MessageKind.GUI:
            return self.__guiQ.empty()
        elif kind==MessagePacker.MessageKind.NETWORK:
            return self.__networkQ.empty()
        else:
            return False

    def getGuiMessage(self):
        if self.__guiQ.empty():
            return False
        else:
            return self.__guiQ.get()
        
    def getGameMessage(self):
        if self.__gameQ.empty() :
            return False
        else:
            return self.__gameQ.get_nowait()

    def getNetworkMessage(self):
        if self.__networkQ.empty():
            return False
        else:
            return self.__networkQ.get_nowait()

