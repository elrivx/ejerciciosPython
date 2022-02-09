# Lo primero es importar la librería random. Nos servirá mucho


import random

# Es momento del plan. Lo mejor para hacer selecciones al azar, es con listas.
# Hagámoslas:

articulos = []
sujeto = []
actividad = []
adverbio = []
adverbio2 = []

# Tenemos que llenar las listas. Comencemos:

archivo1 = open("01articulos.txt")
archivo2 = open("02sujetos.txt")
archivo3 = open("03actividad.txt")
archivo4 = open("04adverbio.txt")
archivo5 = open("05adverbio2.txt")

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

# ¿Se acuerdan que dije que importaríamos la libería random? Bueno,
# es tiempo de usarla. Haremos variables que guarden al azar:

azarArticulo = random.choice(articulos)
azarSujeto = random.choice(sujeto)
azarActividad = random.choice(actividad)
azarAdvervio = random.choice(adverbio)
azarAdverbio2 = random.choice(adverbio2)

# Y ahora, la inspiración llegará:

print(azarArticulo, azarSujeto, "que", azarActividad,
      ". Es", azarAdvervio, "y además", azarAdverbio2, ".")
