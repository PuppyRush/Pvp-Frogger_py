import socket, sys
import pickle
import threading
import queue
import game.multi.MessagePacker

PORT = 31500

class FroggerClient(threading.Thread):
    
    def init(self,ip,nickname):
        self.serverIp = ip
        self.serverPort = PORT
        self.nickname = nickname
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientSocket.connect( (self.serverIp, PORT))
        self.messageQ = queue.Queue()
    
    def run(self):
        while(True):
            if(self.messageQ.qsize() == 0):
                continue
            else:
                self.sendMessage()

    def load(self,data):
        if(type(data) == type(game.multi.MessagePacker.Message)):
            self.messageQ.put(data)
            

    def sendMessage(self):
        self.clientSocket.send( pickle.dumps( self.messageQ.get() ))
            

def beginClientSocket(ip,nickname):
    
    client.init(ip,nickname)
    
    
    
client = FroggerClient()