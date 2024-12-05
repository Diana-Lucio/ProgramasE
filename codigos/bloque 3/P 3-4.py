# Programa 3.4 Programa que calcule los impuestos con if, elif y else
# Fecha de elaboración: 2024/10/29
# Elaborado por: Diana Lucio 
#.................................................................................................. 
print("\n")
ingresos = input("¿Cuáles son tus ingresos? ")
ingresos = float(ingresos)
if ingresos <=1000:
    impuestos = ingresos * 0.05
elif ingresos >1000 and ingresos <=2500:
    impuestos = ingresos * 0.08
elif ingresos >2500 and ingresos <=6000:
    impuestos = ingresos * 0.12
else:
    impuestos = ingresos * 0.15
salario_total = ingresos - impuestos
print("Tus impuestos son " + str(impuestos) + " y tu salario final es " + str(salario_total))
print("\n")
