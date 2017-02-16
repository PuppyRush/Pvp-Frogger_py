import gui.main, gui.wating, gui.server
import game.multi.Server, game.multi.Client
import init

#initInfo = init.InitInfo()

isServer = True
ip = ""
nickname = ""


isServer, nickname, ip = gui.main.beginUI("localhost")

if(isServer):

    level , speed = gui.server.beginUI()

    level = int(level)
    speed = int(speed)

    serverSocket = game.multi.Server.beginServerSocket(ip,nickname)      
    gui.wating.beginUI(serverSocket)

else:
    clientSocket = game.multi.Client.beginClientSocket(ip,nickname)