# Programa 4.12- Programa que se repite indefinidamente hasta que se ingrese la palabra salir
# Fecha de elaboración: 2024/10/09
# Elaborado por: Diana Lucio   
#..................................................................................................  
print("\n")
# Inicialización de variables
palabra = ""
while True:
    palabra = input("Ingresa una palabra o 'salir' para terminar: ")
    palabra = palabra.lower() # Convierte la palabra a minúsculas
    print("Usted ingresó: ", palabra)
    if palabra == "salir":
        break
print("\nFin del programa \U0001F601 \n") # Imprime un eoji feliz
print("¡Hasta luego! \U0001F44B \n") # Imprime un emoji de saludo 
