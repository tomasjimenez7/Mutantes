# Mutantes
Parcial 2 - Programación 1
* Nombre y Apellido: Tomás Jiménez
* Legajo: 51574
* Email: tommasjiimenez@hotmail.com

## De que va el proyecto

 El proyecto consiste en crear un código que sea capaz de analizar cadenas de string almacenadas en un array de 6x6, las cuales son ingresadas por el usuario.
 Estas mismas representan cadenas de ADN, debido a que de manera ficticia somos contratados por Magneto, uno de los personajes de X-Men, y necesita que averiguemos quien es mutante para poder reclutarlo.

 Deben cumplirse varias pautas:
    - El string ingresado debe tener una longitud de 6.
    - Solo puede contener los carácteres "A","C","G" o "T"
    - Debe utilizarse un método o función para validar si es o no mutante:     boolean isMutant(String[] dna);

Se sabrá si un humano es mutante, si en su cadena de ADN contiene más de una secuencia de cuatro caracteres iguales, de forma diagonal, horizontal o vertical.

## Como lo resolvimos

Iniciamos creando el array de 6 strings, con espacios vacios que luego serán llenados con lo que ingrese el usuario. También creamos la variable contador que utilizaremos en un Ciclo While para controlar la cantidad de variables que se ingresan al array :

```
ADN = [""]*6
contador = 0
```

Iniciamos el Ciclo While, le pedimos al usuario que ingrese una cadena de ADN y lo primero que hacemos con el dato ingresado es transformarlo en mayúscula y verificar con un Condiciona If si cumple con la longitud de 6:

```
while contador < 6:
    
    cadena_ADN = input(f"Ingrese la cadena N° {contador + 1} de ADN (de seis letras):").upper()
    if len(cadena_ADN) == 6:
    ...
    ...
    ...
     else: print("Debe contener un máximo de seis caracteres. Intente nuevamente")
```
Si no cumple con el IF de longitud vuelve a pedir que se ingrese de forma correcta. Si lo cumple pasa al siguiente IF donde se verifica que solo contenga "A","C","G" o "T":

```
if (cadena_ADN.count("A") + cadena_ADN.count("T") + cadena_ADN.count("C") + cadena_ADN.count("G")) == 6:
...
...
...
else: print("Recuerde que solo puede contener -A- -C- -G- o -T-. Intente nuevamente.")
```

Si no cumple con éste segundo IF se vuelve a pedir el ingreso del dato. Si lo cumple se asigna el dato dentro de la posicion que corresponda dentro del array según el número del iterador (contador) y a la variable contador se le suma 1 para que una vez que sea igual que 6 se termine el Ciclo While:

```
print("Caracteres correctos")
ADN[contador] = cadena_ADN
contador = contador + 1
```

Una vez completado el array, se muestra por consola con el formato cuadrado de una matriz, para que sea posible analizarlo visualmente:

```
print("----Se formo el siguiente ADN al juntar las diferentes cadenas----")
for fila in ADN:
    print(" ".join(fila))
```

Luego definimos la función que se nos solicitaba

```
def esMutante(ADN):
```

Dentro de ella primero creamos una variable la cual llamamos "secuencia" y nos servira como especie de contador para saber si hay más de una sucesión de cuatro o más carácteres iguales(la iniciamos en 0). Luego iniciamos un Ciclo For para recorrer los elementos del array, y dentro del FOR colocamos un IF que compare cada caracter de cada fila con el caracter que tiene a su derecha (Control horizontal): 

```
for fila in ADN: #Compara de forma horizontal
    if (fila[0] == fila[1] == fila[2] == fila[3]) | (fila[1] == fila[2] == fila[3] == fila[4]) | (fila[2] == fila[3] == fila[4] == fila[5]):
```

Si cumple la condición del IF, a "secuencia" se le sumará 1. Dentro de éste IF se encuentra otro IF que verifica si "secuencia" es mayor a 1. Si se cumple retornará un TRUE, evidenciando que es mutante al tener más de una secuencia con carácteres iguales.

```
secuencia = secuencia + 1
if secuencia > 1:
    return True
```

Si no se cumplió ninguno de los parámetros anteriores, se ingresará a otro Ciclo For en donde compararemos los carácteres pero de forma vertical. En ésta ocasión vamos a transponer el array, para que lo que serian filas se conviertan en columnas y viceversa, y guardamos el resultado en otra variable. Lo realizamos con la siguiente función:

```
ADN_transpuesta = list(zip(*ADN))
```

