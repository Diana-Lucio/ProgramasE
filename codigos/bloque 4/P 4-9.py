# Programa 4.9- Programa que demuestra el uso de los comandos \break\ y \continue\
# Fecha de elaboración: 2024/10/08
# Elaborado por: Diana Lucio   
#..................................................................................................  
print("\n")
# Ejemplo 1- Break
# Imprimir los números del 1 al 10, pero si el número es 5, salir del ciclo while
i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1 # Equivalente a i = i + 1
print("Fin del programa")
print("\n")
# Ejmeplo 2- Continue
# Imprimir los números del 1 al 10. pero si el número es 5 omitirlo
i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1
print("Fin del programa")
print("\n")
