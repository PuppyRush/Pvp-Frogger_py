from socket import *
import socket
import socketserver
import threading
import gui.wating
PORT = 31500

class TCPHandler(socketserver.BaseRequestHandler):
    
    def setup(self):
        
        str = "%s가 접속하였습니다" % (self.client_address[0] )
        gui.wating.wattingThread.isConnect = True
        gui.wating.ui.beginButton.setText("시작하기")
        gui.wating.ui.connectingEdit.setText(str);  
        gui.wating.ui.beginButton.setEnabled(True)

        return super().setup()

    def handle(self):

        while(True):
            
            self.data = self.request.recv(1024);
            if(len(self.data)<=0):
                continue            

            self.messageExcurator(self.data)

        return super().handle()

    def messageExcurator(self,data):
        pass

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
    server = FroggerServer()
    server.init(ip,nickname)
    server.start()
    return server
    