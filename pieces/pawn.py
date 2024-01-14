from pieces.piece import Piece

class Pawn(Piece):
    def __init__(self, team:bool):
        super().__init__()
        super().setName('Pawn')
        super().setTeam(team) # True/False White/Black
        super().setValue(1)
        self.__enPassant = False
        self.__promotion = False

    def __del__(self):
        del self.__enPassant
        super().__del__()

    def getEnPassant(self):
        return self.__enPassant
    
    def flipEnPassant(self):
        self.__enPassant = False

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
        if (self.getTeam() and self.getPos()[1] == '8') or (not self.getTeam() and self.getPos()[1] == '1'):
            return validMoves
        else:
            
            if self.getTeam(): # White Move
                if board.getPositionToken(self.getPos()[0]+str(int(self.getPos()[1])+1)) == None:
                    validMoves.append(self.getPos()[0]+str(int(self.getPos()[1])+1))
            else: # Black Move
                if board.getPositionToken(self.getPos()[0]+str(int(self.getPos()[1])-1)) == None:
                    validMoves.append(self.getPos()[0]+str(int(self.getPos()[1])-1))
            if len(validMoves) > 0:
                if self.getInitial():
                    if self.getTeam(): # White Move
                        if board.getPositionToken(self.getPos()[0]+str(int(self.getPos()[1])+1+self.getInitial())) == None:
                            validMoves.append(self.getPos()[0]+str(int(self.getPos()[1])+1+self.getInitial()))
                    else: # Black Move
                        if board.getPositionToken(self.getPos()[0]+str(int(self.getPos()[1])-1-self.getInitial())) == None:
                            validMoves.append(self.getPos()[0]+str(int(self.getPos()[1])-1-self.getInitial()))
            for index, value in enumerate(x): # Checking for attack moves
                if value == self.getPos()[0]:
                    if value != 'A':
                        if self.getTeam(): # White Move
                            if  board.getPositionToken(x[index-1]+str(int(self.getPos()[1])+1)) != None:
                                if board.getPositionToken(x[index-1]+str(int(self.getPos()[1])+1)).getTeam() != self.getTeam():
                                    if board.getPositionToken(x[index-1]+str(int(self.getPos()[1])+1)).getName() != 'King':
                                        validMoves.append(x[index-1]+str(int(self.getPos()[1])+1))
                        else: # Black Move
                            if  board.getPositionToken(x[index-1]+str(int(self.getPos()[1])-1)) != None:
                                if board.getPositionToken(x[index-1]+str(int(self.getPos()[1])-1)).getTeam() != self.getTeam():
                                    if board.getPositionToken(x[index-1]+str(int(self.getPos()[1])-1)).getName() != 'King':
                                        validMoves.append(x[index-1]+str(int(self.getPos()[1])-1))
                    if value != 'H':
                        if self.getTeam(): # White Move
                            if board.getPositionToken(x[index+1]+str(int(self.getPos()[1])+1)) != None:
                                if board.getPositionToken(x[index+1]+str(int(self.getPos()[1])+1)).getTeam() != self.getTeam():
                                    if board.getPositionToken(x[index+1]+str(int(self.getPos()[1])+1)).getName() != 'King':
                                        validMoves.append(x[index+1]+str(int(self.getPos()[1])+1))
                        else: # Black Move
                            if board.getPositionToken(x[index+1]+str(int(self.getPos()[1])-1)) != None:
                                if board.getPositionToken(x[index+1]+str(int(self.getPos()[1])-1)).getTeam() != self.getTeam():
                                    if board.getPositionToken(x[index+1]+str(int(self.getPos()[1])-1)).getName() != 'King':
                                        validMoves.append(x[index+1]+str(int(self.getPos()[1])-1))
                    break
            # Adding  En Passant
            lastBoard = board.getHistory(-2)
            if self.getTeam() and self.getPos()[1] == '5': # White Move
                if xPos > 0:
                    if board.getPositionToken(x[xPos-1]+self.getPos()[1]) != None:
                        if board.getPositionToken(x[xPos-1]+self.getPos()[1]).getTeam() != self.getTeam():
                            if board.getPositionToken(x[xPos-1]+self.getPos()[1]).getName() == 'Pawn':
                                for index, value in enumerate(lastBoard):
                                    # print(index, value)
                                    if lastBoard[value] != 'Empty\t\t':
                                        # print(lastBoard[value].getID(), board.getPositionToken(x[xPos-1]+self.getPos()[1]).getID())
                                        if lastBoard[value].getID() == board.getPositionToken(x[xPos-1]+self.getPos()[1]).getID():
                                            # print(lastBoard[value].getPos()[0]+str(int(lastBoard[value].getPos()[1])))
                                            if lastBoard[value].getPos()[0] == x[xPos-1] and int(lastBoard[value].getPos()[1]) == int(self.getPos()[1])+2:
                                                if lastBoard[value].getInitial():
                                                    # print(x[xPos-1]+str(int(self.gtePos()[1])+1))
                                                    validMoves.append(x[xPos-1]+str(int(self.getPos()[1])+1))
                                                    self.__enPassant = True
                if xPos < 7:
                    if board.getPositionToken(x[xPos+1]+self.getPos()[1]) != None:
                        if board.getPositionToken(x[xPos+1]+self.getPos()[1]).getTeam() != self.getTeam():
                            if board.getPositionToken(x[xPos+1]+self.getPos()[1]).getName() == 'Pawn':
                                for index, value in enumerate(lastBoard):
                                    # print(index, value)
                                    if lastBoard[value] != 'Empty\t\t':
                                        # print(lastBoard[value].getID(), board.getPositionToken(x[xPos+1]+self.getPos()[1]).getID())
                                        if lastBoard[value].getID() == board.getPositionToken(x[xPos+1]+self.getPos()[1]).getID():
                                            # print(lastBoard[value].getPos())
                                            if lastBoard[value].getPos()[0] == x[xPos+1] and int(lastBoard[value].getPos()[1]) == int(self.getPos()[1])+2:
                                                # print(lastBoard[value].getInitial())
                                                if lastBoard[value].getInitial():
                                                    # print(x[xPos+1]+str(int(self.getPos()[1])+1))
                                                    validMoves.append(x[xPos+1]+str(int(self.getPos()[1])+1))
                                                    self.__enPassant = True
            if not self.getTeam() and int(self.getPos ()[1]) > 1: # Black Move
                if xPos > 0:
                    if board.getPositionToken(x[xPos-1]+self.getPos()[1]) != None:
                        if board.getPositionToken(x[xPos-1]+self.getPos()[1]).getTeam() != self.getTeam():
                            if board.getPositionToken(x[xPos-1]+self.getPos()[1]).getName() == 'Pawn':
                                for index, value in enumerate(lastBoard):
                                    # print(index, value)
                                    if lastBoard[value] != 'Empty\t\t':
                                        if lastBoard[value].getID() == board.getPositionToken(x[xPos-1]+self.getPos()[1]).getID():
                                            if lastBoard[value].getPos()[0] == x[xPos-1] and int(lastBoard[value].getPos()[1]) == int(self.getPos()[1])-2:
                                                if lastBoard[value].getInitial():
                                                    # print(x[xPos-1]+str(int(self.getPos()[1])-1))
                                                    validMoves.append(x[xPos-1]+str(int(self.getPos()[1])-1))
                                                    self.__enPassant = True
                if xPos < 7:
                    if board.getPositionToken(x[xPos+1]+self.getPos()[1]) != None:
                        if board.getPositionToken(x[xPos+1]+self.getPos()[1]).getTeam() != self.getTeam():
                            if board.getPositionToken(x[xPos+1]+self.getPos()[1]).getName() == 'Pawn':
                                for index, value in enumerate(lastBoard):
                                    # print(index, value)
                                    if lastBoard[value] != 'Empty\t\t':
                                        if lastBoard[value].getID() == board.getPositionToken(x[xPos+1]+self.getPos()[1]).getID():
                                            if lastBoard[value].getPos()[0] == x[xPos+1] and int(lastBoard[value].getPos()[1]) == int(self.getPos()[1])-2:
                                                if lastBoard[value].getInitial():
                                                    # print(x[xPos+1]+str(int(self.getPos()[1])-1))
                                                    validMoves.append(x[xPos+1]+str(int(self.getPos()[1])-1))
                                                    self.__enPassant = True
        return validMoves     
        
    def threatening(self, board):
        threat = []
        x, _ = board.getCoordRules()
        xPos = None
        for index, value in enumerate(x):
            if value == self.getPos()[0]:
                xPos = index
        if xPos > 0:
            if self.getTeam():
                if int(self.getPos()[1]) < 8:
                    threat.append(x[xPos-1]+str(int(self.getPos()[1])+1))
            else:
                if int(self.getPos()[1]) > 1:
                    threat.append(x[xPos-1]+str(int(self.getPos()[1])-1))
        if xPos < 7:
            if self.getTeam():
                if int(self.getPos()[1]) < 8:
                    threat.append(x[xPos+1]+str(int(self.getPos()[1])+1))
            else:
                if int(self.getPos()[1]) > 1:
                    threat.append(x[xPos+1]+str(int(self.getPos()[1])-1))
        return threat
# end Pawn