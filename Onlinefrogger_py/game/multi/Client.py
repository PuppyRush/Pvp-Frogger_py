import socket, sys
import pickle
import threading
import queue
import game
from game.multi import MessagePacker, MessageParser


PORT = 31500

class FroggerClient(threading.Thread):
    
    def init(self,ip,nickname):
        self.serverIp = ip
        self.serverPort = PORT
        self.nickname = nickname
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientSocket.connect( (self.serverIp, PORT))
        
        self.__packer = MessagePacker.MessagePacker()
        self.__parser = MessageParser.MessageParser()

    def run(self):
        while(True):
            self.__sendMessage()
            self.__recvMessage()

    def putMessage(self,body=object,kind=MessagePacker.MessageKind):    
        self.__packer.packingMessage(data,kind)
           
    def getMessage(self,kind=MessageParser.MessageKind):
        
        if kind == MessageParser.MessageKind.GAME:
            return self.__parser.getGameMessage
        elif kind == MessageParser.MessageKind.GUI:
            return self.__parser.getGuiMessage
        elif kind == MessageParser.MessageKind.NETWORK:
            return self.__parser.getNetworkMessage
        else:
            print("not exist message kind")
            return            

    def __sendMessage(self):
        if(self.messageQ.qsize() == 0):
            self.clientSocket.send( pickle.dumps( self.messageQ.get() ))
            
    def __recvMessage(self):
        data = self.clientSocket.recv(1024)
        self.__parser.loader(data)
        pass

def beginClientSocket(ip,nickname):
    client = FroggerClient()
    client.init(ip,nickname)
    return client
    
