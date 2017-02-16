
import threading
import queue
import game.multi.Client

HEADER, BODY = 0,1
GUI , NETWORK, GAME = 0,1,2

class Message(object):
    def __init__(self):
        self.header = 0
        self.body = object



class MessagePacker(threading.Thread):
    def init(self):
        self.messageQ = queue.Queue()


    def packingGuiMessage(self,data):
        msg = Message()
        msg.header = GUI
        msg.body = data
        self.messageQ.put(msg)

    def packingGameMessage(self,data):
        msg = Message()
        msg.header = GAME
        msg.body = data
        self.messageQ.put(msg)

    def packingNetworkMessage(self,data):
        msg = Message()
        msg.header = NETWORK
        msg.body = data
        self.messageQ.put(msg)

    def run(self):
        while(True):
            if(self.messageQ.qsize()==0):
                continue
            else:
                game.multi.Client.client.load(self.messageQ.get())


messagePacker = MessagePacker()

def beginMessagePacker():
    messagePacker.init()
    messagePacker.start()