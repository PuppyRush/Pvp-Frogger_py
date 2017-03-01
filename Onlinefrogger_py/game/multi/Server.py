import socket
import select
import threading
import pickle
import game
import gui
from game.multi import MessagePacker as Packer, MessageParser as Parser, Message

PORT = 31500

class FroggerServer(threading.Thread):
    
    def init(self,ip,nickname):                                   
        self.serverIp = ip
        self.serverPort = PORT
        self.nickname = nickname

        self.serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.serverSocket.bind((ip,PORT))
        self.serverSocket.listen(10)             
        
        self.connectionList = []
        self.connectionList.append(self.serverSocket)

        self.__packer = Packer.MessagePacker()
        self.__parser = Parser.MessageParser()
                
      
        
    def __setup(self,ip=str):
        str = "%s가 접속하였습니다" % (ip)
        gui.Watting.wattingThread.isConnect = True
        gui.Watting.ui.connectingEdit.setText(str);
        gui.Watting.ui.beginButton.setText("시작하기")  
        gui.Watting.ui.beginButton.setEnabled(True)
        

    def __sendMessage(self,client=socket.socket):
        data = self.__packer.getMessage()
        if type(data) != bool:
            client.send( pickle.dumps( data ))


    def __recvMessage(self,sock):
        data = sock.recv(2048)
        if len(data)>0 :
            self.__parser.loader(pickle.loads(data))


    def run(self):
        while True:
            read, write,error = select.select(self.connectionList,[],[],10)

            for sock in read:
                if sock == self.serverSocket:

                    clientSocket , addr_info = self.serverSocket.accept()
                    self.connectionList.append(clientSocket)
                    self.__setup(addr_info[0])

                else:
                    self.__recvMessage(sock)

            for client in self.connectionList:
                self.__sendMessage(client)

                
    def putMessage(self,body=object,kind=Packer.MessageKind):    
        self.__packer.packingMessage(body,kind)
    

    def getMessage(self,kind=Packer.MessageKind):
        if kind == Packer.MessageKind.GAME:
            return self.__parser.getGameMessage()
        elif kind == Packer.MessageKind.GUI:
            return self.__parser.getGuiMessage()
        elif kind == Packer.MessageKind.NETWORK:
            return self.__parser.getNetworkMessage()
        else:
            print("not exist message kind")
            return False

    def recvPlayerInfo(self):
        print(id(self.__parser))

        while True:
            if not self.__parser.empty(Packer.MessageKind.GAME):
                msg = self.getMessage(Packer.MessageKind.GAME)
            
                if msg.header == Message.MessageKind.PLAYER_INFO:
                    return msg.nickname
                else:
                    self.__packer.packingMessage(msg,Packer.MessageKind.GAME)

    def getPacker(self):
        return self.__packer

    def getParser(self):
        return self.__parser

def beginServerSocket(ip,nickname):
    server = FroggerServer()
    server.init(ip,nickname)
    server.start()
  
    return server
    
    
