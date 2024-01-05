from uuid import uuid4
import pygame
from core.square import Square
from core.game import Game
from os import path

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
        # guiScale = 1.2
        # res_factor = 82*guiScale
        # res_x, res_y = 10*res_factor, 10*res_factor
        # res_x, res_y = 1280, 720
        # res_x, res_y = 16*res_factor, 9*res_factor
        
        screen = pygame.display.set_mode((self.__res_x, self.__res_y))
        clock = pygame.time.Clock()
        running = True
        # dt = 0
        # player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        # print(res_x, res_factor, (res_x-res_factor*2)/8)
        newGame = Game()
        newGame.newGame()
        updateScreen = True
        currentPos = None
        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if not (pos[0] < self.__res_factor or pos[1] < self.__res_factor or pos[0] > self.__res_factor*9 or pos[1] > self.__res_factor*9):
                        for i in self.__squares:
                            if self.__squares[i].getStats()[0] < pos[0] < self.__squares[i].getStats()[0]+self.__res_factor:
                                if self.__squares[i].getStats()[1] < pos[1] < self.__squares[i].getStats()[1]+self.__res_factor:
                                    if currentPos == i:
                                        currentPos = None
                                        updateScreen = True
                                    else:
                                        currentPos = i
                                        updateScreen = True
                    else:
                        currentPos = None
                        updateScreen = True
                        # for x in self.__x:
                        #     if pos[0] > self.__squares[x+'8'].getStats()[0]:
                        #         for y in reversed(self.__y):
                        #             if pos[1] > self.__squares[x+str(9-int(y))].getStats()[1]:
                        #                 currentPos = x+str(9-int(y))
                        #                 print(currentPos)
                        #                 updateScreen = True
                        #             if x == 'H' and y == '1':
                        #                 currentPos = 'H1'
                        #                 print(currentPos)
                        #                 updateScreen = True
                                
                    # print(currentPos)
                    # print(pos)
                    # print(event.dict)
            # fill the screen with a color to wipe away anything from last frame
            # screen.fill("darkgray")
            if updateScreen:
                screen.fill(pygame.Color(100, 100, 100, a=255))
                self.loadPieces(newGame.getBoard())
                for i in self.__squares:
                    pygame.draw.rect(screen, self.__squares[i].getColor(), pygame.Rect(self.__squares[i].getStats()))
                for i in self.__squares:
                    if self.__squares[i].getPiece() != None:
                        if currentPos == i:
                            screen.blit(self.__images['dot_b_half'], (self.__squares[currentPos].getStats()[0], self.__squares[currentPos].getStats()[1]))
                            screen.blit(self.__images[self.__squares[i].getPiece()], (self.__squares[i].getStats()[0], self.__squares[i].getStats()[1]))
                            print(newGame.getTokenMoves(i))
                            for j in newGame.getTokenMoves(i):
                                print(j)
                                # print(newGame.getBoard()[j])
                                if newGame.getBoard()[j] != 'Empty\t\t':
                                    # print(newGame.getBoard())
                                    # print(i, newGame.getTokenStatus(i)['team'])
                                    if newGame.getTokenStatus(j)['team'] != newGame.getTokenStatus(i)['team']:
                                        screen.blit(self.__images['dot_r_half'], (self.__squares[j].getStats()[0], self.__squares[j].getStats()[1]))
                                    else:
                                        screen.blit(self.__images['dot_b_half'], (self.__squares[j].getStats()[0], self.__squares[j].getStats()[1]))
                                else:
                                    screen.blit(self.__images['dot_g_half'], (self.__squares[j].getStats()[0]+self.__res_factor/4, self.__squares[j].getStats()[1]+self.__res_factor/4))
                        else:
                            screen.blit(self.__images[self.__squares[i].getPiece()], (self.__squares[i].getStats()[0], self.__squares[i].getStats()[1]))
                        
                        # Testing Dots
                        # if i[0] == 'A':
                        #     screen.blit(self.__images['dot_b'], (self.__squares[i].getStats()[0], self.__squares[i].getStats()[1]))
                        # elif i[0] == 'B':
                        #     screen.blit(self.__images['dot_b_half'], (self.__squares[i].getStats()[0], self.__squares[i].getStats()[1]))
                        # elif i[0] == 'C':
                        #     screen.blit(self.__images['dot_g'], (self.__squares[i].getStats()[0]+self.__res_factor/4, self.__squares[i].getStats()[1]+self.__res_factor/4))
                        # if i[0] == 'D' or i[0] == 'A' or i[0] == 'C':
                        #     screen.blit(self.__images['dot_g_half'], (self.__squares[i].getStats()[0]+self.__res_factor/4, self.__squares[i].getStats()[1]+self.__res_factor/4))
                        # elif i[0] == 'E':
                        #     screen.blit(self.__images['dot_r'], (self.__squares[i].getStats()[0], self.__squares[i].getStats()[1]))
                        # elif i[0] == 'F' or i[0] == 'B':
                        #     screen.blit(self.__images['dot_r_half'], (self.__squares[i].getStats()[0], self.__squares[i].getStats()[1]))
                
                # flip() the display to put your work on screen
                
                pygame.display.flip()
                updateScreen = False

            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            # dt = clock.tick(60) / 1000

        pygame.quit()

    def test(self):
        pygame.init()
        res_x, res_y = 1280, 720
        screen = pygame.display.set_mode((res_x, res_y))
        clock = pygame.time.Clock()
        running = True
        dt = 0

        player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # fill the screen with a color to wipe away anything from last frame
            screen.fill("purple")

            pygame.draw.circle(screen, "red", player_pos, 40)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                player_pos.y -= 300 * dt
            if keys[pygame.K_s]:
                player_pos.y += 300 * dt
            if keys[pygame.K_a]:
                player_pos.x -= 300 * dt
            if keys[pygame.K_d]:
                player_pos.x += 300 * dt

            # flip() the display to put your work on screen
            pygame.display.flip()

            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            dt = clock.tick(60) / 1000

        pygame.quit()

def guiTest():
    newInterface = Interface()
    newInterface.start()

if __name__ == '__main__':
    guiTest()