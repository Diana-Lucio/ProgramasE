# Programa 1.8- Programa que calcule el número de minutos, horas y meses, dado el número de días 
# por el usuario 
# Fecha de elaboración: 2024/10/16   
# Elaborado por: Diana Lucio   
#..................................................................................................  
dias = int(input("Ingresa el número de días: ")) 
horas = dias * 24 
minutos = horas * 60 
meses = dias / 30 
print("El número de minutos es: " + str(minutos)) 
print("El número de horas es: " + str(horas)) 
print("El número de meses es: " + str(meses)) 
