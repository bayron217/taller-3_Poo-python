from FizzBuzz import FizzBuzz

class JuegoFizzBuzz:
    def __init__(self, inicio, fin):
        self.inicio = inicio
        self.fin = fin

    def jugar(self):
        for numero in range(self.inicio, self.fin + 1):
            fizzbuzz = FizzBuzz(numero)
            print(fizzbuzz)