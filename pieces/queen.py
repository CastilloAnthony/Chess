from pieces.piece import Piece
from pieces.rook import Rook
from pieces.bishop import Bishop

class Queen(Rook, Bishop, Piece):
    def __init__(self, team:bool):
        Piece.__init__(self)
        self.setName('Queen')
        self.setTeam(team) # True/False White/Black
        self.setValue(9)

    def listMoves(self, board, gameState):
        if self.getPinned():
            # return []
            self.setValidMoves([])
        # return Rook.listMoves(self, board) + Bishop.listMoves(self, board)
        Rook.listMoves(self, board, gameState)
        temp = self.getValidMoves()
        Bishop.listMoves(self, board, gameState)
        validMoves = temp+self.getValidMoves()
        validatedMoves = []
        for i in validMoves:
            if gameState.checkFuture(self.getPos(), i):
                validatedMoves.append(i)
        self.setValidMoves(validatedMoves)    
        # self.setValidMoves()   
    
    def threatening(self, board):
        if self.getPinned():
            return []
        x, _ = board.getCoordRules()
        xPos = None
        for index, value in enumerate(x):
            if value == self.getPos()[0]:
                xPos = index
        return Rook.threatening(self, board) + Bishop.threatening(self, board)
# end Queen