# Solicitar un dato al usuario:
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuál es tu edad? "))
altura = float(input("¿Cuál es tu altura? "))

print("Hola,", nombre , "tienes", edad , " años y mides ", altura ," metros.")

# Para poner el tipo de dato de cada uno:
print(type(nombre))
print(type(edad))
print(type(altura))