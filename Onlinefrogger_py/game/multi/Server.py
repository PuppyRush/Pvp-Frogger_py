import socket
import socketserver
import threading
import gui.Watting
import game
import pickle
from builtins import bytearray
from game.multi import MessagePacker, MessageParser
PORT = 31500


class TCPHandler(socketserver.BaseRequestHandler):
    
    def setup(self):
            
        str = "%s가 접속하였습니다" % (self.client_address[0] )
        gui.Watting.wattingThread.isConnect = True
        gui.Watting.ui.beginButton.setText("시작하기")
        gui.Watting.ui.connectingEdit.setText(str);  
        gui.Watting.ui.beginButton.setEnabled(True)
        
        self.__packer = MessagePacker.MessagePacker()
        self.__parser = MessageParser.MessageParser()

        return super().setup()

    def handle(self):
        
        while(True):
            self.__sendMessage()
            self.__recvMessage()         

        return super().handle()

    def putMessage(self,body=object,kind=MessagePacker.MessageKind):    
        self.__packer.packingMessage(data,kind)

    def getMessage(self,kind=MessageParser.MessageKind):
        
        if kind == MessageParser.MessageKind.GAME:
            return self.tcpHandler.__parser.getGameMessage
        elif kind == MessageParser.MessageKind.GUI:
            return self.__parser.getGuiMessage
        elif kind == MessageParser.MessageKind.NETWORK:
            return self.__parser.getNetworkMessage
        else:
            print("not exist message kind")
            return       

    def __sendMessage(self):
        data = self.__packer.getMessage()
        if type(data) != bool:
            self.request.send( pickle.dumps( data ))
            
    def __recvMessage(self):
        data = self.request.recv(1024)
        temp = pickle.loads(data) 
        self.__parser.loader(temp)
        

class FroggerServer(threading.Thread):
    
    def init(self,ip,nickname):
        self.serverIp = ip
        self.serverPort = PORT
        self.nickname = nickname

        tupe = (self.serverIp,self.serverPort)               
        self.__tcpHandler = TCPHandler()        
        self.__serverSocket = socketserver.TCPServer(tupe,self.__tcpHandler)
        
    def run(self):
        self.__serverSocket.serve_forever()    

       
    def putMessage(self,body=object,kind=MessagePacker.MessageKind):    
        self.__tcpHandler.putMessage(body,kind)
           
    def getMessage(self,kind=MessageParser.MessageKind):
        return self.getMessage(kind)
        

def beginServerSocket(ip,nickname):
    server = FroggerServer()
    server.init(ip,nickname)
    server.start()

    return server
    
    
