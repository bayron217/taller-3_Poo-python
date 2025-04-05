import time
from sensor import SensorMovimiento
from luces import Luces

class SimuladorLuces:
    def __init__(self):
        self.sensor = SensorMovimiento()
        self.luces = Luces()
        self.es_noche = True  # Simula si es de noche

    def simular(self):
        while True:
            self.sensor.detectar_movimiento()

            if self.es_noche and self.sensor.movimiento:
                self.luces.encender()
            else:
                self.luces.apagar()

            print(f"Estado de las luces: {self.luces.estado()}")
            time.sleep(10)