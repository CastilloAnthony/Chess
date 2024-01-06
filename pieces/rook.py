from pieces.piece import Piece

class Rook(Piece):
    def __init__(self, team:bool):
        super().__init__()
        super().setName('Rook')
        super().setTeam(team) # True/False White/Black
        super().setValue(5)

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
        if int(self.getPos()[1]) < 8:
            # print('North')
            for i in range(int(self.getPos()[1])+1, 9):
                if board.getPositionToken(self.getPos()[0]+str(i)) == None:
                    validMoves.append(self.getPos()[0]+str(i))
                elif board.getPositionToken(self.getPos()[0]+str(i)).getTeam() != self.getTeam():
                    validMoves.append(self.getPos()[0]+str(i))
                    break
                else:
                    break
        if int(self.getPos()[1]) > 1:
            # print('South')
            for i in reversed(range(1, int(self.getPos()[1]))):
                if board.getPositionToken(self.getPos()[0]+str(i)) == None:
                    validMoves.append(self.getPos()[0]+str(i))
                elif board.getPositionToken(self.getPos()[0]+str(i)).getTeam() != self.getTeam():
                    validMoves.append(self.getPos()[0]+str(i))
                    break
                else:
                    break
        if xPos > 0:
            # print('West')
            for i in reversed(range(0, xPos)):
                if board.getPositionToken(x[i]+self.getPos()[1]) == None:
                    validMoves.append(x[i]+self.getPos()[1])
                    pass
                elif board.getPositionToken(x[i]+self.getPos()[1]).getTeam() != self.getTeam():
                    validMoves.append(x[i]+self.getPos()[1])
                    break
                else:
                    break
        if xPos < 7:
            # print('East')
            for i in range(xPos+1, 8):
                if board.getPositionToken(x[i]+self.getPos()[1]) == None:
                    validMoves.append(x[i]+self.getPos()[1])
                elif board.getPositionToken(x[i]+self.getPos()[1]).getTeam() != self.getTeam():
                    validMoves.append(x[i]+self.getPos()[1])
                    break
                else:
                    break
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
        if int(self.getPos()[1]) < 8:
            # print('North')
            for i in range(int(self.getPos()[1])+1, 9):
                if board.getPositionToken(self.getPos()[0]+str(i)) == None:
                    threat.append(self.getPos()[0]+str(i))
                elif board.getPositionToken(self.getPos()[0]+str(i)).getTeam() != self.getTeam():
                    threat.append(self.getPos()[0]+str(i))
                    break
                elif board.getPositionToken(self.getPos()[0]+str(i)).getTeam() == self.getTeam():
                    threat.append(self.getPos()[0]+str(i))
                    break
                else:
                    break
        if int(self.getPos()[1]) > 1:
            # print('South')
            for i in reversed(range(1, int(self.getPos()[1]))):
                if board.getPositionToken(self.getPos()[0]+str(i)) == None:
                    threat.append(self.getPos()[0]+str(i))
                elif board.getPositionToken(self.getPos()[0]+str(i)).getTeam() != self.getTeam():
                    threat.append(self.getPos()[0]+str(i))
                    break
                elif board.getPositionToken(self.getPos()[0]+str(i)).getTeam() == self.getTeam():
                    threat.append(self.getPos()[0]+str(i))
                    break
                else:
                    break
        if xPos > 0:
            # print('West')
            for i in reversed(range(0, xPos)):
                if board.getPositionToken(x[i]+self.getPos()[1]) == None:
                    threat.append(x[i]+self.getPos()[1])
                    pass
                elif board.getPositionToken(x[i]+self.getPos()[1]).getTeam() != self.getTeam():
                    threat.append(x[i]+self.getPos()[1])
                    break
                elif board.getPositionToken(x[i]+self.getPos()[1]).getTeam() == self.getTeam():
                    threat.append(x[i]+self.getPos()[1])
                    break
                else:
                    break
        if xPos < 7:
            # print('East')
            for i in range(xPos+1, 8):
                if board.getPositionToken(x[i]+self.getPos()[1]) == None:
                    threat.append(x[i]+self.getPos()[1])
                elif board.getPositionToken(x[i]+self.getPos()[1]).getTeam() != self.getTeam():
                    threat.append(x[i]+self.getPos()[1])
                    break
                elif board.getPositionToken(x[i]+self.getPos()[1]).getTeam() == self.getTeam():
                    threat.append(x[i]+self.getPos()[1])
                    break
                else:
                    break
        return threat
        
# end Rook