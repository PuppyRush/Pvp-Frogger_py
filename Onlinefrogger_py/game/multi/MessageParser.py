import threading
import queue

HEADER, BODY = 0,1
GUI , NETWORK, GAME = 0,1,2

class Message(object):
    def __init__(self):
        self.header = 0
        self.body = object



class MessageParser(threading.Thread):
    
    def init(self):
        self.messageQ = queue.Queue
        self.guiQ = queue.Queue
        self.networkQ = queue.Queue
        self.gameQ = queue.Queue
        

    def run(self):
        while(True):
            self.commandParser()

    
    def load(self,data):
        msg = Message()
        msg.header = data.header
        msg.body = data.body    

        self.message.put(msg)
            
    def commandParser(self):
        if(self.messageQ.qsize==0):
            return
        else:
            data = self.messageQ.get()
        
            if(data.header ==GAME):
                self.gameQ.put(data.body)
            elif(data.header == GUI):
                self.guiQ.put(data.body)
            elif(data.header == NETWORK):
                self.networkQ.put(data.body)
            
             
        
        
    

messageParser = MessageParser()

def beginMessageParser():
    messageParser.init()
    messageParser.start()