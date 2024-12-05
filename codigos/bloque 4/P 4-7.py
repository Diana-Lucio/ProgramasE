# Programa 4.7- Calculadora con opciones de operaciones
# Fecha de elaboración: 2024/10/06
# Elaborado por: Diana Lucio 
#.................................................................................................. 
print("\n")
a = input("Ingresa el primer número: ")
a = float(a)
b = input("Ingresa el segundo número: ")
b = float(b)

sel = input("""
    Selecciona una opción: 
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Módulo
            
    """)

resultado = 0
if sel == "1":
    resultado = a + b
elif sel == "2":
    resultado = a - b
elif sel == "3":
    resultado = a * b
elif sel == "4":
    resultado = a / b
elif sel == "5":
    resultado = a % b   
else:
    print("Opción no válida")
print("El resultado de la operación es: ", resultado)
print("\n")
