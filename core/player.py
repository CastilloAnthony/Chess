from uuid import uuid4

class Player():
    def __init__(self, team:bool):
        self.__id = uuid4
        self.__team = team

    def __del__(self):
        del self.__id, self.__team