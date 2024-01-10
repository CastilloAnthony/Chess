from uuid import uuid4
from core.board import Board
from pieces.pawn import Pawn
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.rook import Rook
from pieces.queen import Queen
from pieces.king import King

class Game():
    def __init__(self):
        self.__id = uuid4
        self.__board = Board()
        self.__currentTurn = True # True/False White/Black

    def __del__(self):
        del self.__board

    def getID(self):
        return self.__id
    
    def getBoard(self):
        return self.__board.getBoard()
    
    def getBoardID(self):
        return self.__board.getID()
    
    def newGame(self):
        del self.__board
        self.__board = Board()
        x, _ = self.__board.getCoordRules()

        # Setting White
        for i in range(8):
            newPawn = Pawn(True)
            self.__board.setPiece(newPawn, x[i]+'2')
        newRook0 = Rook(True)
        self.__board.setPiece(newRook0, 'A1')
        newKnight0 = Knight(True)
        self.__board.setPiece(newKnight0, 'B1')
        newBishop0 = Bishop(True)
        self.__board.setPiece(newBishop0, 'C1')
        newQueen = Queen(True)
        self.__board.setPiece(newQueen, 'D1')
        newKing = King(True)
        self.__board.setPiece(newKing, 'E1')
        newBishop1 = Bishop(True)
        self.__board.setPiece(newBishop1, 'F1')
        newKnight1 = Knight(True)
        self.__board.setPiece(newKnight1, 'G1')
        newRook1 = Rook(True)
        self.__board.setPiece(newRook1, 'H1')
        
        # Setting Black
        for i in range(8):
            newPawn = Pawn(False)
            self.__board.setPiece(newPawn, x[i]+'7')
        newRook0 = Rook(False)
        self.__board.setPiece(newRook0, 'A8')
        newKnight0 = Knight(False)
        self.__board.setPiece(newKnight0, 'B8')
        newBishop0 = Bishop(False)
        self.__board.setPiece(newBishop0, 'C8')
        newQueen = Queen(False)
        self.__board.setPiece(newQueen, 'D8')
        newKing = King(False)
        self.__board.setPiece(newKing, 'E8')
        newBishop1 = Bishop(False)
        self.__board.setPiece(newBishop1, 'F8')
        newKnight1 = Knight(False)
        self.__board.setPiece(newKnight1, 'G8')
        newRook1 = Rook(False)
        self.__board.setPiece(newRook1, 'H8')

        # Save to Hisotry & Reveal Board
        self.__board.snapshotBoard()
        print(self.__board)

    def newTestGame(self):
        del self.__board
        self.__board = Board()
        x, _ = self.__board.getCoordRules()

        # Setting White
        newRook0 = Rook(True)
        self.__board.setPiece(newRook0, 'A1')
        newKnight0 = Knight(True)
        self.__board.setPiece(newKnight0, 'B1')
        newBishop0 = Bishop(True)
        self.__board.setPiece(newBishop0, 'C1')
        newQueen = Queen(True)
        self.__board.setPiece(newQueen, 'D1')
        newKing = King(True)
        self.__board.setPiece(newKing, 'E1')
        newBishop1 = Bishop(True)
        self.__board.setPiece(newBishop1, 'F1')
        newKnight1 = Knight(True)
        self.__board.setPiece(newKnight1, 'G1')
        newRook1 = Rook(True)
        self.__board.setPiece(newRook1, 'H1')
        
        # Setting Black
        newRook0 = Rook(False)
        self.__board.setPiece(newRook0, 'A8')
        newKnight0 = Knight(False)
        self.__board.setPiece(newKnight0, 'B8')
        newBishop0 = Bishop(False)
        self.__board.setPiece(newBishop0, 'C8')
        newQueen = Queen(False)
        self.__board.setPiece(newQueen, 'D8')
        newKing = King(False)
        self.__board.setPiece(newKing, 'E8')
        newBishop1 = Bishop(False)
        self.__board.setPiece(newBishop1, 'F8')
        newKnight1 = Knight(False)
        self.__board.setPiece(newKnight1, 'G8')
        newRook1 = Rook(False)
        self.__board.setPiece(newRook1, 'H8')

        # Save to Hisotry & Reveal Board
        self.__board.snapshotBoard()
        print(self.__board)

    def getTokenMoves(self, position:str):
        return self.__board.getTokenMoves(position)
    
    def getTokenThreatens(self, position:str):
        return self.__board.getTokenThreats(position)
    
    def getTokenStatus(self, position:str):
        return self.__board.getPositionInfo(position)
    
    def move(self, startPos, endPos):
        result = self.__board.movePiece(startPos, endPos)
        print(self.__board)
        return result

    def displayBoard(self):
        print(self.__board)

    def getScore(self):
        return self.__board.getScore()
    
    def displayScore(self):
        print('\t--- Score ---\n' + 'White: ' + str(self.__board.getScore()[True]) + '\nBlack: ' + str(self.__board.getScore()[False]))

    def findChecks(self):
        for i in self.__board:
            if self.__board.getPositionToken(i) != None:
                pass

    def calculateThreats(self):
        self.__board.calculateThreats()

    def calculateKing(self, position:str):
        return self.__board.calculateKing(position)
    
    def getTurn(self):
        return self.__currentTurn
    
    def endTurn(self):
        if self.__currentTurn:
            self.__currentTurn = False
        else:
            self.__currentTurn = True
# end Game