# Programa 3.2- Programa que indique si, de dos números enteros ingresados son iguales o mayor/menor al otro
# Fecha de elaboración: 2024/10/28
# Elaborado por: Diana Lucio 
#.................................................................................................. 
print("\n")
n1 = input("Ingresa un número: ")
n1 = int(n1) # Se convierte a entero el string ingresado desde el teclado
n2 = int(input("Ingresa otro número: ")) # También se puede convertir a entero de esta manera
if (n1 > n2):
    print(str(n1) + " es mayor que " + str(n2))
elif n1 == n1:
    print(str(n1) + " es igual que " + str(n2))
else:
    print(str(n1) + " es menor que " + str(n2))
print("\n")
