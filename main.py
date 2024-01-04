from game import Game
from gui import Interface
class Parent1:
    def __init__(self):
        print("Parent1")

class Parent2:
    def __init__(self):
        print("Parent2")

    def test(self):
        print('Test!')

class Child(Parent1, Parent2):
    def __init__(self):
        super().__init__()
        Parent2.__init__(self)
        Parent2.test(self)
        print("Child")

def main():
    # newChild = Child()
    guiTest()
    # kingTest()
    # knightTest()
    # queenTest()
    # bishopTest()
    # rookTest()
    # pawnTest()

def guiTest():
    newInterface = Interface()
    newInterface.start()

def kingTest():
    newGame = Game()
    newGame.newTestGame()
    print('White:')
    print(newGame.getTokenMoves('E1'))
    newGame.move('E1', 'E2')
    print('Black:')
    print(newGame.getTokenMoves('E8'))
    newGame.move('E8', 'E7')
    print('White:')
    print(newGame.getTokenMoves('E2'))
    print('Threatens: ', newGame.getTokenThreatens('E2'))
    print('Black:')
    print(newGame.getTokenMoves('E7'))
    print('Threatens: ', newGame.getTokenThreatens('E7'))
    newGame.displayScore()

def knightTest():
    newGame = Game()
    newGame.newTestGame()
    print('White:')
    print(newGame.getTokenMoves('B1'))
    newGame.move('B1', 'C3')
    print('Black:')
    print(newGame.getTokenMoves('G8'))
    newGame.move('G8', 'F6')
    print('White:')
    print(newGame.getTokenMoves('C3'))
    print('Threatens: ', newGame.getTokenThreatens('C3'))
    print('Black:')
    print(newGame.getTokenMoves('F6'))
    print('Threatens: ', newGame.getTokenThreatens('F6'))
    newGame.displayScore()

def queenTest():
    newGame = Game()
    newGame.newTestGame()
    print('White:')
    print(newGame.getTokenMoves('D1'))
    newGame.move('D1', 'F3')
    print('Black:')
    print(newGame.getTokenMoves('D8'))
    newGame.move('D8', 'B6')
    print('White:')
    print(newGame.getTokenMoves('F3'))
    print('Threatens: ', newGame.getTokenThreatens('F3'))
    print('Black:')
    print(newGame.getTokenMoves('B6'))
    print('Threatens: ', newGame.getTokenThreatens('B6'))
    newGame.displayScore()

def bishopTest():
    newGame = Game()
    newGame.newTestGame()
    print('White:')
    print(newGame.getTokenMoves('C1'))
    newGame.move('C1', 'G5')
    print('Black:')
    print(newGame.getTokenMoves('F8'))
    newGame.move('F8', 'E7')
    print('White:')
    print(newGame.getTokenMoves('G5'))
    newGame.move('G5', 'E7')
    print('Black:')
    print(newGame.getTokenMoves('E7'))
    print('White:')
    print(newGame.getTokenMoves('E7'))
    newGame.displayScore()

def rookTest():
    newGame = Game()
    newGame.newTestGame()
    print('White:')
    print(newGame.getTokenMoves('A1'))
    newGame.move('A1', 'A5')
    print('Black:')
    print(newGame.getTokenMoves('H8'))
    newGame.move('H8', 'H5')
    print('White:')
    print(newGame.getTokenMoves('A5'))
    newGame.move('A5', 'H5')
    print('White:')
    print(newGame.getTokenMoves('H5'))
    print('Threatens: ', newGame.getTokenThreatens('H5'))
    newGame.displayScore()
    
def pawnTest():
    newGame = Game()
    newGame.newGame()
    print('White:')
    print(newGame.getTokenMoves('B2'))
    newGame.move('B2', 'B3')
    print('Black:')
    print(newGame.getTokenMoves('C7'))
    newGame.move('C7', 'C6')
    print('White:')
    print(newGame.getTokenMoves('B3'))
    newGame.move('B3', 'B4')
    print('Black:')
    print(newGame.getTokenMoves('C6'))
    newGame.move('C6', 'C5')
    print('White:')
    print(newGame.getTokenMoves('B4'))
    newGame.move('B4', 'C5')
    print('Black:')
    print(newGame.getTokenMoves('D7'))
    newGame.move('D7', 'D5')
    print('White:')
    print(newGame.getTokenMoves('C5'))
    newGame.move('C5', 'D6')
    print('Threatens: ', newGame.getTokenThreatens('D6'))
    newGame.displayScore()
# end main
    
if __name__ == '__main__':
    main()