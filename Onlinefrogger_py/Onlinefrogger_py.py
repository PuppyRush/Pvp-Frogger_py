import game
from game import GameApp
from game.multi import Client, Server

import gui
from gui import Main, Watting, Server

import init

#initInfo = init.InitInfo()

isServer = True
ip = ""
nickname = ""

isServer, nickname, ip = gui.Main.beginUI("localhost")

if(isServer):
    
    level , speed = gui.Server.beginUI()

    level = int(level)
    speed = int(speed)

    serverSocket = game.multi.Server.beginServerSocket(ip,nickname)      
    gui.Watting.beginUI()

    clientFrogNickname = serverSocket.recvPlayerInfo()

    players = [[1,"PuppyRush"],[2,clientFrogNickname]]

    game.GameApp.beginServerGameApp(players,3,0,serverSocket)

else:
    clientSocket = game.multi.Client.beginClientSocket(ip,nickname)
    game.GameApp.beginClientGameApp(clientSocket)

