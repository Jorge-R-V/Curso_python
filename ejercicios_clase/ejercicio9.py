import emoji

def pedir_valores():
    try:
        num1 = float(input("Introduce el primer número: "))
        operador = input("Introduce el operador (+, -, *, /): ").strip()
        num2 = float(input("Introduce el segundo número: "))
        return num1, operador, num2
    except ValueError:
        print(emoji.emojize("⚠️ Entrada inválida. Asegúrate de introducir números válidos.", language="alias"))
        return None

def calcular(num1, operador, num2):
    if operador == "+":
        resultado = num1 + num2
        simbolo = emoji.emojize(":heavy_plus_sign:", language="alias")
    elif operador == "-":
        resultado = num1 - num2
        simbolo = emoji.emojize(":heavy_minus_sign:", language="alias")
    elif operador == "*":
        resultado = num1 * num2
        simbolo = emoji.emojize(":heavy_multiplication_x:", language="alias")
    elif operador == "/":
        if num2 == 0:
            print(emoji.emojize("🚫 No se puede dividir entre cero.", language="alias"))
            return None
        resultado = num1 / num2
        simbolo = emoji.emojize(":heavy_division_sign:", language="alias")
    else:
        print(emoji.emojize(f"⚠️ Operador '{operador}' no reconocido. Usa +, -, * o /.", language="alias"))
        return None

    return resultado, simbolo

def main():
    valores = pedir_valores()
    if valores is None:
        return

    num1, operador, num2 = valores
    resultado = calcular(num1, operador, num2)

    if resultado:
        valor, simbolo = resultado
        print(emoji.emojize(f"Resultado: {num1} {operador} {num2} = {valor} {simbolo}", language="alias"))

if __name__ == "__main__":
    main()
