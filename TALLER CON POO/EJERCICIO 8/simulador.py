from cliente import Cliente
from acceso import ControlAcceso

class SimuladorAcceso:
    def __init__(self):
        self.control_acceso = ControlAcceso()

    def simular(self):
        while True:
            tiene_membresia = input("¿El cliente tiene membresía? (s/n): ").lower() == "s"
            es_empleado = input("¿El cliente es empleado? (s/n): ").lower() == "s"

            cliente = Cliente(tiene_membresia, es_empleado)
            resultado = self.control_acceso.verificar_acceso(cliente)
            print(resultado)

            continuar = input("¿Desea verificar otro cliente? (s/n): ").lower()
            if continuar != "s":
                print("Saliendo del sistema de acceso...")
                break