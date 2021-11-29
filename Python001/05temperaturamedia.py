# La programación fue evolucionando con el paso del tiempo.
# Ates, no había problemas si se escribía muchas veces
# un código y se ejecutaba.

# Con el paso del tiempo, nos fuimos dando cuenta de que ésta práctica
# no sólo es tediosa, sino que además generaba un gasto de recursos
# (máquina, compilación, etc.) innecesarios.

# Así como los propios lenguajes de programación tienen un grupo
# de funciones preestablecidas para su uso, nosotros también
# podemos crear algunas. Se suele decir que las funciones
# "encapsulan" una parte del código del resto del programa.

# Ejercicio 05: La Rectora de la Escuela Primaria Los Cuackitos Felices está
# preocupada de las temperaturas del día. Niños y Niñas salen
# a sus respectivos recreos y a temperaturas muy altas o muy bajas,
# se pueden enfermar. Ella nos pidió un programa que le entregue la
# Temperatura Media de un día, nutriéndolo de la temperatura mínima
# y máxima, con el fin de estudiarlas y tomar decisiones. Además,
# nos dijo que el programa debe mostrar los resultados, en base a días que
# pidamos.

# Empecemos a programar. Ya sabemos que la media se obtiene dividiendo
# por 2 la suma de dos valores. Creemeos una función para ello.
# Nota: Las funciones en Python tienen la siguiente estructura
# def nombreFuncion(loQueVaARecibir):
#   loQueVaAHacer
#   loQueDevolvera

def temperaturaMedia(tMin, tMax):
    return (tMin + tMax) / 2


# Ahora, pidamos al usuario el número de temperaturas a calcular
cuantasTemperaturas = int(input("Ingrese las temperaturas a calcular: "))

# ¿Cómo aseguramos que se ejecutará las veces que necesitamos?
# Adivinaron. Con un bucle For y con nuestro amigo Range
for x in range(cuantasTemperaturas):
    tMin = float(input("Ingrese la temperatura mínima: "))
    tMax = float(input("Ingrese la temperatura máxima: "))
    # Por último, llamamos a la función. En éste caso,
    # lo haremos dentro del Print. ¿Se podría hacer dentro
    # de una variable? Si. No lo hice aquí,
    # para obtener el resultado de inmediato.
    print("La Temperatura Media fue de {} grados.".format(
        temperaturaMedia(tMin, tMax)))
