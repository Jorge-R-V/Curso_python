# Pide nombre, edad y altura; muestra un mensaje con f-string y el tipo de cada variable

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad (número entero): "))
altura = float(input("Introduce tu altura en metros (ej. 1.70): "))

# Mensaje con f-string
print(f"Hola {nombre}, tienes {edad} años y mides {altura} metros.")

# Mostrar tipo de dato de cada variable
print("Tipo de 'nombre':", type(nombre))
print("Tipo de 'edad':", type(edad))
print("Tipo de 'altura':", type(altura))
