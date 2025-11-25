def pedir_edad():
    while True:
        try:
            edad = int(input("Introduce tu edad: "))
            return edad
        except ValueError:
            print("Edad inválida. Debes ingresar un número entero.")

def pedir_altura():
    while True:
        try:
            altura = float(input("Introduce tu altura en metros (ej. 1.75): "))
            return altura
        except ValueError:
            print("Altura inválida. Debes ingresar un número decimal.")

def main():
    edad = pedir_edad()
    altura = pedir_altura()
    print(f"Edad: {edad} años, Altura: {altura} m")

if __name__ == "__main__":
    main()
