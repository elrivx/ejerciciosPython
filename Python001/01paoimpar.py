# Ejercicio básico 01: ingresar un número y determinar si es par o impar
# Nota: en aritmética, se asume que un número es par cuando el resultado
# de su división por 2 es un número exacto. Ejemplo: 50/2=25

num = input('Ingrese un número: ')

# Para éste ejemplo, no voy a validar que lo ingresado sean números,
# pero voy a convertir num en un número entero (int) por seguridad.

num = int(num)

# Usando la definición de par escrita en la nota y para no equivocarme,
# voy a preguntar si el resto de la división del número por 2 es igual
# a 0 (lo que sería una división exacta). Para ello, voy a usar el operador
# Módulo (%)

if num % 2 == 0:
    print('El número digitado es par.')
else:
    print('El número digitado es impar.')
