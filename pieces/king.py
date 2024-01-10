from pieces.piece import Piece
from pieces.queen import Queen

class King(Queen, Piece):
    def __init__(self, team:bool):
        Piece.__init__(self)
        self.setName('King')
        self.setTeam(team) # True/False White/Black
        self.setValue(100)
        self.__threatenedSquares = []
        self.__castling = False

    def __del__(self):
        del self.__threatenedSquares
        super().__del__()

    def getCastling(self):
        return self.__castling
    
    def flipCastling(self):
        self.__castling = False

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
        # threatenedSquares = board.getBoardThreats(not self.getTeam())
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
        if self.getInitial(): # Castling
                for i in reversed(range(0, xPos)): # Left Side
                    # print('Left', x[i]+self.getPos()[1],board.getPositionToken(x[i]+self.getPos()[1]))
                    if board.getPositionToken(x[i]+self.getPos()[1]) == None:
                        continue
                    elif board.getPositionToken(x[i]+self.getPos()[1]).getName() != 'Rook':
                        break
                    if board.getPositionToken(x[i]+self.getPos()[1]) != None:
                        if board.getPositionToken(x[i]+self.getPos()[1]).getName() == 'Rook':
                            if board.getPositionToken(x[i]+self.getPos()[1]).getInitial():
                                validMoves.append('C'+self.getPos()[1])
                                self.__castling = True
                for i in range(xPos+1, 8): # Right Side
                    # print('Right', x[i]+self.getPos()[1], board.getPositionToken(x[i]+self.getPos()[1]))
                    if board.getPositionToken(x[i]+self.getPos()[1]) == None:
                        continue
                    elif board.getPositionToken(x[i]+self.getPos()[1]).getName() != 'Rook':
                        break
                    if board.getPositionToken(x[i]+self.getPos()[1]) != None:
                        if board.getPositionToken(x[i]+self.getPos()[1]).getName() == 'Rook':
                            if board.getPositionToken(x[i]+self.getPos()[1]).getInitial():
                                validMoves.append('G'+self.getPos()[1])
                                self.__castling = True
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
        return self.__threatenedSquares
    
    def calculateThreats(self, board):
        selfThreats = self.threatening(board)
        threatenedSquares = []
        for index, value in enumerate(board.getBoard()):
            if board.getTokenThreats(value) != None:
                if board.getPositionToken(value).getTeam() != self.getTeam():
                    for i in board.getTokenThreats(value):
                        if i in selfThreats:
                            if i not in threatenedSquares:
                                threatenedSquares.append(i)
                        if len(threatenedSquares) == len(selfThreats):
                            break
        self.__threatenedSquares = threatenedSquares

    def check(self, board):
        threat = self.getBoardThreatens(board)
        for i in (threat):
            if i == self.getPos():
                return True
        return False

    def pinned(self, board, piecePosition:str):
        pass
# end King