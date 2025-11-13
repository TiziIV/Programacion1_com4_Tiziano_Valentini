# ============================================================
# EJERCICIO 1: Factorial de un número (recursivo)
# ============================================================

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Mostrar los factoriales desde 1 hasta el número indicado por el usuario
num = int(input("Ingrese un número: "))
for i in range(1, num + 1):
    print(f"Factorial de {i} = {factorial(i)}")


# ============================================================
# EJERCICIO 2: Serie de Fibonacci (recursivo)
# ============================================================

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Mostrar la serie hasta la posición indicada
n = int(input("\nIngrese la posición hasta la que desea ver la serie de Fibonacci: "))
print("Serie de Fibonacci:")
for i in range(n):
    print(fibonacci(i), end=" ")
print()


# ============================================================
# EJERCICIO 3: Potencia recursiva (n^m)
# ============================================================

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = int(input("\nIngrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(f"{base}^{exponente} = {potencia(base, exponente)}")


# ============================================================
# EJERCICIO 4: Conversión decimal a binario (recursivo)
# ============================================================

def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

num = int(input("\nIngrese un número decimal: "))
binario = decimal_a_binario(num)
print(f"El número {num} en binario es: {binario if binario else '0'}")


# ============================================================
# EJERCICIO 5: Verificar si una palabra es palíndromo (recursivo)
# ============================================================

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

palabra = input("\nIngrese una palabra: ").lower()
if es_palindromo(palabra):
    print(f"{palabra} es un palíndromo")
else:
    print(f"{palabra} no es un palíndromo")


# ============================================================
# EJERCICIO 6: Suma de dígitos de un número (recursivo)
# ============================================================

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)

n = int(input("\nIngrese un número entero positivo: "))
print(f"La suma de los dígitos de {n} es {suma_digitos(n)}")


# ============================================================
# EJERCICIO 7: Pirámide de bloques (recursivo)
# ============================================================

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

niveles = int(input("\nIngrese la cantidad de bloques en el nivel más bajo: "))
print(f"Total de bloques necesarios: {contar_bloques(niveles)}")


# ============================================================
# EJERCICIO 8: Contar ocurrencias de un dígito en un número (recursivo)
# ============================================================

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

numero = int(input("\nIngrese un número entero positivo: "))
digito = int(input("Ingrese un dígito (0-9): "))
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en {numero}")
