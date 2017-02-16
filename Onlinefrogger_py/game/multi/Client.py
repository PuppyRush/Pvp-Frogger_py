import socket, sys


PORT = 31500

class FroggerClient(object):
    
    def __init__(self,ip,nickname):
        self.serverIp = ip
        self.serverPort = PORT
        self.nickname = nickname
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def beginClient(self):
        self.clientSocket.connect( (self.serverIp, PORT))
        data = bytearray()
        data.extend(map(ord,self.nickname))
        self.clientSocket.send(data)
        

def beginClientSocket(ip,nickname):
    client = FroggerClient(ip,nickname)
    client.beginClient()
    return client
    