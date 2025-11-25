import random
import emoji

# Almacen de colores y emojis que usaremos
COLORES_DISPONIBLES = {
    'R': '🔴 emoji.emojize(`:red_circle`)',  # Rojo
    'G': '🟢emoji.emojize(`:green_circle`)',  # Verde
    'B': '🔵emoji.emojize(`:blue_circle`)',  # Azul
    'Y': '🟡emoji.emojize(`:yellow_circle`)',  # Amarillo
    'P': '🟣emoji.emojize(`:purple_circle`)',  # Púrpura
    'O': '🟠emoji.emojize(`:orange_circle`)'   # Naranja
}

def generar_combinacion():
    # Generador de la combinación secreta de 4 colores aleatorios.
    return random.choices(list(COLORES_DISPONIBLES.keys()), k=4)

def mostrar_historial():
    # Muestro los colores disponibles.
    print("Colores disponibles:")
    for letra, icono in COLORES_DISPONIBLES.items():
        print(f"{letra} → {emoji.emojize(icono)}")

def validar_entrada(entrada):
    # Validacion de que estén 4 colores ingresados
    entrada = entrada.upper()
    return len(entrada) == 4 and all(letra in COLORES_DISPONIBLES for letra in entrada)

def mostrar_combinacion_emojis(combinacion):
    # Conviersor de letras a emijis
    return ' '.join(COLORES_DISPONIBLES[letra] for letra in combinacion)

def evaluar_intento(intento, secreto):
    # Comparador errores y aciertos
    colores_correctos = sum(min(intento.count(c), secreto.count(c)) for c in set(intento))
    posiciones_correctas = sum(1 for i in range(4) if intento[i] == secreto[i])
    return colores_correctos, posiciones_correctas
