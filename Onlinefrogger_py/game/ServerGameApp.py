import game
from game import Player, Heckler, Map, Controller as Ctl, GameApp as GA
from game.multi import Message , Server, MessagePacker as Packer


class ServerGameApp(object):

    def __init__(self,ctl=Ctl.Controller, players=[],level=int,speed=int,maxHeightCount=int):
        self.ctl = ctl
        self.__GAP_OF_FROG = GA.GameInfo.WIDTH_COUNT.value * GA.GameInfo.WIDTH_SIZE.value /(len(players)+1)
        self.__level = level
        self.__speed = speed
        self.MAX_HEIGHT_COUNT = maxHeightCount
        self.__setPlayer(players)
        self.__setMap()
        self.__setHecklers()

    def __setPlayer(self,players=[]):

        self.players = []
        order =0
        for player in players:
            x = int((order+1)*GA.GameInfo.WIDTH_COUNT.value/(len(players)+1))
            y = 0
            self.players.append( game.Player.Player(self.ctl,player[0], player[1], 
                                                    [ (order+1)*self.__GAP_OF_FROG, GA.GameInfo.HEIGHT_COUNT.value], 
                                                    [ x,y ]) )
            order+=1
          
    def __setMap(self):
        
        self.map = Map.Map(self.ctl,self.MAX_HEIGHT_COUNT)

    def __setHecklers(self):
        
        self.hecklers = []    
        for i in self.map.earth:
            self.hecklers.append( Heckler.HecklerFactory(self.ctl, i.mapKind, i.heightIdx ,self.__speed).getHecklers())
       