class Square():
    def __init__(self, color, x:float, y:float, w:float, h:float):
        self.__color = color
        self.__x = x
        self.__y = y
        self.__w = w
        self.__h = h
        self.__piece = None

    def __del__(self):
        del self.__color, self.__x, self.__y, self.__w, self.__h, self.__piece

    def getStats(self):
        return (self.__x, self.__y, self.__w, self.__h)
    
    def getColor(self):
        return self.__color
    
    def setPiece(self, piece:str):
        self.__piece = piece

    def getPiece(self):
        return self.__piece
# end Square