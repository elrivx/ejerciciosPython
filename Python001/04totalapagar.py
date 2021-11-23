# Hemos visto ejercicios donde tenemos rangos para actuar. Eso está bien.
# Ahora bien, ¿qué pasaría si no tenemos claro dicho límite de acción,
# pero sabemos que debe darse una condición?
# Existe en programación (no depende del lenguaje) un bucle que sirve para responder esa pregunta:
# El Bucle While. Éste bucle tiene por finalidad repetir un bloque de código
# mientras la condición que le proporcionemos sea verdadera.
# Nota: While admite condiciones afirmativas y negativas, pero siempre pregunta si dicha
# condición se cumple.
# 
#  Ejercicio 04: Corbatas Migue está realizando una buena oferta. Cada corbata para
#  ejecutivos y ejecutivas tiene un valor de US$11. Si un cliente decidiera llevar más
#  de dichas corbatas, se le aplicará un 10% de descuento si el total de su compra es
#  superior a US$20. El dueño de Corbatas Migue nos pidió realizar una solución
#  que logre hacerlo. Además nos dio otra tarea. No debe el programa aceptar valores
#  negativos. Tampoco debe aceptar valores que no
#  sean los de una sola corbata. El programa se detendrá si se ingresa el monto 0. 

# Empecemos a programar. Ya en el ejercicio aparecen dos variables que serán nuestras
# protagonistas: el total a pagar y el monto de la compra. Declarémoslas:

totalCompra = 0  # Python puede aceptar valores sin declarar su tipo. Por ejemplo, si a un
# entero se le suma un decimal, Python asume que ese dicha variable es X.00
montoAcumulado = float(input("Ingrese el monto (US$11 mín.): US$"))

# Existen muchas formas de programar algo. Partamos por la simple. La aplicación no debe
# admitir valores negativos y además, terminar si
# el monto es igual a 0. La mejor forma de proguntarlo es con While:

while montoAcumulado  != 0:
    if montoAcumulado < 11:
        print("El monto es inválido.")
    else:
        # Si la condición anterior no es así, sumamos precios: 
        totalCompra += montoAcumulado
    # Y pedimos otro monto:
    montoAcumulado = float(input("Ingrese el monto (US$11 mín.): US$"))
# Recordemos que se debe aplicar un descuento si el total es superior a US$20:    
if totalCompra > 20:
    totalCompra -= totalCompra * 0.1
# Una vez decidimos terminar la petición de montos, imprimimos el total
# y le damos formato de 2 decimales en pantalla:
print("Total: US${:.2f}".format(totalCompra))
