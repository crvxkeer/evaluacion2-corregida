from random import randint

# Entrada de datos con validación
while True:
    try:
        num1 = int(input("Ingrese límite inferior: "))
        num2 = int(input("Ingrese límite superior: "))
        if num1 < num2:
            break
        else:
            print("El límite inferior debe ser menor que el superior.")
    except:
        print("Debe ingresar números enteros.")

# Generar número aleatorio
numero = randint(num1, num2)

# Ajustar a número par
if numero % 2 != 0:
    if numero + 1 <= num2:
        numero += 1
    else:
        numero -= 1

# Juego con 3 intentos
intentos = 3
previo = None
for i in range(1, intentos + 1):
    intento = int(input(f"Intento {i}: Adivine el número: "))
    if intento == numero:
        print("Felicitaciones, pudiste adivinar.")
        break
    else:
        if intento < numero:
            print("El número es mayor.")
        else:
            print("El número es menor.")

        # Pista después del segundo intento
        if i == 2 and previo is not None:
            dif1 = abs(intento - numero)
            dif2 = abs(previo - numero)
            if dif1 < dif2:
                print("Te daré una pista: El número que buscas está más cerca de", intento)
            else:
                print("Te daré una pista: El número que buscas está más cerca de", previo)

    previo = intento

# Si no adivinó en 3 intentos
if intento != numero:
    print("Perdiste. El número era:", numero)