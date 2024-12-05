# Programa 4.5- Patrones para ciclos (Loops Patterns)
# Fecha de elaboración: 2024/11/05
# Elaborado por: Diana Lucio 
#.................................................................................................. 
print("\n")
# THE COUNT PATTERN
letras = ["a","b","c","d","e"]
contador = 0 # Inicializa variable
for letra in letras:
    contador=contador+1
    print("La lista \"letras\" tiene", contador, "letras")
print("\n")

# THE SUM PATTERN
numeros = [100,200,300,400]
sumatoria = 0 # Inicialización
for numero in numeros:
    sumatoria=sumatoria+numero
    print("La sumatoria es ", sumatoria)
print("\n")

# THE ACCUMULATION PATTERN
palabras = ["Hoy", " " ,"hace", " " ,"frío"]
mensaje = " "
for palabra in palabras:
    mensaje=mensaje+palabra
    print(mensaje)
print("\n")

# THE MAP PATTERN
lista_anterior = ["Manzana", "Piña", "Uva"]
lista_nueva = [ ]
print("La lista vacía", lista_nueva)
for fruta in lista_anterior:
    lista_nueva.append(fruta)
    print("La lista copiada es: ", lista_nueva)
print("\n")
