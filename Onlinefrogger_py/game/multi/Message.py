import enum

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
            self.map.append(hecklers[i])
            

class Map(Message):
    def __init__(self,msgKind=MessageKind,mapRows=[],beginIdx=int,endIdx=int,screenHeightCount=int):
        super().__init__(msgKind)
        self.mapSize = screenHeightCount
        self.map = []
        
        for i in range(beginIdx,endIdx):
            self.map.append(mapRows[i])
            

class Player(Message):
    def __init__(self,msgKind=MessageKind,position=[],jumpCount=0,):
        super().__init__(msgKind)
        self.position = ()
        self.jumpCount = jumpCount


class GameInfo(Message):
    def __init__(self,msgKind=MessageKind,gameInfo=object,heightMax=int,clockTick=int):
        super().__init__(msgKind)
        self.widthCount=gameInfo.WIDTH_COUNT.value
        self.heightCount=gameInfo.HEIGHT_COUNT.value
        self.widthSize=gameInfo.WIDTH_COUNT.value
        self.heightSize=gameInfo.HEIGHT_SIZE.value
        self.frogSize=gameInfo.FROG_SIZE.value
        self.screenHeightSize=gameInfo.SCREEN_HEIGHT_SIZE.value
        self.screenWidthSize=gameInfo.SCREEN_WIDTH_SIZE.value
        self.heightFullSize=heightMax
        self.clockTick=clockTick

class PlayerInfo(Message):
    def __init__(self,msgKind=MessageKind,name=str):
        super().__init__(msgKind)
        self.nickname = name
