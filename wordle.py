def obtener_fila_verificada(palabra_ingresada, palabra_secreta):

    # creamos la lista vacia
    letras_verificadas = []

    # verificar si las letras de palabra_ingresada existen en palabra_secreta
    
    cantidad_de_letras = len(palabra_secreta)

    for pos in range(cantidad_de_letras):
        # verificar si la letra existe en palabra_secreta
        letra_existe_en_la_palabra = palabra_ingresada[pos] in palabra_secreta

        # verificar si las posiciones de la letras
        letras_poseen_misma_posicion = palabra_ingresada[pos] == palabra_secreta[pos]

        # Si las letras existen en la palabra a encontrar y sus posiciones coinciden
        if letra_existe_en_la_palabra and letras_poseen_misma_posicion:
            letras_verificadas.append("[" + palabra_ingresada[pos] + "]")
        
        # Si las letras existen en la palabra a encontrar pero sus posiciones no coinciden
        elif letra_existe_en_la_palabra and not letras_poseen_misma_posicion:
            letras_verificadas.append("(" + palabra_ingresada[pos] + ")")

        # Si no se cumple ninguna de las anteriores, agregar la letra a la lista vacía sin modificaciones
        else:
            letras_verificadas.append(palabra_ingresada[pos])
    
    # devolvemos el resultado
    return letras_verificadas 


def imprimir_grilla(lista_palabras):
    for lista_letras in lista_palabras:
        print(lista_letras)


import os

# Empezamos a definir el juego

os.system("clear")

palabra_a_encontrar = "horas"
cantidad_de_letras = 5
intentos = 6

grilla = []

while intentos > 0:
    print(f"Te quedan {intentos} intentos")
    intentos = intentos - 1
    palabra_ingresada = input("Ingrese una palabra de 5 letras: ")

    os.system("clear")
    
    # Verificar cantidad de letras en palabra_ingresada
    cantidad_de_letras_palabra_ingresada = len(palabra_ingresada)
    if cantidad_de_letras_palabra_ingresada != cantidad_de_letras:
        print(f"Favor ingrese una palabra de {cantidad_de_letras} letras")
    else:
        linea_verificada = obtener_fila_verificada(palabra_ingresada, palabra_a_encontrar)

        grilla.append(linea_verificada)

        imprimir_grilla(grilla)

    # que pasa si acierta?
    if palabra_ingresada == palabra_a_encontrar:
        print("GANASTE BROSKI")
        break
    
print("TE QUEDASTE SIN INTENTOS")