
import threading
import queue
import game.multi.Client
import enum

HEADER, BODY = 0,1

class MessageKind(enum.Enum):
    GUI = 0
    NETWORK = 1
    GAME = 2

class Message(object):
    def __init__(self):
        self.header = 0
        self.body = object



class MessagePacker(object):
    def __init__(self):
        self.__messageQ = queue.Queue()


    def packingMessage(self,data=object,dataKind=MessageKind):

        if self.__messageQ.full():
            return False

        msg = Message()
        msg.header = dataKind
        msg.body = data
        self.__messageQ.put(msg)

    def getMessage(self):
        if self.__messageQ.empty():
            return False
        else:
            return self.__messageQ.get()
