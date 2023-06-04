from Lista import Lista
from Nuevo import Nuevo
from Usado import Usado
def test(lis):
    autoN = Nuevo("Corrolla22", 5, "Rojo", 2200000, "Full", "Toyota")
    autoU = Usado("Scirocco", 5, "Negro", 28000000, "AFG456", "2013", 39000, "Volkswagen" )
    lis.agregarPorPosicion(autoN, 2)
    lis.agregarPorPosicion(autoU, 7)
    
    

if __name__ == '__main__':
    lis = Lista()
    lis.lecArchivo()
    o=1
    while o != 0:
        print("""
    --------MENU---------
    1_Insertar vehiculo en una posicion determinada
    2_ Agregar vehiculo
    3_ Mostrar vehiculo dada una posicion
    4_ Modificar precio base y mostrar el nuevo precio dado una patente
    5_ Mostrar datos del vehiculo mas economico
    6_ Mostrar vehiculos en venta
    7_ Almacenar nueva lista en un archivo json
    
    """)
        o = int(input("Ingrese opcion: "))
        if o==1:
            lis.opcion1y2(True) ##CUANDO PASAMOS EL PARAMETRO TRUE SE EJECUTA LA OPCION 1
        elif o == 2:            ##HACEMOS ESTO PARA FOMENTAR LA REUTILIZACION DE CODIGO
            lis.opcion1y2(False) ##CUANDO PASAMOS EL PARAMETRO FALSE SE EJECUTA LA OPCION 2
        elif o == 3:
            lis.opcion3()
        elif o == 4:
            lis.opcion4()
        elif o == 5:
            lis.opcion5()
        elif o==6:
            lis.opcion6()
        elif o == 7:
            lis.opcion7()
        elif o == 0:
            exit()
        else:
            print("Opcion mal ingresada...")