import time
from sensor import SensorTemperatura
from controlador import ControladorInvernadero

class SimuladorInvernadero:
    def __init__(self):
        self.sensor = SensorTemperatura()
        self.controlador = ControladorInvernadero()

    def simular(self):
        while True:
            temperatura = self.sensor.leer_temperatura()
            self.controlador.controlar_temperatura(temperatura)
            estado = self.controlador.obtener_estado()
            print(f"Temperatura: {temperatura}°C | Estado: {estado}")
            time.sleep(5)  # Espera 5 segundos antes de la siguiente lectura