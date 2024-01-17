from pieces.piece import Piece
from uuid import uuid4

class Knight(Piece):
    def __init__(self, team:bool):
        super().__init__()
        super().setName('Knight')
        super().setTeam(team) # True/False White/Black
        super().setValue(3)

    def listMoves(self, board, gameState):
        validMoves = []
        if self.getPinned():
            # return validMoves
            self.setValidMoves(validMoves)
        x, y = board.getCoordRules()
        xPos = None
        for index, value in enumerate(x):
            if value == self.getPos()[0]:
                xPos = index
                break
        if (int(self.getPos()[1]) < 8-1):
            # print('North')
            if (xPos > 0):
                # print('NorthWest')
                if board.getPositionToken(str(x[xPos-1])+str(int(self.getPos()[1])+2)) == None:
                    validMoves.append(str(x[xPos-1])+str(int(self.getPos()[1])+2))
                elif board.getPositionToken(str(x[xPos-1])+str(int(self.getPos()[1])+2)).getTeam() != self.getTeam():
                    if board.getPositionToken(str(x[xPos-1])+str(int(self.getPos()[1])+2)).getName() != 'King':
                        validMoves.append(str(x[xPos-1])+str(int(self.getPos()[1])+2))
            if (xPos < 7):
                # print('NorthEast')
                if board.getPositionToken(str(x[xPos+1])+str(int(self.getPos()[1])+2)) == None:
                    validMoves.append(str(x[xPos+1])+str(int(self.getPos()[1])+2))
                elif board.getPositionToken(str(x[xPos+1])+str(int(self.getPos()[1])+2)).getTeam() != self.getTeam():
                    if board.getPositionToken(str(x[xPos+1])+str(int(self.getPos()[1])+2)).getName() != 'King':
                        validMoves.append(str(x[xPos+1])+str(int(self.getPos()[1])+2))
        if (int(self.getPos()[1]) > 1+1):
            # print('South')
            if (xPos > 0):
                # print('SouthWest')
                if board.getPositionToken(str(x[xPos-1])+str(int(self.getPos()[1])-2)) == None:
                    validMoves.append(str(x[xPos-1])+str(int(self.getPos()[1])-2))
                elif board.getPositionToken(str(x[xPos-1])+str(int(self.getPos()[1])-2)).getTeam() != self.getTeam():
                    if board.getPositionToken(str(x[xPos-1])+str(int(self.getPos()[1])-2)).getName() != 'King':
                        validMoves.append(str(x[xPos-1])+str(int(self.getPos()[1])-2))
            if (xPos < 7):
                # print('SouthEast')
                if board.getPositionToken(str(x[xPos+1])+str(int(self.getPos()[1])-2)) == None:
                    validMoves.append(str(x[xPos+1])+str(int(self.getPos()[1])-2))
                elif board.getPositionToken(str(x[xPos+1])+str(int(self.getPos()[1])-2)).getTeam() != self.getTeam():
                    if board.getPositionToken(str(x[xPos+1])+str(int(self.getPos()[1])-2)).getName() != 'King':
                        validMoves.append(str(x[xPos+1])+str(int(self.getPos()[1])-2))
        if (xPos > 0+1):
            # print('West')
            if (int(self.getPos()[1]) < 8):
                # print('WestNorth')
                if board.getPositionToken(str(x[xPos-2])+str(int(self.getPos()[1])+1)) == None:
                    validMoves.append(str(x[xPos-2])+str(int(self.getPos()[1])+1))
                elif board.getPositionToken(str(x[xPos-2])+str(int(self.getPos()[1])+1)).getTeam() != self.getTeam():
                    if board.getPositionToken(str(x[xPos-2])+str(int(self.getPos()[1])+1)).getName() != 'King':
                        validMoves.append(str(x[xPos-2])+str(int(self.getPos()[1])+1))
            if (int(self.getPos()[1]) > 1):
                # print('WestSouth')
                if board.getPositionToken(str(x[xPos-2])+str(int(self.getPos()[1])-1)) == None:
                    validMoves.append(str(x[xPos-2])+str(int(self.getPos()[1])-1))
                elif board.getPositionToken(str(x[xPos-2])+str(int(self.getPos()[1])-1)).getTeam() != self.getTeam():
                    if board.getPositionToken(str(x[xPos-2])+str(int(self.getPos()[1])-1)).getName() != 'King':
                        validMoves.append(str(x[xPos-2])+str(int(self.getPos()[1])-1))
        if (xPos < 7-1):
            # print('East')
            if (int(self.getPos()[1]) < 8):
                # print('EastNorth')
                if board.getPositionToken(str(x[xPos+2])+str(int(self.getPos()[1])+1)) == None:
                    validMoves.append(str(x[xPos+2])+str(int(self.getPos()[1])+1))
                elif board.getPositionToken(str(x[xPos+2])+str(int(self.getPos()[1])+1)).getTeam() != self.getTeam():
                    if board.getPositionToken(str(x[xPos+2])+str(int(self.getPos()[1])+1)).getName() != 'King':
                        validMoves.append(str(x[xPos+2])+str(int(self.getPos()[1])+1))
            if (int(self.getPos()[1]) > 1):
                # print('EastSouth')
                if board.getPositionToken(str(x[xPos+2])+str(int(self.getPos()[1])-1)) == None:
                    validMoves.append(str(x[xPos+2])+str(int(self.getPos()[1])-1))
                elif board.getPositionToken(str(x[xPos+2])+str(int(self.getPos()[1])-1)).getTeam() != self.getTeam():
                    if board.getPositionToken(str(x[xPos+2])+str(int(self.getPos()[1])-1)).getName() != 'King':
                        validMoves.append(str(x[xPos+2])+str(int(self.getPos()[1])-1))
        # return validMoves
        validatedMoves = []
        for i in validMoves:
            if gameState.checkFuture(self.getPos(), i):
                validatedMoves.append(i)
        self.setValidMoves(validatedMoves)        
    
    def threatening(self, board):
        threat = []
        if self.getPinned():
            return threat
        x, _ = board.getCoordRules()
        xPos = None
        for index, value in enumerate(x):
            if value == self.getPos()[0]:
                xPos = index
        if (int(self.getPos()[1]) < 8-2):
            # print('North')
            if (xPos > 0):
                # print('NorthWest')
                if board.getPositionToken(str(x[xPos-1])+str(int(self.getPos()[1])+2)) == None:
                    threat.append(str(x[xPos-1])+str(int(self.getPos()[1])+2))
                elif board.getPositionToken(str(x[xPos-1])+str(int(self.getPos()[1])+2)).getTeam() != self.getTeam():
                    threat.append(str(x[xPos-1])+str(int(self.getPos()[1])+2))
                elif board.getPositionToken(str(x[xPos-1])+str(int(self.getPos()[1])+2)).getTeam() == self.getTeam():
                    threat.append(str(x[xPos-1])+str(int(self.getPos()[1])+2))
            if (xPos < 7):
                # print('NorthEast')
                if board.getPositionToken(str(x[xPos+1])+str(int(self.getPos()[1])+2)) == None:
                    threat.append(str(x[xPos+1])+str(int(self.getPos()[1])+2))
                elif board.getPositionToken(str(x[xPos+1])+str(int(self.getPos()[1])+2)).getTeam() != self.getTeam():
                    threat.append(str(x[xPos+1])+str(int(self.getPos()[1])+2))
                elif board.getPositionToken(str(x[xPos+1])+str(int(self.getPos()[1])+2)).getTeam() == self.getTeam():
                    threat.append(str(x[xPos+1])+str(int(self.getPos()[1])+2))
        if (int(self.getPos()[1]) > 1+2):
            # print('South')
            if (xPos > 0):
                # print('SouthWest')
                if board.getPositionToken(str(x[xPos-1])+str(int(self.getPos()[1])-2)) == None:
                    threat.append(str(x[xPos-1])+str(int(self.getPos()[1])-2))
                elif board.getPositionToken(str(x[xPos-1])+str(int(self.getPos()[1])-2)).getTeam() != self.getTeam():
                    threat.append(str(x[xPos-1])+str(int(self.getPos()[1])-2))
                elif board.getPositionToken(str(x[xPos-1])+str(int(self.getPos()[1])-2)).getTeam() == self.getTeam():
                    threat.append(str(x[xPos-1])+str(int(self.getPos()[1])-2))
            if (xPos < 7):
                # print('SouthEast')
                if board.getPositionToken(str(x[xPos+1])+str(int(self.getPos()[1])-2)) == None:
                    threat.append(str(x[xPos+1])+str(int(self.getPos()[1])-2))
                elif board.getPositionToken(str(x[xPos+1])+str(int(self.getPos()[1])-2)).getTeam() != self.getTeam():
                    threat.append(str(x[xPos+1])+str(int(self.getPos()[1])-2))
                elif board.getPositionToken(str(x[xPos+1])+str(int(self.getPos()[1])-2)).getTeam() == self.getTeam():
                    threat.append(str(x[xPos+1])+str(int(self.getPos()[1])-2))
        if (xPos > 0+1):
            # print('West')
            if (int(self.getPos()[1]) < 8):
                # print('WestNorth')
                if board.getPositionToken(str(x[xPos-2])+str(int(self.getPos()[1])+1)) == None:
                    threat.append(str(x[xPos-2])+str(int(self.getPos()[1])+1))
                elif board.getPositionToken(str(x[xPos-2])+str(int(self.getPos()[1])+1)).getTeam() != self.getTeam():
                    threat.append(str(x[xPos-2])+str(int(self.getPos()[1])+1))
                elif board.getPositionToken(str(x[xPos-2])+str(int(self.getPos()[1])+1)).getTeam() == self.getTeam():
                    threat.append(str(x[xPos-2])+str(int(self.getPos()[1])+1))
            if (int(self.getPos()[1]) > 1):
                # print('WestSouth')
                if board.getPositionToken(str(x[xPos-2])+str(int(self.getPos()[1])-1)) == None:
                    threat.append(str(x[xPos-2])+str(int(self.getPos()[1])-1))
                elif board.getPositionToken(str(x[xPos-2])+str(int(self.getPos()[1])-1)).getTeam() != self.getTeam():
                    threat.append(str(x[xPos-2])+str(int(self.getPos()[1])-1))
                elif board.getPositionToken(str(x[xPos-2])+str(int(self.getPos()[1])-1)).getTeam() == self.getTeam():
                    threat.append(str(x[xPos-2])+str(int(self.getPos()[1])-1))
        if (xPos < 7-1):
            # print('East')
            if (int(self.getPos()[1]) < 8):
                # print('EastNorth')
                if board.getPositionToken(str(x[xPos+2])+str(int(self.getPos()[1])+1)) == None:
                    threat.append(str(x[xPos+2])+str(int(self.getPos()[1])+1))
                elif board.getPositionToken(str(x[xPos+2])+str(int(self.getPos()[1])+1)).getTeam() != self.getTeam():
                    threat.append(str(x[xPos+2])+str(int(self.getPos()[1])+1))
                elif board.getPositionToken(str(x[xPos+2])+str(int(self.getPos()[1])+1)).getTeam() == self.getTeam():
                    threat.append(str(x[xPos+2])+str(int(self.getPos()[1])+1))
            if (int(self.getPos()[1]) > 1):
                # print('EastSouth')
                if board.getPositionToken(str(x[xPos+2])+str(int(self.getPos()[1])-1)) == None:
                    threat.append(str(x[xPos+2])+str(int(self.getPos()[1])-1))
                elif board.getPositionToken(str(x[xPos+2])+str(int(self.getPos()[1])-1)).getTeam() != self.getTeam():
                    threat.append(str(x[xPos+2])+str(int(self.getPos()[1])-1))
                elif board.getPositionToken(str(x[xPos+2])+str(int(self.getPos()[1])-1)).getTeam() == self.getTeam():
                    threat.append(str(x[xPos+2])+str(int(self.getPos()[1])-1))
        return threat
# end Pawn