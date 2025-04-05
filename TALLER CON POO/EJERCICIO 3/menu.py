class Menu:
    def mostrar_menu(self):
        print("\n=== Calculadora ===")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

    def obtener_numeros(self):
        try:
            num1 = float(input("Primer número: "))
            num2 = float(input("Segundo número: "))
            return num1, num2
        except ValueError:
            print("Error: Ingresa números válidos.")
            return None, None