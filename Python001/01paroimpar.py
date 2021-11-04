# Ejercicio básico 01: ¿Número par o impar?
# Nota: en aritmética, se asume que un número es par
# cuando el resultado de su división por '2', es un
# número exacto (entero).
# Ejemplo: 50 / 2 = 25

num = input('Ingrese un número: ')

# Como éste es un ejercicio para "calentar motores", no voy a validar si
# lo ingresado es un número o letras.
# Eso sí, para asegurarme, voy a convertir el número a entero (int)

num = int(num)

# ¿Cómo se puede averiguar si una división arroja un resultado exacto?
# Si uno divide dos números, se obtienen el Cociente y en algunos casos, el Resto.
# Cuando una división da como Cociente un número entero, significa que su resto es 0.
# Para averiguar eso, en programación existe algo llamado Módulo, representado en Python
# con el signo % .
# Si el módulo de un número X y 2 es igual a 0, significa que su resultado es
# exacto, por ende, es par.
# Eso significa que hay que preguntar

if num % 2 == 0:
  print('El resultado es par.')
else:
  print('El resultado es impar.')