# EJERCICIO 1
def imprimir_hola_mundo():
    print("HOLA MUNDO")
imprimir_hola_mundo()
print("")

# EJERCICIO 2
def saludar_usuario(usuario):
    print(f"Hola {usuario}")
    return usuario
usuario=input("INGRESE SU NOMBRE: ")
saludar_usuario(usuario)
print("")

# EJERCICIO 3
def informacion_personal(nom, apell, edad, res):
    print(f"Soy {nom} {apell}, tengo {edad} años y vivo en {res}")
nombre=input("INGRESE SU NOMBRE: ")
apellido=input("INGRESE SU APELLIDO: ")
edad=int(input("INGRESE SU EDAD: "))
residencia=input("INGRESE SU RESIDENCIA: ")
informacion_personal(nombre,apellido,edad,residencia)
print("")

# EJERCICIO 4
import math
def calcular_area_circulo(rad):
    print(math.pi * (rad ** 2))
def calcular_perimetro_circulo(rad):
    print(math.pi*2*rad )
radio=int(input("INGRESE EL RADIO: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)
print("")

# EJERCICIO 5
def segundos_a_horas(seg):
    print(f"{seg} SEGUNDOS PASADO A HORAS ES ",seg/3600)
segundos=int(input("INGRESE LOS SEGUNDOS: "))
segundos_a_horas(segundos)
print("")

# EJERCICIO 6
def tabla_multiplicar(num):
    for i in range(1,11):
        print(f"{num} * {i}=",num*i)
numero=int(input("INGRESE EL NUMERO A MULTIPLICAR: "))
tabla_multiplicar(numero)
print("")

# EJERCICIO 7
def operaciones_basicas(a,b):
    suma=a+b
    resta=a-b
    mult=a*b
    div=a/b
    return(suma,resta,mult,div)
primer_num=(int(input("INGRESE EL NUMERO: ")))
segundo_num=(int(input("INGRESE EL OTRO NUMERO: ")))
resultados=operaciones_basicas(primer_num,segundo_num)
print(f"SUMA: {resultados[0]}")
print(f"RESTA: {resultados[1]}")
print(f"MULTIPLICACION: {resultados[2]}")
print(f"DIVISION: {resultados[3]}")
print("")

# EJERCICIO 8
def calcular_imc(pes,alt):
    alt=alt/100
    imc=pes/(alt**2)
    print(imc)
peso=int(input("INGRESE SU PESO EN KG: "))
altura=int(input("INGRESE SU ALTURA EN CENTIMETROS: "))
calcular_imc(peso,altura)
print("")

# EJERCICIO 9
def celsius_a_fahrenheit(cels):
    fahrenheit=(cels * 9/5) + 32
    return fahrenheit
celsius=float(input("INGRESE LA TEMPERATURA EN GRADOS: "))
fahr=celsius_a_fahrenheit(celsius)
print(fahr)
print("")

# EJERCICIO 10
def calcular_promedio(a, b, c):
    promedio=(a+b+c)/3
    print(promedio)
notas=[]
for i in range(0,3):
    nota=int(input("INGRESE LA NOTA: "))
    notas.append(nota)
calcular_promedio(notas[0],notas[1],notas[2])




    
