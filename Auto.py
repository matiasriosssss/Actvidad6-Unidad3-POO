import abc
from abc import ABC
class Auto(ABC):
    def __init__(self, modelo, puertas, color, preciobase):
        self.__modelo = modelo
        self.__puertas = int(puertas)
        self.__color = color
        self.__precioBase = float(preciobase)
        
    def getModelo(self):
        return self.__modelo
    def getPuertas (self):
        return self.__puertas
    def getColor(self):
        return self.__color
    def precioBase(self):
        return self.__precioBase
    def setPrecioBase(self, new):
        self.__precioBase = new
    @abc.abstractmethod
    def getPrecio(self):
        pass
    