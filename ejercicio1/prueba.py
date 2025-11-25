contador = 5
while contador < 20:
    contador += 1
    if contador%2 == 0:
        continue
    elif contador == 15:
        break
    print(f"El valor de contador es  {contador}")
    contador += 1