# Programa 3.5- Programa que calcule el nivel de desempeño de un estudiante respecto a su calificación 
# dada por el usuario, de acuerdo a la siguiente tabla:
# Menos de 60 -> Insuficiente
# 70-79 -> Suficiente
# 80-89 -> Muy bien
# 90-95 -> Notable
# 96-100 -> Excelente
# Fecha de elaboración: 2024/10/14 
# Elaborado por: Diana Lucio 
#.................................................................................................. 
print("\n")
calif = float(input("Calificación del estudiante (0-100): "))
if calif <= 60:
    desempeño = "Insuficiente"
elif 60 < calif <= 79 :
    desempeño = "Suficiente"
elif 79 < calif <= 89:
    desempeño = "Muy bien"
elif 89 < calif <= 95:
    desempeño = "Notable"
elif 95 < calif <= 100:
    desempeño = "Excelente"
print(f"El nivel de desempeño es: {desempeño}")
print("\n")
