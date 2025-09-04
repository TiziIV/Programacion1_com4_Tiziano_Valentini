# EJERCICIO 1
for i in range (0,101):
    print(i)

# EJERCICIO 2
print("")
numero = int(input("Ingrese un número entero: "))
n = abs(numero)
contador = 0
if n == 0:
    contador = 1
else:
    while n > 0:
        n = n // 10 
        contador += 1  
print(f"El número tiene {contador} dígitos.")

# EJERCICIO 3
print("")
valor_uno = int(input("INGRESE EL PRIMERO VALOR: "))
valor_dos = int(input("INGRESE EL SEGUNDO VALOR: "))
suma=0
numeros_sumados = valor_uno + 1
while numeros_sumados < valor_dos:
    suma += numeros_sumados
    numeros_sumados += 1
print(f"La suma de los numeros entre {valor_uno} y {valor_dos} es {suma}")

# EJERCICIO 4
print("")
numero = int(input("INGRESE UN NUMERO: "))
suma = numero
while numero != 0:
    numero = int(input("INGRESE UN NUMERO: "))
    suma=suma+numero
print(f"La suma de todos los numeros ingresados es de: {suma}")

# EJERCICIO 5
print("")
import random
numero_aleatorio = random.randint(0,9)
numero_usuario = int(input("INGRESE UN NUMERO ENTRE 0 Y 9: "))
contador = 1
while numero_usuario != numero_aleatorio:
    numero_usuario = int(input("ESE NO ES EL NUMERO, INGRESE OTRO: "))
    contador = contador+1
print (f"!ADIVINASTE¡, EL NUMERO CORRECTO ERA {numero_aleatorio} Y LO ADIVINASTE EN EL INTENTO {contador}")

 
# EJERCICIO 6
print("")
valor_uno = 0
valor_dos = 100
suma=0
for numero in range(valor_uno, valor_dos + 1):
    suma += numero
print(f"La suma de los numeros pares entre {valor_uno} y {valor_dos} es {suma}")

# EJERCICIO 7
print("")
valor_uno = 0
valor_dos = int(input("INGRESE EL NUMERO DE CIERRE: "))
suma=0
numeros_sumados = valor_uno 
while numeros_sumados < valor_dos:
    suma += numeros_sumados
    numeros_sumados += 1
print(f"La suma de los numeros entre {valor_uno} y {valor_dos} es {suma}")

# EJERCICIO 8
print("")
numeros_pares = 0
numeros_impares = 0
numeros_positivos = 0
numeros_negativos = 0 
for i in range(0,100):
    numero=int(input("INGRESE UN NUMERO: "))
    # REVISAMOS SI ES PAR O NO
    if numero % 2 == 0:
        numeros_pares=numeros_pares+1
    else:
        numeros_impares=numeros_impares+1
    # REVISAMOS LA POSITIVIDAD
    if numero >= 0:
        numeros_positivos=numeros_positivos+1
    else:
        numeros_negativos=numeros_negativos+1
print(f"LA CANTIDAD DE NUMEROS PARES ES DE {numeros_pares}")
print(f"LA CANTIDAD DE NUMEROS IMPARES ES DE {numeros_impares}")
print(f"LA CANTIDAD DE NUMEROS POSITIVOS ES DE {numeros_positivos}")
print(f"LA CANTIDAD DE NUMEROS NEGATIVOS ES DE {numeros_negativos}")

# EJERCICIO 9
print("")
suma=0
for i in range(0,100):
    numero=int(input("INGRESE UN NUMERO: "))
    suma=suma+numero
    media=suma/100

# EJERCICIO 10
print("")
numero = int(input("INGRESE UN NUMERO: "))
numero_str = str(abs(numero)) 
numero_inverso_str = ""
for digito in numero_str:
    numero_inverso_str = digito + numero_inverso_str
numero_inverso = int(numero_inverso_str)
print(f"EL NUMERO INVERTIDO ES: {numero_inverso}")