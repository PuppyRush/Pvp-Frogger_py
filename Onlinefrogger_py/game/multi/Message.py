import enum

class MessageKind(enum.Enum):
    HECKLER=1
    MAP=2
    PLAYER=3
    GAMEINFO=4
    PLAYER_INFO=5
    
class Message(object):
    def __init__(self,msgKind=MessageKind,body=object):
        self.msgKind=msgKind
        self.body=object

class Heckler(Message):
    def __init__(self,msgKind=MessageKind, hecklers=[],beginIdx=int,endIdx=int,screenHeightCount=int):
        super(msgKind)
        
        self.heightSize = screenHeightCount
        self.hecklers = []

        for i in range(beginIdx,endIdx):
            self.map.append(hecklers[i])
            

class Map(Message):
    def __init__(self,msgKind=MessageKind,mapRows=[],beginIdx=int,endIdx=int,screenHeightCount=int):
        super(msgKind)
        self.mapSize = screenHeightCount
        self.map = []
        
        for i in range(beginIdx,endIdx):
            self.map.append(mapRows[i])
            

class Player(Message):
    def __init__(self,msgKind=MessageKind,position=[],jumpCount=0,):
        super(msgKind)
        self.position = ()
        self.jumpCount = jumpCount


class GameInfo(Message):
    def __init__(self,msgKind=MessageKind,gameInfo=object,heightMax=int,clockTick=int):
        super(msgKind)
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
    def __int__(self,msgKind=MessageKind,name=str):
        self.nickname = name
