# Los Vectores son una buena forma de guardar variables, pero tienen
# un problema. Entran en funcionamiento una vez que se ejecuta
# la aplicación y cuando ésta termina, sus datos quedan inaccesibles.

# Ya en los principios de la Informática, los desarrolladores
# buscaron formas de "retener" esos datos con el fin de acceder
# a ellos en un futuro. Desde Tarjetas Perforadas hasta
# Almacenamiento en la Nube. Todo sirve.

# En los lenguajes de programación existe el concepto de Manipulación
# de Ficheros (Archivos). Cada fichero puede contar una cantidad de datos
# y éstos datos pueden ser leídos, modiificados o eliminados, además
# de ingresar nuevos datos, en caso de ser necesario.
#
# Ejercicio 07: Estábamos descansando cuando recibimos la visita de los
# Duendes de Santa (San Nicolás, El Viejo Pacuero, Papá Noel, etc), muy
# nerviosos y asustados. Se acerca la Navidad y deben dejar preparado
# todo para la fecha importante. Santa les dejó en un archivo separado
# por comas (cvs) la lista de niñas y niños del mundo, con lo que van a recibir.
# Eso suena bello, si no fuera por un detalle. ¡Los duendes no cuentan con
# una forma de leer el archivo! Para no sentirse nerviosos, nos
# pidieron que creemos una aplicación donde ellos puedan escribir un nombre,
# esa aplicación haga la consulta al fichero y les devuelva
# si éste año va a recibir un obsequio o carbón.

# Empecemos a trabajar. En Python, existen 4 métodos para tratamiento
# de archivos: "Open", "Read", "Write" y "Close". Usémos el primero.
# No sin antes importar la librería csv:

import csv

lista = 'lista.csv'

# Abrimos el fichero:
with open(lista, newline='', encoding='utf-8') as f:
    # Ahora, pedimos el nombre:
    consulta = input("Ingrese el nombre de la Niña o el Niño: ")
    next(f, None)  # Esto sirve para que no cuente el encabezado como dato
    datos = csv.reader(f, delimiter=',',
                       quotechar=';')  # Decimos que la separación es una coma

    # Haremos esto en cada fila del archivo
    for fila in datos:
        nombre = fila[0]
        recibe = fila[1]
        # Si el nombre está en la lista, mostramos el mensaje:
        if consulta == nombre:
            print(f"A {nombre} le corresponde: {recibe}.")
