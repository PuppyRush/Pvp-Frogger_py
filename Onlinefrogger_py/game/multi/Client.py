import socket
import sys
import pickle
import threading
import queue
import game
import select
from game.multi import MessagePacker, MessageParser, Message


PORT = 31500

class FroggerClient(threading.Thread):
    
    def init(self,ip,nickname):
        self.serverIp = ip
        self.serverPort = PORT
        self.nickname = nickname

        self.__packer = MessagePacker.MessagePacker()
        self.__parser = MessageParser.MessageParser()


        self.clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.clientSocket.connect((self.serverIp,self.serverPort))                
        self.__sendClientInfo()

    def run(self):
        while(True):
            read, write,error = select.select([self.clientSocket],[],[],10)

            for sock in read:
                if sock == self.clientSocket:
                    self.__recvMessage(sock)

            self.__sendMessage()


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

    def getPacker(self):
        return self.__packer

    def getParser(self):
        return self.__parser

    def __sendClientInfo(self):
        msg = Message.PlayerInfo(Message.MessageKind.PLAYER_INFO, self.nickname)
        self.__packer.packingMessage(msg,MessagePacker.MessageKind.GAME)
           
    def __recvMessage(self,sock):
        data = sock.recv(2048)
        if len(data)>0 :
            self.__parser.loader(pickle.loads(data))

    def __sendMessage(self):
        if not self.__packer.empty():
            self.clientSocket.send( pickle.dumps( self.__packer.getMessage() ))
            


def beginClientSocket(ip,nickname):
    client = FroggerClient()
    client.init(ip,nickname)
    client.start()
    return client
    