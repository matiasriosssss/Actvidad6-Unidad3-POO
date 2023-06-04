from Auto import Auto

class Nuevo(Auto):
    def __init__(self, modelo, puertas, color, precio, version, marca):
        super().__init__(modelo, puertas, color, precio)
        self.__version = version
        self.__marca = 'Toyota'
        
    def __str__(self):
        return "Marca: " + self.getMarca() + " Modelo: " + super().getModelo() + " Precio Final: " + str(self.getPrecio()) + " Version: " + self.__version + " Color: " + super().getColor()
    def getVersion(self):
        return self.__version
    def getMarca (self):
        return self.__marca
    def getPrecio(self):
        return super().precioBase() + ((10*super().precioBase()) / 100) + ((2*super().precioBase()) / 100)
    def to_dict(self):
        return self.__dict__