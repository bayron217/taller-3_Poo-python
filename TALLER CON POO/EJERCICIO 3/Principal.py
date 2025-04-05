from Calculadora import Calculadora
from menu import Menu

def main():
    calculadora = Calculadora()
    menu = Menu()

    while True:
        menu.mostrar_menu()
        opcion = input("Elige una opción (1-5): ")
        
        if opcion == "5":
            print("¡Adiós!")
            break
        
        if opcion not in ["1", "2", "3", "4"]:
            print("Opción incorrecta")
            continue
        
        num1, num2 = menu.obtener_numeros()
        if num1 is None or num2 is None:
            continue
        
        if opcion == "1":
            resultado = calculadora.suma(num1, num2)
        elif opcion == "2":
            resultado = calculadora.resta(num1, num2)
        elif opcion == "3":
            resultado = calculadora.multiplicacion(num1, num2)
        elif opcion == "4":
            resultado = calculadora.division(num1, num2)
        
        print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()