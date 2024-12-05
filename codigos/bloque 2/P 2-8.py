# Programa 2.8- Programa que calcule el promedio de 5 unidades e indique si aprobó la materia
# Fecha de elaboración: 2024/10/24
# Elaborado por: Diana Lucio   
#..................................................................................................  

print("\n")
num1 = float(input("Calificación de la unidad 1: "))
num2 = float(input("Calificación de la unidad 2: "))
num3 = float(input("Calificación de la unidad 3: "))
num4 = float(input("Calificación de la unidad 4: "))
num5 = float(input("Calificación de la unidad 5: "))

calificaciones = (num1+num2+num3+num4+num5)/5

if calificaciones >=7:
    print("Aprobaste tus materias...¡Felicidades!")

else:
    print("Desaprobaste tus materias...vuelve a intentarlo, ¡tú puedes!")
print("\n")
