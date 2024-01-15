from uuid import uuid4

class Piece():
    def __init__(self):
        self.__id = uuid4()
        self.__name = None
        self.__team = None # True/False White/Black
        self.__value = 0
        self.__initial = True # True/Flase Not Moved/Moved
        self.__position = None
        self.__pinned = False
        self.__validMoves = []

    def __del__(self):
        del self.__id, self.__name, self.__team, self.__value, self.__initial, self.__position, self.__validMoves

    def __str__(self):
        if self.__team:
            info = 'White'
        else:
            info = 'Black'
        info += ' ' + self.__name
        if len(info) < 12:
            info += '\t'
        return info
    
    def readStatus(self):
        info = 'ID:\t\t\t'+ str(self.__id) + '\nName:\t\t' + str(self.__name) + '\nTeam:\t\t' + str(self.__team) + '\nValue:\t\t' + str(self.__value) + '\nInitial:\t' + str(self.__initial) + '\nPosition:\t' + str(self.__position)
        return info
    
    def getStatus(self):
        info = {
            'id':self.__id,
            'name':self.__name,
            'team':self.__team,
            'value':self.__value,
            'initial':self.__initial,
            'position':self.__position,
        }
        return info
    
    def listMoves(self, board):
        pass
        
    def getID(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def getTeam(self):
        return self.__team
    
    def getValue(self):
        return self.__value

    def getInitial(self):
        return self.__initial
    
    def getPos(self):
        return self.__position
    
    def setName(self, name):
        self.__name = name

    def setTeam(self, team):
        self.__team = team

    def setValue(self, value):
        self.__value = value

    def flipInitial(self):
        self.__initial = False

    def setPos(self, position:str):
        self.__position = position

    def getPinned(self):
        return self.__pinned
    
    def setPinned(self, pinned):
        self.__pinned = pinned

    def getValidMoves(self):
        return self.__validMoves
    
    def setValidMoves(self, validMoves:list):
        self.__validMoves = validMoves
# end Piece