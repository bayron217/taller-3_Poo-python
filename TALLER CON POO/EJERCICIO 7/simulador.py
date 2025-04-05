import time
from sensores import Sensores
from aire import AireAcondicionado

class SimuladorAire:
    def __init__(self):
        self.sensores = Sensores()
        self.aire = AireAcondicionado()

    def simular(self):
        while True:
            self.sensores.leer_temperatura()
            self.sensores.leer_humedad()

            if (self.sensores.temperatura > 28 and self.sensores.humedad > 60) or self.sensores.temperatura > 30:
                self.aire.encender()
            else:
                self.aire.apagar()

            print(f"Estado del aire acondicionado: {self.aire.estado()}")
            time.sleep(10)  # Espera 10 segundos antes de la siguiente lectura