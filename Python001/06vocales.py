# Al pasar el tiempo, las personas que trabajan en programación
# se dieron cuenta de que mientras más variables creaban,
# más recursos iban generando. Si tenemos variables similares
# y que signifiquen para nosotros lo mismo, ¿no sería
# mejor encontrar una forma de agruparlas en un sólo
# lugar?

# La respuesta vino desde las matemáticas. Notaron
# de que las matrices podían almacenar muchos datos en un
# sólo lugar. Para no complicar las cosas, se fijaron en
# la Matriz Unidimensional y la bautizaron como Vector (Array
# en inglés).

# Donde más útiles son los vectores son en aquellas situaciones donde
# no tenemos muy claro el orden en el que están los datos.

# Ejercicio 06: Quedó tan feliz la Rectora de la Escuela Primaria Los Patitos
# Felices que nos pidió algo más lúdico pero educativo. En una ronda de inspección,
# ella se dio cuenta de que los alumnos y alumnas no podían contar las vocales
# contenidas en una palabra. Es el momento de que la ayudemos.

palabra = input("Escribe una palabra: ")
vocales = ['a', 'e', 'i', 'o', 'u']
for vocal in vocales:
    veces = 0
    for letra in palabra:
        if letra == vocal:
            veces += 1
    print("La vocal " + vocal + " aparece " + str(veces) + " veces.")
