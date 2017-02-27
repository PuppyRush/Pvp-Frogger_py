import socket, sys
import pickle
import threading
import queue
import game
from game.multi import MessagePacker, MessageParser, Message


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
            self.__resolveRequestedInfo()

    def putMessage(self,body=object,kind=object):    
        self.__packer.packingMessage(data,kind)
        

    def getMessage(self,kind=object):
        
        if kind == MessagePacker.MessageKind.GAME:
            return self.__parser.getGameMessage()
        elif kind == MessagePacker.MessageKind.GUI:
            return self.__parser.getGuiMessage()
        elif kind == MessagePacker.MessageKind.NETWORK:
            return self.__parser.getNetworkMessage()
        else:
            print("not exist message kind")
            return False  

    def __resolveRequestedInfo(self):
        if not self.__parser.empty(MessagePacker.MessageKind.GAME):
            msg = Message.PlayerInfo(Message.MessageKind.PLAYER_INFO, self.nickname)
            self.__packer.packingMessage(msg,MessagePacker.MessageKind.GAME)
           

    def __sendMessage(self):
        
        if not self.__packer.empty():
            self.clientSocket.send( pickle.dumps( self.__packer.getMessage() ))
            
    def __recvMessage(self):
        data = self.clientSocket.recv(1024)

        if len(data)<=0 :
            return
        self.__parser.loader(pickle.loads(data))
        

def beginClientSocket(ip,nickname):
    client = FroggerClient()
    client.init(ip,nickname)
    client.start()
    return client
    
