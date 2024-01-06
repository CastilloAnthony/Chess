from pieces.piece import Piece

class Bishop(Piece):
    def __init__(self, team:bool):
        super().__init__()
        super().setName('Bishop')
        super().setTeam(team) # True/False White/Black
        super().setValue(3)

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
        if (xPos >= 0 and int(self.getPos()[1]) <= 8):
            # print('NorthWest')
            count = 1
            while (count <= 8) and (xPos - count >= 0 and int(self.getPos()[1]) + count <= 8):
                if board.getPositionToken(str(x[xPos-count])+str(int(self.getPos()[1])+count)) == None:
                    validMoves.append(str(x[xPos-count])+str(int(self.getPos()[1])+count))
                    count += 1
                elif board.getPositionToken(str(x[xPos-count])+str(int(self.getPos()[1])+count)).getTeam() != self.getTeam():
                    if board.getPositionToken(str(x[xPos-count])+str(int(self.getPos()[1])+count)).getName() != 'King':
                        validMoves.append(str(x[xPos-count])+str(int(self.getPos()[1])+count))
                    break
                else:
                    break
        if (xPos <= 7 and int(self.getPos()[1]) <= 8):
            # print('NorthEast')
            count = 1
            while (count <= 7) and (xPos + count <= 7 and int(self.getPos()[1]) + count <= 8):
                if board.getPositionToken(str(x[xPos+count])+str(int(self.getPos()[1])+count)) == None:
                    validMoves.append(str(x[xPos+count])+str(int(self.getPos()[1])+count))
                    count += 1
                elif board.getPositionToken(str(x[xPos+count])+str(int(self.getPos()[1])+count)).getTeam() != self.getTeam():
                    if board.getPositionToken(str(x[xPos+count])+str(int(self.getPos()[1])+count)).getName() != 'King':
                        validMoves.append(str(x[xPos+count])+str(int(self.getPos()[1])+count))
                    break
                else:
                    break
        if (xPos >= 0 and int(self.getPos()[1]) >= 1):
            # print('SouthWest')
            count = 1
            while (count <= 7) and (xPos - count >= 0 and int(self.getPos()[1]) - count >= 1):
                if board.getPositionToken(str(x[xPos-count])+str(int(self.getPos()[1])-count)) == None:
                    validMoves.append(str(x[xPos-count])+str(int(self.getPos()[1])-count))
                    count += 1
                elif board.getPositionToken(str(x[xPos-count])+str(int(self.getPos()[1])-count)).getTeam() != self.getTeam():
                    if board.getPositionToken(str(x[xPos-count])+str(int(self.getPos()[1])-count)).getName() != 'King':
                        validMoves.append(str(x[xPos-count])+str(int(self.getPos()[1])-count))
                    break
                else:
                    break
        if (xPos <= 7 and int(self.getPos()[1]) >= 1):
            # print('SouthEast')
            count = 1
            while (count <= 7) and (xPos + count <= 7 and int(self.getPos()[1]) - count >= 1):
                if board.getPositionToken(str(x[xPos+count])+str(int(self.getPos()[1])-count)) == None:
                    validMoves.append(str(x[xPos+count])+str(int(self.getPos()[1])-count))
                    count += 1
                elif board.getPositionToken(str(x[xPos+count])+str(int(self.getPos()[1])-count)).getTeam() != self.getTeam():
                    if board.getPositionToken(str(x[xPos+count])+str(int(self.getPos()[1])-count)).getName() != 'King':
                        validMoves.append(str(x[xPos+count])+str(int(self.getPos()[1])-count))
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
        if (xPos >= 0 and int(self.getPos()[1]) <= 8):
            # print('NorthWest')
            count = 1
            while (count <= 8) and (xPos - count >= 0 and int(self.getPos()[1]) + count <= 8):
                if board.getPositionToken(str(x[xPos-count])+str(int(self.getPos()[1])+count)) == None:
                    threat.append(str(x[xPos-count])+str(int(self.getPos()[1])+count))
                    count += 1
                elif board.getPositionToken(str(x[xPos-count])+str(int(self.getPos()[1])+count)).getTeam() != self.getTeam():
                    threat.append(str(x[xPos-count])+str(int(self.getPos()[1])+count))
                    break
                elif board.getPositionToken(str(x[xPos-count])+str(int(self.getPos()[1])+count)).getTeam() == self.getTeam():
                    threat.append(str(x[xPos-count])+str(int(self.getPos()[1])+count))
                    break
                else:
                    break
        if (xPos <= 7 and int(self.getPos()[1]) <= 8):
            # print('NorthEast')
            count = 1
            while (count <= 7) and (xPos + count <= 7 and int(self.getPos()[1]) + count <= 8):
                if board.getPositionToken(str(x[xPos+count])+str(int(self.getPos()[1])+count)) == None:
                    threat.append(str(x[xPos+count])+str(int(self.getPos()[1])+count))
                    count += 1
                elif board.getPositionToken(str(x[xPos+count])+str(int(self.getPos()[1])+count)).getTeam() != self.getTeam():
                    threat.append(str(x[xPos+count])+str(int(self.getPos()[1])+count))
                    break
                elif board.getPositionToken(str(x[xPos+count])+str(int(self.getPos()[1])+count)).getTeam() == self.getTeam():
                    threat.append(str(x[xPos+count])+str(int(self.getPos()[1])+count))
                    break
                else:
                    break
        if (xPos >= 0 and int(self.getPos()[1]) >= 1):
            # print('SouthWest')
            count = 1
            while (count <= 7) and (xPos - count >= 0 and int(self.getPos()[1]) - count >= 1):
                if board.getPositionToken(str(x[xPos-count])+str(int(self.getPos()[1])-count)) == None:
                    threat.append(str(x[xPos-count])+str(int(self.getPos()[1])-count))
                    count += 1
                elif board.getPositionToken(str(x[xPos-count])+str(int(self.getPos()[1])-count)).getTeam() != self.getTeam():
                    threat.append(str(x[xPos-count])+str(int(self.getPos()[1])-count))
                    break
                elif board.getPositionToken(str(x[xPos-count])+str(int(self.getPos()[1])-count)).getTeam() == self.getTeam():
                    threat.append(str(x[xPos-count])+str(int(self.getPos()[1])-count))
                    break
                else:
                    break
        if (xPos <= 7 and int(self.getPos()[1]) >= 1):
            # print('SouthEast')
            count = 1
            while (count <= 7) and (xPos + count <= 7 and int(self.getPos()[1]) - count >= 1):
                if board.getPositionToken(str(x[xPos+count])+str(int(self.getPos()[1])-count)) == None:
                    threat.append(str(x[xPos+count])+str(int(self.getPos()[1])-count))
                    count += 1
                elif board.getPositionToken(str(x[xPos+count])+str(int(self.getPos()[1])-count)).getTeam() != self.getTeam():
                    threat.append(str(x[xPos+count])+str(int(self.getPos()[1])-count))
                    break
                elif board.getPositionToken(str(x[xPos+count])+str(int(self.getPos()[1])-count)).getTeam() == self.getTeam():
                    threat.append(str(x[xPos+count])+str(int(self.getPos()[1])-count))
                    break
                else:
                    break
        return threat
# end Bishop