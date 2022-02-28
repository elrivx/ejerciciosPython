# Vamos a importar la libería random

import random

# Intentemos traspasar ésto a una función


def alAzar(archivo1, archivo2, archivo3, archivo4, archivo5):
    articulos = []
    sujeto = []
    actividad = []
    adverbio = []
    adverbio2 = []

    # Llenando las listas vacías con los datos de los archivos
    for a in archivo1:
        articulos.append(a.strip())

    for b in archivo2:
        sujeto.append(b.strip())

    for c in archivo3:
        actividad.append(c.strip())

    for d in archivo4:
        adverbio.append(d.strip())

    for e in archivo5:
        adverbio2.append(e.strip())

    # Ahora, seleccionaremos un dato al azar de cada lista
    azarArticulo = random.choice(articulos)
    azarSujeto = random.choice(sujeto)
    azarActividad = random.choice(actividad)
    azarAdvervio = random.choice(adverbio)
    azarAdverbio2 = random.choice(adverbio2)

    # Imprimir el resultado
    print(azarArticulo, azarSujeto, "que", azarActividad,
          ". Es", azarAdvervio, "y además", azarAdverbio2, ".")
