from uuid import uuid4

class Player():
    def __init__(self, team:bool):
        self.__id = uuid4
        self.__team = team
        self.__name = 'Player1'

    def __del__(self):
        del self.__id, self.__team

    def getID(self):
        return self.__id
    
    def getTeam(self):
        return self.__team
    
    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name