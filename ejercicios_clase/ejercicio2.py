def saludar(nombre):
    """Recibe un nombre y devuelve un saludo."""
    return f"Hola {nombre}, ¡bienvenido!"

def calcular_imc(peso, altura):
    """Devuelve el IMC (índice de masa corporal) dado peso en kg y altura en metros."""
    return peso / (altura ** 2)

# Solicitar datos al usuario
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad (número entero): "))
altura = float(input("Introduce tu altura en metros (ej. 1.70): "))
peso = float(input("Introduce tu peso en kilogramos (ej. 68.5): "))

# Usar las funciones
saludo = saludar(nombre)
imc = calcular_imc(peso, altura)

# Mostrar resultados con f-strings
print(f"{saludo} Tienes {edad} años y mides {altura} metros.")
print(f"Tu IMC es {imc:.2f}.")

# Mostrar tipo de dato de cada variable
print("Tipo de 'nombre':", type(nombre))
print("Tipo de 'edad':", type(edad))
print("Tipo de 'altura':", type(altura))
print("Tipo de 'peso':", type(peso))
print("Tipo de 'saludo':", type(saludo))
print("Tipo de 'imc':", type(imc))
