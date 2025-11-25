'''
Implementa una calculadora con las operaciones de suma (+), resta (-), multiplicación () y división (/).* 
El programa ofrecerá un menú con las operaciones disponibles y pedirá al usuario que introduzca una opción. 
A continuación, pedirá dos números y efectuará la operación requerida.

Esto se hará en 2 ficheros: operaciones.py que se encarga de las cuentas que realizamos y menu.py que esta la logica y llamadas a operaciones
'''

import operaciones

def mostrarMenu():
    print("Calculadora:")
    print("1. Sumar (+)")
    print("2. Restar (-)")
    print("3. Multiplicar (*)")
    print("4. Dividir (/)")
    print("5. Salir")

def pedirNumeros():
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))
    return a, b

def main():
    while True:
        mostrarMenu()
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "5":
            print("Fin del programa")
            break

        if opcion in ["1", "2", "3", "4"]:
            a, b = pedirNumeros()

            if opcion == "1":
                resultado = operaciones.sumar(a, b)
            elif opcion == "2":
                resultado = operaciones.restar(a, b)
            elif opcion == "3":
                resultado = operaciones.multiplicar(a, b)
            elif opcion == "4":
                resultado = operaciones.dividir(a, b)

            print(f"Resultado: {resultado}\n")
        else:
            print("Opción no válida. Intenta de nuevo.\n")

if __name__ == "__main__":
    main()
