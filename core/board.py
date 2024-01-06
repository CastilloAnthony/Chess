from uuid import uuid4
from copy import deepcopy

class Board():
    def __init__(self):
        self.__id = uuid4()
        self.__x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.__y = ['1', '2', '3', '4', '5', '6', '7', '8']
        self.__board = {}
        for i in self.__x:
            for j in self.__y:
                self.__board[str(i+j)] = 'Empty\t\t'
        self.__score = [0, 0] # [Black, White]/[False, True]
        self.__graveyard = []
        self.__history = []
        self.__history.append(deepcopy(self.__board))

    def __del__(self):
        pass

    def __str__(self):
        #info = 'ID:\t' + str(self.__id)
        infoBoard = ''
        for i in self.__x:
            for j in self.__y:
                infoBoard += str(i+j) + ': ' + str(self.__board[str(i+j)]) + '\t'
            infoBoard += '\n'
        #info += '\n' + infoBoard
        return infoBoard
    
    def clearBoard(self):
        try:
            del self.__board
            self.__board = {}
            for i in self.__x:
                for j in self.__y:
                    self.__board[str(i+j)] = 'Empty\t\t'
            return True
        except:
            return False

    def getID(self):
        return self.__id
    
    def getBoard(self):
        return deepcopy(self.__board)
    
    def getCoordRules(self):
        return (self.__x, self.__y)
    
    def getScore(self):
        return self.__score
    
    def setPiece(self, piece, position:str):
        try:
            self.__board[position] = piece
            self.__board[position].setPos(position)
            return True
        except:
            return False
        
    def getPositionInfo(self, position:str):
        if self.__board[position] != 'Empty\t\t':
            return self.__board[position].getStatus()
        else:
            return False
    
    def getPositionToken(self, position:str):
        if self.__board[position] != 'Empty\t\t':
            return self.__board[position]
        else:
            return None
        
    def getTokenMoves(self, position:str):
        if self.__board[position] != 'Empty\t\t':
            return self.__board[position].listMoves(deepcopy(self))
        else:
            return None
        
    def getTokenThreats(self, position:str):
        if self.__board[position] != 'Empty\t\t':
            return self.__board[position].threatening(deepcopy(self))
        else:
            return None
        
    def movePiece(self, startPos, endPos):
        if endPos in self.__board[startPos].listMoves(deepcopy(self)):
            if self.__board[endPos] != 'Empty\t\t': # Taking a Piece
                self.__score[self.__board[startPos].getTeam()] += self.__board[endPos].getValue()
                self.__graveyard.append(self.__board[endPos])
                self.__board[endPos] = 'Empty\t\t'
            elif self.__board[startPos].getName() == 'Pawn': # Check for En Passant
                if self.__board[startPos].getEnPassant():
                    if self.__board[startPos].getTeam(): # White En Passant
                        self.__score[self.__board[startPos].getTeam()] += self.__board[endPos[0]+str(int(endPos[1])-1)].getValue()
                        self.__graveyard.append(self.__board[endPos[0]+str(int(endPos[1])-1)])
                        self.__board[endPos[0]+str(int(endPos[1])-1)] = 'Empty\t\t'
                    else: # Black En Passant
                        self.__score[self.__board[startPos].getTeam()] += self.__board[endPos[0]+str(int(endPos[1])+1)].getValue()
                        self.__graveyard.append(self.__board[endPos[0]+str(int(endPos[1])+1)])
                        self.__board[endPos[0]+str(int(endPos[1])+1)] = 'Empty\t\t'
            self.__board[endPos] = self.__board[startPos]
            print(startPos, self.__board[startPos], endPos, self.__board[endPos])
            self.__board[endPos].setPos(endPos)
            self.__board[startPos] = 'Empty\t\t'
            if self.__board[endPos].getInitial():
                self.__board[endPos].flipInitial()
            self.__history.append(deepcopy(self.__board))
            return True
        else:
            return False
        # try:
        #     if endPos in self.__board[startPos].listMoves(deepcopy(self)):
        #         if self.__board[endPos] != 'Empty\t\t': # Taking a Piece
        #             self.__score[self.__board[startPos].getTeam()] += self.__board[endPos].getValue()
        #             self.__graveyard.append(self.__board[endPos])
        #             self.__board[endPos] = 'Empty\t\t'
        #         if self.__board[startPos].getName() == 'Pawn': # Check for En Passant
        #             if self.__board[startPos].getEnPassant():
        #                 if self.__board[startPos].getTeam(): # White En Passant
        #                     self.__score[self.__board[startPos].getTeam()] += self.__board[endPos[0]+str(int(endPos[1])-1)].getValue()
        #                     self.__graveyard.append(self.__board[endPos[0]+str(int(endPos[1])-1)])
        #                     self.__board[endPos[0]+str(int(endPos[1])-1)] = 'Empty\t\t'
        #                 else: # Black En Passant
        #                     self.__score[self.__board[startPos].getTeam()] += self.__board[endPos[0]+str(int(endPos[1])+1)].getValue()
        #                     self.__graveyard.append(self.__board[endPos[0]+str(int(endPos[1])+1)])
        #                     self.__board[endPos[0]+str(int(endPos[1])+1)] = 'Empty\t\t'
        #         self.__board[endPos] = self.__board[startPos]
        #         self.__board[endPos].setPos(endPos)
        #         self.__board[startPos] = 'Empty\t\t'
        #         if self.__board[endPos].getInitial():
        #             self.__board[endPos].flipInitial()
        #         self.__history.append(deepcopy(self.__board))
        #         return True
        #     else:
        #         return False
        # except:
        #     return False
        
    def snapshotBoard(self):
        self.__history.append(deepcopy(self.__board))

    def getHistory(self, number:int):
        return self.__history[number]
# end Board