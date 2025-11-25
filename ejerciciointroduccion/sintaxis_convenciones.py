"""
En Este primer programa, vamos a
practicar la sintaxis básica de Python.
"""

import ejerciciointroduccion.operaciones as operaciones      #Para importar funciones continuamos  con as NOMBRE para darle nombe a lo que llamamos 
# from operaciones import resta as res

# numero1 = int(input("Introduce un numero: "))
# numero2 = int(input("Introduce un segundo numero: "))
# print(restar(numero1, numero2))

#Esto imprime "Hola mundo" en pantalla
print("Hola mundo")

print(type(10))

edad = 25
print(type(edad))
precio = 19.90
nombre = "Python"
activo = True
ventas = None

print("edad",type(edad),"precio",type(precio))

lista1 = [1,2,3,4]
print(lista1[1])

midiccionario = {
    "nombre":"Paquito",
    "apellido":"Chocolatero",
    "usuario":"chocopaquito",
    "contraseña":"1234"
}

print(midiccionario["contraseña"])

conjunto1 = {10, 20, 30, 40}
conjunto2 = {1, 2, 3, "hola", "adios"}

print(list(conjunto2)[2])

numero1 = int(input("Introduce un numero: "))
numero2 = int(input("Introduce un segundo numero: "))

print(numero1 + numero2)

# if numero1 > numero2:
#     print(numero2 + " es mayor " + numero1 )
# else:
#     print(numero1 + " es mayor " + numero2 )

try:
    # Código que puede lanzar una excepción
    resultado = 10 / 0
except ZeroDivisionError:
    # Código a ejecutar si se produce una excepción del tipo ZeroDivisionError
    print("No se puede dividir por cero.")
except ValueError:
    # Código a ejecutar si se produce una excepción del tipo ValueError
    print("Valor incorrecto.")
except:
    # Código a ejecutar si se produce cualquier tipo de excepción
    print("Se produjo una excepción.")
    
    
def sumar(a, b):
  suma = a + b
  return suma   # Devuelve la suma de a y b

# total = sumar(5, 3)  # total ahora será 8

numero1 = int(input("Introduce un numero: "))
numero2 = int(input("Introduce un segundo numero: "))
print(sumar(numero1, numero2))

def saludar (nombre):
    return("hola, {nombre}")