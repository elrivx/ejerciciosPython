# El siguiente ejercicio nos hará pensar en trabajar en base a límites y la forma en la 
# debemos confrontarlos, para dar solución.

# La empresa Pescaditos S.A. hace una evaluación de desempeño a final de año. Sin
# contar su salario mensual, los trabajadores obtienen un bono, basado en los
# resultados de dicha evaluación. Necesitan un programa para agilizar el proceso.

# La tabla de puntos es la siguiente:

# Insuficiente = de 0.0 a 0.4
# Aceptable = de 0.4 a 0.6
# Extraordinario = 0.6

# Fórmula del bono: valor fijo * punto evaluación
# Valor fijo = US$ 62.98

# Determinemos la variable valorFijo

valorFijo = 62.98

# Ahora, los rangos

puntoInsuficiente = 0.0
puntoAceptable = 0.4
puntoExtraordinario = 0.6

# Necesitaremos ahora la puntuación del trabajador. Pidámosla

puntosTrabajador = float(input("Introduzca la puntuación: "))

# Nota: Como es un ejercicio básico, no vamos a validar si los puntos son
# de tipo float. Eso sí, una buena práctica sería implementar una validación.

# Debemos ahora crear la secuencia de instrucciones para la evaluación.
# Nota: Python no tiene dentro de sus operadores una intrucción equivalente a "Between",
# por lo que tocará buscar otras formas. Podríamos preguntar haciando comparaciones:

if puntosTrabajador >= puntoInsuficiente and puntosTrabajador < puntoAceptable:
  print("Resultado evaluación: Insuficiente")
  bonoFinal = valorFijo * puntoInsuficiente
  print("Bonificación total: US$", bonoFinal)
elif puntosTrabajador >= puntoAceptable and puntosTrabajador < puntoExtraordinario:
  print("Resultado evaluación: Aceptable")
  bonoFinal = valorFijo * puntoAceptable
  print("Bonificación total: US$", bonoFinal)
else:
  print("Resultado evaluación: Extraordinario")
  bonoFinal = valorFijo * puntoExtraordinario
  print("Bonificación total: US$", bonoFinal)

