from nodo import Nodo
from Nuevo import Nuevo
from Usado import Usado
import json

class Lista:
    def __init__(self):
        self.__primerNodo = None
        self.__ultimoNodo = None
    def getUltimoNodo(self):
        return self.__ultimoNodo
    def lecArchivo(self):
        with open ('vehiculos.json', 'r') as file:
            archivo = json.load(file)
            vehiculos = archivo["vehiculos"]
            for vehiculo in vehiculos:
                if vehiculo["__class__"] == "Nuevo":
                    a = vehiculo["__atributos__"]
                    autoN = Nuevo(a["modelo"], a["puertas"], a["color"], a["preciobase"], a["version"], a["marca"])
                    self.agregarALista(autoN)
                    
                elif vehiculo["__class__"] == "Usado":
                    a = vehiculo["__atributos__"]
                    autoU = Usado(a["modelo"], a["puertas"], a["color"], a["preciobase"], a["patente"], a["anio"], a["kilometraje"], a["marca"])
                    self.agregarALista(autoU)
    
    def agregarALista(self, aut):
        newNodo = Nodo(aut)
        
        if self.__primerNodo == None:
            self.__primerNodo = newNodo
            self.__ultimoNodo = newNodo
        else:
            self.getUltimoNodo().agregarNodo(newNodo)
            self.__ultimoNodo = newNodo
    def agregarPorPosicion(self, aut, pos):
        newNodo = Nodo(aut)
        n = self.__primerNodo
        for i in range(pos - 1):
            n = n.sig()  ##ADELANTA EL NODO LA CANTIDAD DE VECES INDICADA
        newNodo.agregarNodo(n.sig()) ## A EL NUEVO NODO SE LE ASIGNA EL SIGUIENTE
        n.agregarNodo(newNodo) ##SE COLOCA EL NUEVO NODO EN LA POSICION
        print("Auto agregado correctamente a la lista...")
        
    def opcion1y2(self, boolean): ##CUANDO EL PARAMETRO BOOLEAN TOMA EL VALOR TRUE SE EJECUTA LA OPCION 1 Y CUANDO TOMA EL VALOR FALSO SE EJECUTA LA OPCION 2
        type = int(input("Ingrese el tipo de vehiculo (1: Nuevo, 2: Usado): "))
        if type == 1:
            modelo = input("Ingese nombre del modelo: ")
            puertas = int(input("Ingrese cantidad de puertas: "))
            color = input(("Ingrese color: "))
            pb = float(input("Ingrese precio base: "))
            version = input("Ingrese version (base o full): ")
            marca = 'Toyota'
            newAuto = Nuevo(modelo, puertas, color, pb, version, marca)
            if boolean:
                pos = int(input("Ingrese posicion a colocar: "))
                self.agregarPorPosicion(newAuto, pos)
            else:
                self.agregarALista(newAuto)
        elif type == 2:
            modelo = input("Ingese nombre del modelo: ")
            puertas = int(input("Ingrese cantidad de puertas: "))
            color = input(("Ingrese color: "))
            pb = float(input("Ingrese precio base: "))
            pat = input("Ingrese patente: ")
            año = int(input("Ingrese año: "))
            km = float(input("Ingrese cantidad de km: "))
            marca = input("Ingrese marca: ")
            newAuto = Usado(modelo, puertas, color, pb, pat, año, km, marca)
            if boolean:
                pos = int(input("Ingrese posicion a colocar: "))
                self.agregarPorPosicion(newAuto, pos)
            else:
                self.agregarALista(newAuto)
        else:
            print("Opcion mal ingresada...")
    def opcion3(self):
        pos = int(input("Ingresa la poscion a mostrar: "))
        n = self.__primerNodo
        centinela = True
        i=0
        while i < pos and centinela:
            if n.sig() != None: ##VERIFICA QUE LA LISTA NO SE HAYA TERMINADO
                n = n.sig()  ##ADELANTA EL NODO LA CANTIDAD DE VECES INDICADA
                i+=1
            else:
                print(f"La posicion numero {pos} no existe...")
                centinela = False
        if centinela:
            print(n.getAuto())
            
    def opcion4(self):
        pat = input("Ingrese la patente a buscar: ")
        i=0
        centinela = True
        n = self.__primerNodo
        while n != None and centinela:
            if isinstance(n.getAuto(),Usado):
                if n.getAuto().getPatente() == pat:
                    print("Vehiculo encontrado...")
                    nPB = float(input("Ingrese el nuevo precio base: "))
                    n.getAuto().setPrecioBase(nPB)
                    print(f"El nuevo precio es: {n.getAuto().getPrecio()}")
                    centinela = False
            n = n.sig()
        if centinela:
            print("No se encontro tal patente...")
    def opcion5(self):
        minimo = 9999999999999999
        n = self.__primerNodo
        while n != None:
            if n.getAuto().getPrecio() < minimo:
                minimo = n.getAuto().getPrecio()
                autoEconomico = n.getAuto()
            n = n.sig()
        print("El vehiculo mas economico es:")
        print(autoEconomico)
        
    def opcion6(self):
        n = self.__primerNodo
        print("-----LISTA DE AUTOS EN VENTA-----")
        while n != None:
            print(f"Modelo: {n.getAuto().getModelo()} - Puertas: {n.getAuto().getPuertas()} - Importe: {n.getAuto().getPrecio()}")
            n = n.sig()
    def listar(self):
        lista = []
        n = self.__primerNodo
        while n != None:
            obj = n.getAuto().to_dict()
            lista.append({"vehiculo":obj})
            n = n.sig()
        print(lista)
        return lista
    def opcion7(self):
        lis = self.listar()
        with open ('nuevaListaVehiculos.json', 'w') as archivo:
            json.dump(lis, archivo)
        print("Archivo creado exitosamente...")