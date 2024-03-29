from uuid import uuid4
import pygame
from core.square import Square
from core.game import Game
from os import path
from threading import Thread
from copy import deepcopy

class Interface():
    def __init__(self):
        self.__id = uuid4()
        self.__x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.__y = ['1', '2', '3', '4', '5', '6', '7', '8']
        self.__squares, self.__images = {}, {}
        self.__guiScale = 1.0
        self.__res_factor = 82*self.__guiScale
        self.__res_x, self.__res_y = 10*self.__res_factor, 10*self.__res_factor
        self.setupBoard()

    def __del__(self):
        del self.__id, self.__x, self.__y, self.__squares, self.__images, self.__guiScale, self.__res_factor, self.__res_x, self.__res_y

    def getID(self):
        return self.__id
    
    def setupBoard(self):
        for i in range(0, 8):
                # print('i:', i)
                for j in range(0, 8):
                    # print('j: ', j)
                    if i % 2 == 0:
                        if j % 2 == 0:
                            self.__squares[self.__x[i]+str(8-j)] = Square("white", (self.__res_x-self.__res_factor*2)/8*(i+1), (self.__res_y-self.__res_factor*2)/8*(j+1), (self.__res_x-self.__res_factor*2)/8, (self.__res_y-self.__res_factor*2)/8)
                        else:
                            self.__squares[self.__x[i]+str(8-j)] = Square("black", (self.__res_x-self.__res_factor*2)/8*(i+1), (self.__res_y-self.__res_factor*2)/8*(j+1), (self.__res_x-self.__res_factor*2)/8, (self.__res_y-self.__res_factor*2)/8)
                    else:
                        if j % 2 == 0:
                            self.__squares[self.__x[i]+str(8-j)] = Square("black", (self.__res_x-self.__res_factor*2)/8*(i+1), (self.__res_y-self.__res_factor*2)/8*(j+1), (self.__res_x-self.__res_factor*2)/8, (self.__res_y-self.__res_factor*2)/8)
                        else:
                            self.__squares[self.__x[i]+str(8-j)] = Square("white", (self.__res_x-self.__res_factor*2)/8*(i+1), (self.__res_y-self.__res_factor*2)/8*(j+1), (self.__res_x-self.__res_factor*2)/8, (self.__res_y-self.__res_factor*2)/8)
        
    def loadPieces(self, board):
        for i in board:
            if board[i] != 'Empty\t\t':
                if board[i].getTeam():
                    self.__squares[i].setPiece('w_'+board[i].getName().lower())
                else:
                    self.__squares[i].setPiece('b_'+board[i].getName().lower())
            else:
                self.__squares[i].setPiece(None)
        if len(self.__images) == 0:
            self.loadImages()

    def updatePieces(self, startPos, endPos):
        self.__squares[endPos].setPiece(self.__squares[startPos].getPiece())
        self.__squares[startPos].setPiece(None)

    def loadImages(self):
        for i in self.__squares:
            if self.__squares[i].getPiece() != None:
                self.__images[self.__squares[i].getPiece()] = pygame.transform.scale(pygame.image.load(path.join('assets', 'pieces', self.__squares[i].getPiece()+'.png')), (self.__squares[i].getStats()[2], self.__squares[i].getStats()[3]))
        self.__images['dot_b'] = pygame.transform.scale(pygame.image.load(path.join('assets', 'dots', 'blue_dot.png')), (self.__squares['A1'].getStats()[2], self.__squares['A1'].getStats()[3]))
        self.__images['dot_b_half'] = pygame.transform.scale(pygame.image.load(path.join('assets', 'dots', 'blue_dot_50%.png')), (self.__squares['A1'].getStats()[2], self.__squares['A1'].getStats()[3]))
        self.__images['dot_g'] = pygame.transform.scale(pygame.image.load(path.join('assets', 'dots', 'green_dot.png')), (self.__squares['A1'].getStats()[2]/2, self.__squares['A1'].getStats()[3]/2))
        self.__images['dot_g_half'] = pygame.transform.scale(pygame.image.load(path.join('assets', 'dots', 'green_dot_50%.png')), (self.__squares['A1'].getStats()[2]/2, self.__squares['A1'].getStats()[3]/2))
        self.__images['dot_r'] = pygame.transform.scale(pygame.image.load(path.join('assets', 'dots', 'red_dot.png')), (self.__squares['A1'].getStats()[2], self.__squares['A1'].getStats()[3]))
        self.__images['dot_r_half'] = pygame.transform.scale(pygame.image.load(path.join('assets', 'dots', 'red_dot_50%.png')), (self.__squares['A1'].getStats()[2], self.__squares['A1'].getStats()[3]))
        print(self.__images)

    def start(self):
        pygame.init()
        pygame.display.set_caption('Chess') # Set the window title
        screen = pygame.display.set_mode((self.__res_x, self.__res_y))
        clock = pygame.time.Clock()
        running = True
        newGame = Game()
        newGame.newGame()
        currentPos = None
        debug = True
        threads = newGame.calculateMoves()
        threads['move'] = Thread()
        self.loadPieces(newGame.getBoard())
        kings = {'white':'E1', 'black':'E8'}
        while running:
            # Check events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if not (pos[0] < self.__res_factor or pos[1] < self.__res_factor or pos[0] > self.__res_factor*9 or pos[1] > self.__res_factor*9):
                        for i in self.__squares:
                            if self.__squares[i].getStats()[0] < pos[0] < self.__squares[i].getStats()[0]+self.__res_factor:
                                if self.__squares[i].getStats()[1] < pos[1] < self.__squares[i].getStats()[1]+self.__res_factor:
                                    if i == currentPos:
                                        currentPos = None
                                    elif currentPos == None:
                                        # Turn Order Checking
                                        if newGame.getTokenStatus(i) != None and newGame.getTokenStatus(i) != False:
                                            if newGame.getTokenStatus(i)['team'] == newGame.getTurn():
                                                currentPos = i
                                        # currentPos = i # Uncomment to remove restriction
                                    elif newGame.getTokenMoves(currentPos) != None and i in newGame.getTokenMoves(currentPos) and newGame.getTokenStatus(currentPos)['team'] == newGame.getTurn(): # Comment out team stuff to remove turn restrictions
                                        # if newGame.findChecks() == False:
                                        #     if newGame.checkFuture(currentPos, i):
                                        #         validMove = True
                                        if currentPos in threads.values():
                                            if threads[currentPos].is_alive():
                                                threads[currentPos].join()
                                            del threads[currentPos]
                                        # if newGame.checkFuture(currentPos, i):
                                        #     validMove = True
                                        # else:
                                        #     validMove = False
                                        # validMove = True
                                        # if validMove:
                                        threads['move'] = Thread(target=newGame.move, name='name', args=(currentPos, i,))
                                        threads['move'].start()
                                        if currentPos == kings['white']:
                                            kings['white'] = i
                                        elif currentPos == kings['black']:
                                            kings['black'] = i
                                        # self.updatePieces(currentPos, i)
                                        # currentPos = None
                                        # oneKing = False
                                        # newGame.endTurn()
                                        if threads['move'].is_alive():
                                            threads['move'].join()
                                        threads[kings['white']] = newGame.calculateKing(kings['white'])
                                        threads[kings['black']] = newGame.calculateKing(kings['black'])
                                        currentPos = None
                                        newGame.endTurn()
                                        # if threads['move'].is_alive():
                                        #     threads['move'].join()
                                        # for j in self.__squares:
                                        #     if self.__squares[j].getPiece() != None:
                                        #         if 'king' in self.__squares[j].getPiece():
                                        #             if threads['move'].is_alive():
                                        #                 threads['move'].join()
                                        #             threads[self.__squares[j].getPiece()] = newGame.calculateKing(j)
                                        #             if oneKing:
                                        #                 break
                                        #             else:
                                        #                 oneKing = True
                                        threads[kings['white']].join()
                                        threads[kings['black']].join()
                                        threads.update(newGame.calculateMoves())
                                            # print(newGame.checkForPromote())
                                        # if newGame.move(currentPos, i):
                                        #     threads['move'] = Thread(target=newGame.move, name='name', args=(currentPos, i,))
                                        #     # self.updatePieces(currentPos, i)
                                        #     currentPos = None
                                        #     oneKing = False
                                        #     newGame.endTurn()
                                        #     for j in self.__squares:
                                        #         if self.__squares[j].getPiece() != None:
                                        #             if 'king' in self.__squares[j].getPiece():
                                        #                 threads[self.__squares[j].getPiece()] = newGame.calculateKing(j)
                                        #                 if oneKing:
                                        #                     break
                                        #                 else:
                                        #                     oneKing = True
                                        # else:
                                        #     currentPos = None
                                    else:
                                        currentPos = None
                    else:
                        currentPos = None
            # Updating the screen
            if True: # For screen updates
                self.loadPieces(newGame.getBoard())
                screen.fill(pygame.Color(100, 100, 100, a=255))
                # Redraw Board
                for i in self.__squares:
                    pygame.draw.rect(screen, self.__squares[i].getColor(), pygame.Rect(self.__squares[i].getStats()))
                # Margin, Bottom
                for index, x in enumerate(self.__x):
                    text = pygame.font.SysFont("Times New Roman", round (18*self.__guiScale)).render(x, True, (0, 0, 0))
                    screen.blit(text, (self.__res_factor+self.__res_factor*int(index)+self.__res_factor/2-text.get_width()/2, self.__res_factor*9))#+text.get_height()*2))#self.__res_factor/10))
                # Margin, Left
                for y in self.__y:
                    text = pygame.font.SysFont("Times New Roman", round (18*self.__guiScale)).render(y, True, (0, 0, 0))
                    screen.blit(text, (self.__res_factor-text.get_width()*2, self.__res_factor*(9-int(y))+self.__res_factor/2-text.get_height()/2))
                # Drawing info onto the board, score, board id, fps, etc.
                score = pygame.font.SysFont("Times New Roman", round(32*self.__guiScale)).render("White: "+str(newGame.getScore()[True])+"   Black: "+str(newGame.getScore()[False]), True, (0, 0, 0))
                screen.blit(score, (self.__res_x/2-score.get_width()/2, self.__res_factor/2-score.get_height()/2))
                checked = newGame.findChecks()
                if checked != False:
                    if checked['team']:
                        team = 'White'
                    else:
                        team = 'Black'
                    check = pygame.font.SysFont("Times New Roman", round(32*self.__guiScale)).render(team+' Check', True, (0, 0, 0))
                    screen.blit(check, (self.__res_x/2-check.get_width()/2, self.__res_factor*9+self.__res_factor/2-check.get_height()/2))
                # if newGame.checkForPromote() != False:
                #     promote = pygame.font.SysFont("Times New Roman", round(32*self.__guiScale)).render('Pawn at '+newGame.checkForPromote()['position']+' is ready for Promotion', True, (0, 0, 0))
                #     screen.blit(promote, (self.__res_x/2-promote.get_width()/2, self.__res_factor*9+self.__res_factor/2-promote.get_height()/2))
                # print(checked)
                if debug:
                    fps = pygame.font.SysFont("Times New Roman", round(12*self.__guiScale)).render('fps: '+str(round(clock.get_fps())), True, (0, 0, 0))
                    screen.blit(fps, (0, 0))
                    id = pygame.font.SysFont("Times New Roman", round(12*self.__guiScale)).render('Board ID: '+str(newGame.getBoardID()), True, (0, 0, 0))
                    screen.blit(id, (0, fps.get_height()))
                # Draw Pieces and dots
                # if threads['move'].is_alive():
                #     threads['move'].join()
                if currentPos != None:
                    if currentPos in threads.values():
                        if threads[currentPos].is_alive():
                            threads[currentPos].join()
                        del threads[currentPos]
                    screen.blit(self.__images['dot_b_half'], (self.__squares[currentPos].getStats()[0], self.__squares[currentPos].getStats()[1]))
                    # screen.blit(self.__images[self.__squares[currentPos].getPiece()], (self.__squares[currentPos].getStats()[0], self.__squares[currentPos].getStats()[1]))
                    for j in newGame.getTokenMoves(currentPos):
                        # if not newGame.checkFuture(i, j):
                        #         continue
                        if newGame.getBoard()[j] != 'Empty\t\t':
                            if newGame.getTokenStatus(j)['team'] != newGame.getTokenStatus(currentPos)['team']:
                                screen.blit(self.__images['dot_r_half'], (self.__squares[j].getStats()[0], self.__squares[j].getStats()[1]))
                                # screen.blit(self.__images[self.__squares[j].getPiece()], (self.__squares[j].getStats()[0], self.__squares[j].getStats()[1]))
                            else:
                                screen.blit(self.__images['dot_b_half'], (self.__squares[j].getStats()[0], self.__squares[j].getStats()[1]))
                        else:
                            screen.blit(self.__images['dot_g_half'], (self.__squares[j].getStats()[0]+self.__res_factor/4, self.__squares[j].getStats()[1]+self.__res_factor/4))
                for i in self.__squares:
                    if self.__squares[i].getPiece() != None:
                        screen.blit(self.__images[self.__squares[i].getPiece()], (self.__squares[i].getStats()[0], self.__squares[i].getStats()[1]))
                        # if currentPos == i:
                        #     screen.blit(self.__images['dot_b_half'], (self.__squares[currentPos].getStats()[0], self.__squares[currentPos].getStats()[1]))
                        #     screen.blit(self.__images[self.__squares[i].getPiece()], (self.__squares[i].getStats()[0], self.__squares[i].getStats()[1]))
                            # if i in threads.values():
                            #     if threads[i].is_alive():
                            #         threads[i].join()
                            #     del threads[i]
                            # if 'king' in self.__squares[i].getPiece():
                            #     if self.__squares[i].getPiece() in threads:
                            #         if threads[self.__squares[i].getPiece()].is_alive():
                            #             threads[self.__squares[i].getPiece()].join()
                            #         del threads[self.__squares[i].getPiece()]
                            # validMove = True
                            # print(newGame.getTokenStatus(i))
                            # print(newGame.getTokenMoves(i))
                            # for j in newGame.getTokenMoves(i):
                            #     # if not newGame.checkFuture(i, j):
                            #     #         continue
                            #     if newGame.getBoard()[j] != 'Empty\t\t':
                            #         if newGame.getTokenStatus(j)['team'] != newGame.getTokenStatus(i)['team']:
                            #             screen.blit(self.__images['dot_r_half'], (self.__squares[j].getStats()[0], self.__squares[j].getStats()[1]))
                            #             screen.blit(self.__images[self.__squares[j].getPiece()], (self.__squares[j].getStats()[0], self.__squares[j].getStats()[1]))
                            #         else:
                            #             screen.blit(self.__images['dot_b_half'], (self.__squares[j].getStats()[0], self.__squares[j].getStats()[1]))
                            #     else:
                            #         screen.blit(self.__images['dot_g_half'], (self.__squares[j].getStats()[0]+self.__res_factor/4, self.__squares[j].getStats()[1]+self.__res_factor/4))
                        # else:
                        #     screen.blit(self.__images[self.__squares[i].getPiece()], (self.__squares[i].getStats()[0], self.__squares[i].getStats()[1]))
                # Update screen
                pygame.display.flip()
            # Limits FPS to 60
            clock.tick(60)
        pygame.quit()

def guiTest():
    newInterface = Interface()
    newInterface.start()

if __name__ == '__main__':
    guiTest()