# Programa 4.11- Programa que se repite hasta que ingrese la palabra salir
# Fecha de elaboración: 2024/11/15
# Elaborado por: Diana Lucio   
#..................................................................................................  
print("\n")
# Inicialización de variables
palabra = ""
while palabra != "salir":
    palabra = input("Ingresa una palabra o 'salir' para terminar: ")
    palabra = palabra.lower() # Convierte la palabra a minúsculas
    print("Usted ingresó: ", palabra)
print("\nFin del programa\n") 
