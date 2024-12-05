# Programa 2.9- Programa que calcule el costo total de un número de artículos si:
# *Son 3 artículos o menos - Precio unitario $45.00
# *Más de 3 artículos - Precio unitario $30.00
# Al final mostrar un mensaje
# Fecha de elaboración: 2024/10/25
# Elaborado por: Diana Lucio   
#.................................................................................................. 

print("\n")
articulos = float(input("¿Cuántos artículos compró? "))
if articulos >=3: 
    total = articulos*30
else:
    total = articulos*45
print("El total a pagar es: $" + str(total))
print("¡Muchas gracias por comprar, que tenga un excelente día!")
print("\n")
