def saludar(nombre):
    return f"Hola {nombre}, ¡bienvenido!"

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def presentar_persona(nombre="Usuario", edad=None, *aficiones):
    if edad is None:
        texto_edad = ""
    else:
        texto_edad = f" tiene {edad} años"
    texto_aficiones = f" y le gusta: {', '.join(aficiones)}" if aficiones else ""
    print(f"{nombre}{texto_edad}{texto_aficiones}")

if __name__ == "__main__":
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    altura = float(input("Altura en metros: "))
    peso = float(input("Peso en kg: "))
    print(saludar(nombre))
    print(f"IMC: {calcular_imc(peso, altura):.2f}")
    presentar_persona(nombre, edad, "leer", "correr")
