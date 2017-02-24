import game.GameApp

import gui.Main , gui.Main, gui.Watting
import init
from game.multi import *
from game import *


#initInfo = init.InitInfo()

#game.multi.MessageParser.beginMessageParser()
#game.multi.MessagePacker.beginMessagePacker()

isServer = True
ip = ""
nickname = ""


#isServer, nickname, ip = gui.Main.beginUI("localhost")

#if(isServer):
    
#    level , speed = gui.Server.beginUI()

#    level = int(level)
#    speed = int(speed)

#    game.multi.Server.beginServerSocket(ip,nickname)      
#    gui.Watting.beginUI()

#else:
#    game.multi.Client.beginClientSocket(ip,nickname)


players = [(1,"asd"),(2,"sd")]
         

game.GameApp.beginServerGameApp(players,3,0)