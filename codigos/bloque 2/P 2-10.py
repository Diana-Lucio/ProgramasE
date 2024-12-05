# Programa 2.10- Programa que revise si puedes ver una película en Netflix.
# La condidición para esto es que seas mayor de edad y que hayas comprado la película.
# Fecha de elaboración: 2024/10/25
# Elaborado por: Diana Lucio   
#.................................................................................................. 

print("\n")
edad = int(input("¿Cuál es tu edad?: "))
if edad >=18:
    compra = int(input("Compraste la película? \n 1 significa si \n 0 significa no  "))
    if compra == 1:
      print("Puedes ver la película")
else:
   print("Vete a hacer la tarea")
print("Gracias por usar Netflix")
print("\n")