Luego hacemos exactamente lo mismo que en el FOR anterior, comparando de manera horizontal cada caracter de cada elemento del array transpuesto:

```
for fila in ADN_transpuesta: #Compara de forma horizontal
    if (fila[0] == fila[1] == fila[2] == fila[3]) | (fila[1] == fila[2] == fila[3] == fila[4]) | (fila[2] == fila[3] == fila[4] == fila[5]):
        secuencia = secuencia + 1
        if secuencia > 1:
            return True
```

Si hasta ahora ninguno de los Ciclo For anteriores a retornado un TRUE, entonces se ingresará al primer Ciclo For anidado para comparar los caracteres de forma diagonal:

```
for fila in range(len(ADN)-3): #Controla las diagonales
    for columna in range(len(ADN[0])-3):
```

Indicamos la longitud del recorrido de cada FOR, y nos posicionamos en el punto de conexión de fila y columna que indiquemos. Asi vamos comparando cada elemento con el siguiente en una diagonal de tipo descendente:

```
if ADN[fila][columna] == ADN[fila+1][columna+1] == ADN[fila+2][columna+2] == ADN[fila+3][columna+3]:
    secuencia = secuencia + 1
    if secuencia > 1:
        return True
```

Si hasta éste punto tampoco se a retornado un TRUE, se ingresará al siguiente FOR anidado, el cual también es el último ciclo comparativo. Es igual que el FOR anidado anterior pero compara los elementos de forma diagonal de tipo ascendente:

```
for fila in range(len(ADN)-3): #Controla las diagonales inversas
    for columna in range(3, len(ADN[0])):
        if ADN[fila][columna] == ADN[fila+1][columna-1] == ADN[fila+2][columna-2] == ADN[fila+3][columna-3]:
            secuencia = secuencia + 1
            if secuencia > 1:
                return True
```

Si después de recorrer cada Ciclo For, tanto simple como anidado, no se devolvió un TRUE, entonces no se cumplió con ninguna condición y la función retornará un FALSE demostrando que no hay más de una secuencias de ningún tipo(horizontal, vertical o diagonal) que tenga 4 o más carácteres iguales de forma consecutiva.

Una vez ya definido cada paso a recorrer dentro de la función esMutante(), se la llama, se le brinda el arreglo que ingreso el usuario como parámetro y el resultado que retorne(en éste caso TRUE o FALSE) se almacenará en una variable:

```
es_Mutante = esMutante(ADN)
```

Finalmente, con un condicional IF, validamos el valor de la variable es_Mutante. Si contiene un TRUE, se mostrará por consola un mensaje diciendo que efectivamente es un mutante. Si contiene un FALSE, se mostrará otro mensaje informando que no es mutante:

```
print("----El resultado obtenido es el siguiente----")
if es_Mutante:
    print("Es mutante")
else:
    print("No es mutante")
```

Este sería el paso a paso que se utilizó para resolver el proyecto.

## Como correrlo

Se pueden ingresar los siguientes casos para comprobar si funciona:

Caso 1:
```
ADN = ["AAAAAA","ACTGAC","CTGGGG","TCGAAT","ATATAT","TGCTGC"]
#Es mutante, se cumple de forma horizontal
```
Caso 2:
```
ADN = ["AATAAT","ACTAAC","CTGAGC","TCGAAC","ATATAC","TGCTGT"]
#Es mutante, se cumple de forma vertical
```
Caso 3:
```
ADN = ["GATAAA","AGTAAC","CTGAGT","TCTGAC","ATATAC","TGCTTT"]
#Es mutante, se cumple de forma diagonal descendente
```
Caso 4:
```
ADN = ["CATTAT","AGTAAC","CTGAGA","TCTGAC","ATAAAC","TGATTT"]
#Es mutante, se cumple de forma diagonal ascendente
```
Caso 5:
```
ADN = ["CATTAT","AGTAAC","CTGAGA","TCTTAC","ATGGGG","TGATTT"]
#Es mutante, se cumple de forma horizontal y diagonal ascendente
```
Caso 6:
```
ADN = ["TATTAT","AGTAAC","ATGAGA","ACTTAC","ATGTGG","TGATTT"]
#Es mutante, se cumple de forma vertical y diagonal descendente
```
Caso 7:
```
ADN = ["TATTAT","AGTAAC","ATGAGA","GCTTAC","ATGCGG","TGATTT"]
#No es mutante, no se cumple de forma horizontal, vertical ni diagonal
```