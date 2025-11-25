
from mastermind_utils import (
    generar_combinacion,
    mostrar_historial,
    validar_entrada,
    mostrar_combinacion_emojis,
    evaluar_intento
)

def jugar_mastermind():
    print("Bienvenido al juego Mastermind")
    mostrar_historial()
    secreto = generar_combinacion()
    intentos = 0

    while True:
        entrada = input("\nIntroduce tu combinación (4 letras): ").upper()
        if not validar_entrada(entrada):
            print("❌ Entrada inválida. Usa 4 letras válidas de la leyenda.")
            continue

        intento = list(entrada)
        intentos += 1

        print("Tu combinación:", mostrar_combinacion_emojis(intento))
        colores, posiciones = evaluar_intento(intento, secreto)
        print(f"Colores correctos (pero en posición incorrecta): {colores} | Posiciones correctas: {posiciones}")

        if intento == secreto:
            print("\n ¡Felicidades! Has adivinado la combinación.")
            print("Combinación secreta:", mostrar_combinacion_emojis(secreto))
            print(f"🔢 Número de intentos: {intentos}")
            break

if __name__ == "__main__":
    jugar_mastermind()
