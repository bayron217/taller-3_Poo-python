from Juego_FizzBuzz import JuegoFizzBuzz

def main():
    inicio = 1
    fin = 100
    juego = JuegoFizzBuzz(inicio, fin)
    print(f"¡Bienvenido al juego FizzBuzz! (Números del {inicio} al {fin})")
    juego.jugar()

if __name__ == "__main__":
    main()