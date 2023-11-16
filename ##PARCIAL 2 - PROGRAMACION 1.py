##PARCIAL 2 - PROGRAMACION 1

print('''----- PROYECTO MUTANTES -----
    -- A continuación le solicitaremos el ingreso de las cadenas de ADN --
    -- El uso de la siguiente información es de extrema confidencialidad --
    -- Se pide seguir las instrucciones rigurosamente --''')

ADN = [""]*6
contador = 0
while contador < 6:
    
    cadena_ADN = input(f"Ingrese la cadena N° {contador + 1} de ADN (de seis letras):").upper()
    if len(cadena_ADN) == 6:
        
        #Revisa que se repitan solo estos caracteres y debe dar seis para comprobar
        #que cada letra (por mas que se repita) ocupe un lugar
        if (cadena_ADN.count("A") + cadena_ADN.count("T") + cadena_ADN.count("C") + cadena_ADN.count("G")) == 6:
            print("Caracteres correctos")
            ADN[contador] = cadena_ADN
            contador = contador + 1

        else: print("Recuerde que solo puede contener -A- -C- -G- o -T-. Intente nuevamente.")

    else: print("Debe contener un máximo de seis caracteres. Intente nuevamente")

print("----Se formo el siguiente ADN al juntar las diferentes cadenas----")
for fila in ADN:
    print(" ".join(fila)) # Se suma un espacio entre cada caracter, que en definitiva también es una lista


def esMutante(ADN):
        secuencia = 0
        for fila in ADN: #Compara de forma horizontal
            if (fila[0] == fila[1] == fila[2] == fila[3]) | (fila[1] == fila[2] == fila[3] == fila[4]) | (fila[2] == fila[3] == fila[4] == fila[5]):
                secuencia = secuencia + 1
                if secuencia > 1:
                    return True
        
        ADN_transpuesta = list(zip(*ADN)) #Transpongo los elementos para aplicar el metodo anterior
        for fila in ADN_transpuesta: #Compara de forma horizontal
            if (fila[0] == fila[1] == fila[2] == fila[3]) | (fila[1] == fila[2] == fila[3] == fila[4]) | (fila[2] == fila[3] == fila[4] == fila[5]):
                secuencia = secuencia + 1
                if secuencia > 1:
                    return True
                
        for fila in range(len(ADN)-3): #Controla las diagonales
            for columna in range(len(ADN[0])-3):
                if ADN[fila][columna] == ADN[fila+1][columna+1] == ADN[fila+2][columna+2] == ADN[fila+3][columna+3]:
                    secuencia = secuencia + 1
                    if secuencia > 1:
                        return True

        for fila in range(len(ADN)-3): #Controla las diagonales inversas
            for columna in range(3, len(ADN[0])):
                if ADN[fila][columna] == ADN[fila+1][columna-1] == ADN[fila+2][columna-2] == ADN[fila+3][columna-3]:
                    secuencia = secuencia + 1
                    if secuencia > 1:
                        return True

        return False

es_Mutante = esMutante(ADN)

print("----El resultado obtenido es el siguiente----")
if es_Mutante:
    print("Es mutante")
else:
    print("No es mutante")
