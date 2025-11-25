# Definir variable para numero
# Pedir usuario introdzca un numero (3)
# 3*1=3   3*2=6   3*3=9
# validar que el usuario solo introduce numeros
# Imprimir el número multiplicado por un rango de 1 a 10 y el resultado
import sys
global num_usuario

def multiplicar_tabla(numero):
    for i in range(1, 11):
        print(f"{numero} * {i} = {numero * i}")
        
def pedir_numero():
    global num_usuario
    while num_usuario < 1 or num_usuario > 10:
        print("Solo valores del 1 al 10")
        try:
            num_usuario = int(input("Introduce que tabla de multiplicar quieres (número entero): "))
        except ValueError:
            print("Solo valores del 1 al 10")
        except:
            print("Ha ocurrido un error inesperado")
            
def ejecutar_con_argumento():
    if len(sys.argv) < 1 and len(sys.argv) > 1:
        print("El programa solo recibe un argumento")
    else:
        pintar_tablas(sys.arg[0])