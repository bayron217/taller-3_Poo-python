class FizzBuzz:
    def __init__(self, numero):
        self.numero = numero

    def es_fizz(self):
        return self.numero % 3 == 0

    def es_buzz(self):
        return self.numero % 5 == 0

    def es_fizzbuzz(self):
        return self.es_fizz() and self.es_buzz()

    def __str__(self):
        if self.es_fizzbuzz():
            return "FizzBuzz"
        elif self.es_fizz():
            return "Fizz"
        elif self.es_buzz():
            return "Buzz"
        else:
            return str(self.numero)