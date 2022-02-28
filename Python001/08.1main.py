# Vamos a importar la función que creamos en en archivo funciones.py

from 08.1funciones import alAzar


# Vamos a abrir los archivos

archivo1 = open("01articulos.txt")
archivo2 = open("02sujetos.txt")
archivo3 = open("03actividad.txt")
archivo4 = open("04adverbio.txt")
archivo5 = open("05adverbio2.txt")

# Por último, llamaremos a la función alAzar para que nos ayude

alAzar(archivo1, archivo2, archivo3, archivo4, archivo5)
