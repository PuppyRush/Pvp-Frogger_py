import socket
import socketserver
import threading
import gui.Watting
import game.multi.MessageParser
import pickle
from builtins import bytearray

PORT = 31500


class TCPHandler(socketserver.BaseRequestHandler):
    
    def setup(self):
            
        str = "%s가 접속하였습니다" % (self.client_address[0] )
        gui.Watting.wattingThread.isConnect = True
        gui.Watting.ui.beginButton.setText("시작하기")
        gui.Watting.ui.connectingEdit.setText(str);  
        gui.Watting.ui.beginButton.setEnabled(True)
        
        return super().setup()

    def handle(self):
        
        while(True):
            
            data = self.request.recv(1024)
            temp = pickle.loads(data) 
        
            game.multi.MessageParser.messageParser.load(temp)

        return super().handle()


class FroggerServer(threading.Thread):
    
    def init(self,ip,nickname):
        self.serverIp = ip
        self.serverPort = PORT
        self.nickname = nickname
        tupe = (self.serverIp,self.serverPort)

        
        
        self.serverSocket = socketserver.TCPServer(tupe,TCPHandler)
        
    def run(self):
        self.serverSocket.serve_forever()    

                



def beginServerSocket(ip,nickname):
    
    server.init(ip,nickname)
    server.start()
    
    
server = FroggerServer()