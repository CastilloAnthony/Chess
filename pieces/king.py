from pieces.piece import Piece
from pieces.queen import Queen

class King(Queen, Piece):
    def __init__(self, team:bool):
        Piece.__init__(self)
        self.setName('King')
        self.setTeam(team) # True/False White/Black
        self.setValue(100)

    def listMoves(self, board):
        validMoves = []
        if self.getPinned():
            return validMoves
        x, y = board.getCoordRules()
        xPos = None
        for index, value in enumerate(x):
            if value == self.getPos()[0]:
                xPos = index
                break
        threatenedSquares = self.getBoardThreatens(board)
        # print('Detected Threats: ', threatenedSquares)
        if (int(self.getPos()[1]) < 8):
            # print('Noth')
            if (self.getPos()[0]+str(int(self.getPos()[1])+1) not in threatenedSquares):
                if board.getPositionToken(self.getPos()[0]+str(int(self.getPos()[1])+1)) == None:
                    validMoves.append(self.getPos()[0]+str(int(self.getPos()[1])+1))
                elif board.getPositionToken(self.getPos()[0]+str(int(self.getPos()[1])+1)).getTeam() != self.getTeam():
                    validMoves.append(self.getPos()[0]+str(int(self.getPos()[1])+1))
        if (int(self.getPos()[1]) > 1):
            # print('South')
            if (self.getPos()[0]+str(int(self.getPos()[1])-1) not in threatenedSquares):
                if board.getPositionToken(self.getPos()[0]+str(int(self.getPos()[1])-1)) == None:
                    validMoves.append(self.getPos()[0]+str(int(self.getPos()[1])-1))
                elif board.getPositionToken(self.getPos()[0]+str(int(self.getPos()[1])-1)).getTeam() != self.getTeam():
                    validMoves.append(self.getPos()[0]+str(int(self.getPos()[1])-1))
        if (xPos > 0):
            # print('West')
            if (x[xPos-1]+self.getPos()[1] not in threatenedSquares):
                if board.getPositionToken(x[xPos-1]+self.getPos()[1]) == None:
                    validMoves.append(x[xPos-1]+self.getPos()[1])
                elif board.getPositionToken(x[xPos-1]+self.getPos()[1]).getTeam() != self.getTeam():
                    validMoves.append(x[xPos-1]+self.getPos()[1])
        if (xPos < 7):
            # print('East')
            if (x[xPos+1]+self.getPos()[1] not in threatenedSquares):
                if board.getPositionToken(x[xPos+1]+self.getPos()[1]) == None:
                    validMoves.append(x[xPos+1]+self.getPos()[1])
                elif board.getPositionToken(x[xPos+1]+self.getPos()[1]).getTeam() != self.getTeam():
                    validMoves.append(x[xPos+1]+self.getPos()[1])
        if (int(self.getPos()[1]) < 8 and xPos > 0):
            # print('NorthWest')
            if (x[xPos-1]+str(int(self.getPos()[1])+1) not in threatenedSquares):
                if board.getPositionToken(x[xPos-1]+str(int(self.getPos()[1])+1)) == None:
                    validMoves.append(x[xPos-1]+str(int(self.getPos()[1])+1))
                elif board.getPositionToken(x[xPos-1]+str(int(self.getPos()[1])+1)).getTeam() != self.getTeam():
                    validMoves.append(x[xPos-1]+str(int(self.getPos()[1])+1))
        if (int(self.getPos()[1]) < 8 and xPos < 7):
            # print('NorthEast')
            if (str(x[xPos+1])+str(int(self.getPos()[1])+1) not in threatenedSquares):
                if board.getPositionToken(x[xPos+1]+str(int(self.getPos()[1])+1)) == None:
                    validMoves.append(x[xPos+1]+str(int(self.getPos()[1])+1))
                elif board.getPositionToken(x[xPos+1]+str(int(self.getPos()[1])+1)).getTeam() != self.getTeam():
                    validMoves.append(x[xPos+1]+str(int(self.getPos()[1])+1))
        if (int(self.getPos()[1]) > 1 and xPos > 0):
            # print('SouthWest')
            if (x[xPos-1]+str(int(self.getPos()[1])-1) not in threatenedSquares):
                if board.getPositionToken(x[xPos-1]+str(int(self.getPos()[1])-1)) == None:
                    validMoves.append(x[xPos-1]+str(int(self.getPos()[1])-1))
                elif board.getPositionToken(x[xPos-1]+str(int(self.getPos()[1])-1)).getTeam() != self.getTeam():
                    validMoves.append(x[xPos-1]+str(int(self.getPos()[1])-1))
        if (int(self.getPos()[1]) > 1 and xPos < 7):
            # print('SouthEast')
            if (x[xPos+1]+str(int(self.getPos()[1])-1) not in threatenedSquares):
                if board.getPositionToken(x[xPos+1]+str(int(self.getPos()[1])-1)) == None:
                    validMoves.append(x[xPos+1]+str(int(self.getPos()[1])-1))
                elif board.getPositionToken(x[xPos+1]+str(int(self.getPos()[1])-1)).getTeam() != self.getTeam():
                    validMoves.append(x[xPos+1]+str(int(self.getPos()[1])-1))
        return validMoves

    def threatening(self, board):
        threat = []
        if self.getPinned():
            return threat
        x, _ = board.getCoordRules()
        xPos = None
        for index, value in enumerate(x):
            if value == self.getPos()[0]:
                xPos = index
        #threatenedSquares = self.getBoardThreatens(board)
        if (int(self.getPos()[1]) < 8):
            # print('Noth')
            # if (self.getPos()[0]+str(int(self.getPos()[1])+1) not in threatenedSquares):
            if board.getPositionToken(self.getPos()[0]+str(int(self.getPos()[1])+1)) == None:
                threat.append(self.getPos()[0]+str(int(self.getPos()[1])+1))
            elif board.getPositionToken(self.getPos()[0]+str(int(self.getPos()[1])+1)).getTeam() != self.getTeam():
                threat.append(self.getPos()[0]+str(int(self.getPos()[1])+1))
            elif board.getPositionToken(self.getPos()[0]+str(int(self.getPos()[1])+1)).getTeam() == self.getTeam():
                threat.append(self.getPos()[0]+str(int(self.getPos()[1])+1))
        if (int(self.getPos()[1]) > 1):
            # print('South')
            # if (self.getPos()[0]+str(int(self.getPos()[1])-1) not in threatenedSquares):
            if board.getPositionToken(self.getPos()[0]+str(int(self.getPos()[1])-1)) == None:
                threat.append(self.getPos()[0]+str(int(self.getPos()[1])-1))
            elif board.getPositionToken(self.getPos()[0]+str(int(self.getPos()[1])-1)).getTeam() != self.getTeam():
                threat.append(self.getPos()[0]+str(int(self.getPos()[1])-1))
            elif board.getPositionToken(self.getPos()[0]+str(int(self.getPos()[1])-1)).getTeam() == self.getTeam():
                threat.append(self.getPos()[0]+str(int(self.getPos()[1])-1))
        if (xPos > 0):
            # print('West')
            # if (x[xPos-1]+self.getPos()[1] not in threatenedSquares):
            if board.getPositionToken(x[xPos-1]+self.getPos()[1]) == None:
                threat.append(x[xPos-1]+self.getPos()[1])
            elif board.getPositionToken(x[xPos-1]+self.getPos()[1]).getTeam() != self.getTeam():
                threat.append(x[xPos-1]+self.getPos()[1])
            elif board.getPositionToken(x[xPos-1]+self.getPos()[1]).getTeam() == self.getTeam():
                threat.append(x[xPos-1]+self.getPos()[1])
        if (xPos < 7):
            # print('East')
            # if (x[xPos+1]+self.getPos()[1] not in threatenedSquares):
            if board.getPositionToken(x[xPos+1]+self.getPos()[1]) == None:
                threat.append(x[xPos+1]+self.getPos()[1])
            elif board.getPositionToken(x[xPos+1]+self.getPos()[1]).getTeam() != self.getTeam():
                threat.append(x[xPos+1]+self.getPos()[1])
            elif board.getPositionToken(x[xPos+1]+self.getPos()[1]).getTeam() == self.getTeam():
                threat.append(x[xPos+1]+self.getPos()[1])
        if (int(self.getPos()[1]) < 8 and xPos > 0):
            # print('NorthWest')
            # if (x[xPos-1]+str(int(self.getPos()[1])+1) not in threatenedSquares):
            if board.getPositionToken(x[xPos-1]+str(int(self.getPos()[1])+1)) == None:
                threat.append(x[xPos-1]+str(int(self.getPos()[1])+1))
            elif board.getPositionToken(x[xPos-1]+str(int(self.getPos()[1])+1)).getTeam() != self.getTeam():
                threat.append(x[xPos-1]+str(int(self.getPos()[1])+1))
            elif board.getPositionToken(x[xPos-1]+str(int(self.getPos()[1])+1)).getTeam() == self.getTeam():
                threat.append(x[xPos-1]+str(int(self.getPos()[1])+1))
        if (int(self.getPos()[1]) < 8 and xPos < 7):
            # print('NorthEast')
            # if (str(x[xPos+1])+str(int(self.getPos()[1])+1) not in threatenedSquares):
            if board.getPositionToken(x[xPos+1]+str(int(self.getPos()[1])+1)) == None:
                threat.append(x[xPos+1]+str(int(self.getPos()[1])+1))
            elif board.getPositionToken(x[xPos+1]+str(int(self.getPos()[1])+1)).getTeam() != self.getTeam():
                threat.append(x[xPos+1]+str(int(self.getPos()[1])+1))
            elif board.getPositionToken(x[xPos+1]+str(int(self.getPos()[1])+1)).getTeam() == self.getTeam():
                threat.append(x[xPos+1]+str(int(self.getPos()[1])+1))
        if (int(self.getPos()[1]) > 1 and xPos > 0):
            # print('SouthWest')
            # if (x[xPos-1]+str(int(self.getPos()[1])-1) not in threatenedSquares):
            if board.getPositionToken(x[xPos-1]+str(int(self.getPos()[1])-1)) == None:
                threat.append(x[xPos-1]+str(int(self.getPos()[1])-1))
            elif board.getPositionToken(x[xPos-1]+str(int(self.getPos()[1])-1)).getTeam() != self.getTeam():
                threat.append(x[xPos-1]+str(int(self.getPos()[1])-1))
            elif board.getPositionToken(x[xPos-1]+str(int(self.getPos()[1])-1)).getTeam() == self.getTeam():
                threat.append(x[xPos-1]+str(int(self.getPos()[1])-1))
        if (int(self.getPos()[1]) > 1 and xPos < 7):
            # print('SouthEast')
            # if (x[xPos+1]+str(int(self.getPos()[1])-1) not in threatenedSquares):
            if board.getPositionToken(x[xPos+1]+str(int(self.getPos()[1])-1)) == None:
                threat.append(x[xPos+1]+str(int(self.getPos()[1])-1))
            elif board.getPositionToken(x[xPos+1]+str(int(self.getPos()[1])-1)).getTeam() != self.getTeam():
                threat.append(x[xPos+1]+str(int(self.getPos()[1])-1))
            elif board.getPositionToken(x[xPos+1]+str(int(self.getPos()[1])-1)).getTeam() == self.getTeam():
                threat.append(x[xPos+1]+str(int(self.getPos()[1])-1))
        return threat

    def getBoardThreatens(self, board):
        threatenedSquares = []
        for index, value in enumerate(board.getBoard()):
            if board.getTokenThreats(value) != None:
                if board.getPositionToken(value).getTeam() != self.getTeam():
                    if board.getPositionToken(value).getName() != 'King':
                        for i in board.getTokenThreats(value):
                            if i not in threatenedSquares:
                                threatenedSquares.append(i)
        return threatenedSquares

    def check(self, board):
        threat = self.getBoardThreatens(board)
        for i in (threat):
            if i == self.getPos():
                return True
        return False

    def pinned(self, board, piecePosition:str):
        pass
# end King