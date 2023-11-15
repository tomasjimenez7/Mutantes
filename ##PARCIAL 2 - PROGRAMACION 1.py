##PARCIAL 2 - PROGRAMACION 1

print('''----- PROYECTO MUTANTES -----
    -- A continuación le solicitaremos el ingreso de las cadenas de ADN --
    -- El uso de la siguiente información es de extrema confidencialidad --
    -- Se pide seguir las instrucciones rigurosamente --''')

DNA = [""]*6
contador = 0
while contador < 6:
    
    cadena_ADN = input(f"Ingrese la cadena N° {contador + 1} de ADN (de seis letras):").upper()
    if len(cadena_ADN) == 6:
        
        #Revisa que se repitan solo estos caracteres y debe dar seis para comprobar
        #que cada letra (por mas que se repita) ocupe un lugar
        if (cadena_ADN.count("A") + cadena_ADN.count("T") + cadena_ADN.count("C") + cadena_ADN.count("G")) == 6:
            print("Caracteres correctos")
            DNA[contador] = cadena_ADN
            contador = contador + 1

        else: print("Recuerde que solo puede contener -A- -C- -G- o -T-. Intente nuevamente.")

    else: print("Debe contener un máximo de seis caracteres. Intente nuevamente")

print(DNA)
