'''
Aqui meto las operaciones que seran llamadas en el programa principal
'''
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero no es posible."
    return a / b
