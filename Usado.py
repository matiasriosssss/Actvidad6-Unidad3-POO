from Auto import Auto
class Usado(Auto):
    def __init__(self, modelo, puertas, color, preciobase, patente, anio, kilometraje, marca):
        super().__init__(modelo, puertas, color, preciobase)
        self.__patente = patente
        self.__año = int(anio)
        self.__km = int(kilometraje)
        self.__marca = marca
    
    def __str__(self):
        return "Marca: " + self.getMarca() + " Modelo: " + super().getModelo() + " Precio Final: " + str(self.getPrecio()) + " Color " + super().getColor() + " Año: " + str(self.getAño()) + " Kilometros: " + str(self.getKm())
    def getMarca (self):
        return self.__marca
    def getPatente(self):
        return self.__patente
    def getAño(self):
        return self.__año
    def getKm(self):
        return self.__km
    def setPrecioBase(self, nuevoPrecio):
        super().setPrecioBase(nuevoPrecio)
        print("Precio base modificado...")
    def getPrecio(self):
        return super().precioBase() - ((((2023 - self.__año))*super().precioBase()) / 100) - self.calc_km()
    def calc_km(self):
        if self.__km > 100000:
            calculo = (super().precioBase() * 2) / 100
        else:
            calculo = 0
        return calculo 
    def to_dict(self):
        return self.__dict__