import time
from sensor import SensoresMovimiento  # Importación corregida
from alarma import Alarma

class SimuladorSeguridad:
    def __init__(self):
        self.sensores = SensoresMovimiento()
        self.alarma = Alarma()
        self.es_noche = True  # Simula si es de noche

    def mostrar_menu(self):
        print("\n=== Menú de Seguridad ===")
        print("1. Activar alarma")
        print("2. Desactivar alarma")
        print("3. Simular detección de movimiento")
        print("4. Salir")

    def simular(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción (1-4): ")

            if opcion == "1":
                self.alarma.activar()
            elif opcion == "2":
                self.alarma.desactivar()
            elif opcion == "3":
                self.sensores.leer_sensores()
                if self.es_noche and self.sensores.al_menos_dos_activos():
                    if self.alarma.estado() == "Activada":
                        print("¡Alarma activada! Intruso detectado.")
                    else:
                        print("Movimiento detectado, pero la alarma está desactivada.")
                else:
                    print("No se detectó intrusión.")
            elif opcion == "4":
                print("Saliendo del sistema de seguridad...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

            time.sleep(2)  # Espera 2 segundos antes de mostrar el menú nuevamente