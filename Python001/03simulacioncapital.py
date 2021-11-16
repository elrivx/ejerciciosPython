# Éste ejercicio servirá para explicar de forma sencilla el funcionamiento
# de la función Range en Python.
# Range, como su nombre lo indica, sirve para establecer un límite acotado.
# ¿Existe una función que sea vea beneficiada con Range? Si. El Bucle For

# Ejercicio: Luego de muchos años, una comunidad decide invertir una cantidad de ahorros
# en el banco. El banco tiene por política mostrarle a sus clientes una simulación
# que explique como su capital va a aumentar, en base a la tasa de Interés
# y una cantidad de años. El problema es que el computador que cargaba
# dicho programa está en mantención, y como los ejecutivos no tienen un plan B,
# nos llamaron para crear una solución computacional de emergencia

# Primer paso: Pedir los datos

capital = float(input("Ingrese la cantidad a invertir $: "))
tasaInteres = float(input("Ingrese la tasa de interés (%): "))
anhosSimulacion = int(input("Ingrese la cantidad de años a simular: "))

# Es en éste preciso momento donde Range, acompañado de un bucle For, deben entrar en acción.
# Existen tres formas de usarlo: en base a un sólo número "for i in range(x)", entregando
# un rango entre dos números "for i in range(x,y)" y entregar un rango de 2 números, 
# añadiendo además la cantidad de pasos en la que debe seguir la secuencia
# "for i in range(x,y,z)".
# Como éste es un problema que tiene como un sólo parámetro los años, usaremos la
# primera forma de usar la función Range

for i in range(anhosSimulacion):
  # La fórmula que usa el banco para obtener el capital es: capital = capital * (1 * interés/100)
  capital *= 1 + tasaInteres / 100
  # Ahora, mostraremos por pantalla la simulación del capital. El resultado
  # de la fórmula dará un número con infinitos decimales. Para facilitar la lectura,
  # sólamente mostraremos 2 decimales.
  print("Capital tras {} años: ${}".format(i + 1, round(capital, 2)))    
