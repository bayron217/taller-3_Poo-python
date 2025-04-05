class SensoresMovimiento:
    def __init__(self):
        self.sensor1 = False
        self.sensor2 = False
        self.sensor3 = False

    def leer_sensores(self):
        # Simulamos la lectura de los sensores (puedes cambiarla manualmente)
        self.sensor1 = input("Sensor 1 detectó movimiento? (s/n): ").lower() == "s"
        self.sensor2 = input("Sensor 2 detectó movimiento? (s/n): ").lower() == "s"
        self.sensor3 = input("Sensor 3 detectó movimiento? (s/n): ").lower() == "s"

    def al_menos_dos_activos(self):
        # Verifica si al menos dos sensores están activos
        sensores_activos = [self.sensor1, self.sensor2, self.sensor3]
        return sum(sensores_activos) >= 2