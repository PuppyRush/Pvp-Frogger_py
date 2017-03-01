import enum
import game
from game import GameApp
class MessageKind(enum.Enum):
    HECKLER=1
    MAP=2
    PLAYER=3
    GAMEINFO=4
    PLAYER_INFO=5
    
class Message(object):
    def __init__(self,msgKind=MessageKind):
        self.header=msgKind

class Heckler(Message):
    def __init__(self,msgKind=MessageKind, hecklers=[],beginIdx=int,endIdx=int,screenHeightCount=int):
        super().__init__(msgKind)
        
        self.heightSize = screenHeightCount
        self.hecklers = []

        for i in range(beginIdx,endIdx):
            self.hecklers.append(hecklers[i])
            

class Map(Message):
    def __init__(self,msgKind=MessageKind,earth=[],beginIdx=int,endIdx=int,screenHeightCount=int):
        super().__init__(msgKind)
        self.mapSize = screenHeightCount
        self.map = []
        
        for i in range(beginIdx,endIdx):
            self.map.append(earth[i])
            

class Player(Message):
    def __init__(self,msgKind=MessageKind,position=[],jumpCount=0,nickname=str,number=int):
        super().__init__(msgKind)
        self.position = ()
        self.jumpCount = jumpCount
        self.nickname = nickname
        self.number = number


class GameInfo(Message):
    def __init__(self,heightMax=int):
        super().__init__(msgKind)      
        self.heightFullSize=heightMax



class PlayerInfo(Message):
    def __init__(self,msgKind=MessageKind,name=str):
        super().__init__(msgKind)
        self.nickname = name
