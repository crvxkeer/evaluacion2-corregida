# Ejercicio 1: Cálculo de medicamentos y despacho con validaciones

# Validación de edad
flag_edad = True
while flag_edad:
    try:
        edad = int(input("Ingrese su edad: "))
        if edad <= 0:
            print("Su edad debe ser mayor a cero.")
        else:
            flag_edad = False
    except:
        print("Debe ingresar un número entero.")

# Validación de tramo
flag_tramo = True
while flag_tramo:
    tramo = input("Ingrese su tramo (A, B, C o D): ").upper()
    if tramo in ["A", "B", "C", "D"]:
        flag_tramo = False
    else:
        print("Debe ingresar las siguientes opciones: (A, B, C o D).")

# Valores base
valor_medicamentos = 60000
valor_despacho = 8000

# Valores variables 
descuento_medicamentos = 0.0
descuento_despacho = 0.0

# Cálculo de descuento en medicamentos
if edad <= 30:
    if tramo in ["A", "B"]:
        descuento_medicamentos = 0.18
    else:
        descuento_medicamentos = 0.12
elif edad >= 31 and edad <= 60:
    if tramo in ["A", "B"]:
        descuento_medicamentos = 0.12
    else:
        descuento_medicamentos = 0.08
elif edad > 60: 
    descuento_medicamentos = 0.0

# Cálculo de descuento en despacho
if tramo in ["A", "B"]:
    descuento_despacho = 0.10
    if edad >= 55:
        descuento_despacho += 0.05

# Aplicar descuentos
total_medicamentos = int(valor_medicamentos - (valor_medicamentos * descuento_medicamentos))
total_despacho = int(valor_despacho - (valor_despacho * descuento_despacho))

# Mostrar resultados
print(f"El valor de medicamentos es: ${total_medicamentos}")
print(f"El valor de despacho es: ${total_despacho}")
