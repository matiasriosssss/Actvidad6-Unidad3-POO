from Nuevo import Nuevo
from Usado import Usado


class Nodo:
    def __init__(self, auto):
        self.__auto = auto
        self.__sig = None
        self.__indice = 0
        
    def agregarNodo(self, newNodo):
        self.__sig = newNodo
    def sig(self):
        return self.__sig
    def getAuto(self):
        return self.__auto
    def getIndice(self):
        return self.__indice
    def setIndice(self, num):
        self.__indice = num
    
