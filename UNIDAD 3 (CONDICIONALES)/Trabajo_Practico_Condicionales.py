# EJERCICIO 1
edad = int(input("INGRESE SU EDAD: "))
if edad > 18:
    print("ES MAYOR DE EDAD")

# EJERCICIO 2

nota = int(input("INGRESE SU NOTA: "))
if nota >= 6:
    print("APROBADO")
else:
    print("DESAPROBADO")

# EJERCICIO 3

numero = int(input("INGRESE UN NUMERO PAR: "))
par = numero % 2 
if par == 0:
    print("HA INGRESADO UN NUMERO PAR")
else:
    print("PORFAVOR INGRESE UN NUMERO PAR")

# EJERCICIO 4

edad = int(input("INGRESE SU EDAD: "))
if edad < 12:
    print("NIÑO/A")
elif edad >= 12 and edad < 18:
    print("ADOLESCENTE")
elif edad >= 18 and edad < 30:
    print("ADULTO/A JOVEN")
else:
    print("ADULTO/A")

# EJERCICIO 5
contrasena = input("INGRESE UNA CONTRASEÑA: ")
validar_contrasena = len(contrasena)
if validar_contrasena >=8 and validar_contrasena <=14:
    print("HA INGRESADO UNA CONTRASEÑA CORRECTA")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# EJERCICIO 6



# EJERCICIO 7

frase = input("INGRESE UNA FRASE: ")
frase = frase.lower()
if frase[-1] in "aeiou":
    frase += "!"
    print(frase)

# EJERCICIO 8

print("PRESIONE 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO." )
print("PRESIONE 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. ")
print("PRESIONE 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")
modo=int(input("SELECIONE EL MODO: 1/2/3: "))

nombre = input("INGRESE SU NOMBRE: ")

if modo == 1:
    nombre=nombre.upper()
elif modo == 2:
    nombre=nombre.lower()
elif modo == 3:
    nombre=nombre.title()
print(nombre)

# EJERCICIO 9

terremoto=int(input("INGRESE LA MAGNITUD DEL TERREMOTO: "))
if terremoto < 3:
    print("MUY LEVE(Impercetible)")
elif terremoto >= 3 and terremoto < 4:
    print("LEVE(Ligeramente perceptible)")
elif terremoto >= 4 and terremoto < 5:
    print("MODERADO (sentido por personas, pero generalmente no causa daños).")
elif terremoto >= 5 and terremoto < 6:
    print("FUERTE (puede causar daños en estructuras débiles).")
elif terremoto >= 6 and terremoto < 7:
    print("MUY FUERTE (puede causar daños significativos). ")
else:
    print("EXTREMO(puede causar graves daños a gran escala)")

# EJERCICIO 10
mes = int(input("INGRESE EL NUMERO DEL MES QUE SE ENCUENTRA: "))
dia = int(input("QUE DIA DEL MES ES: "))
hemisferio = input("EN QUE HEMISFERIO SE ENCUENTRA: NORTE/SUR ")
hemisferio=hemisferio.capitalize()
if hemisferio == "Norte":
    if (mes == 12 and dia >= 21) or (mes <= 3 and (mes < 3 or (mes == 3 and dia <= 20))):
            print ("Invierno")
    elif (mes == 3 and dia >= 21) or (mes <= 6 and (mes < 6 or (mes == 6 and dia <= 20))):
            print ("Primavera")
    elif (mes == 6 and dia >= 21) or (mes <= 9 and (mes < 9 or (mes == 9 and dia <= 20))):
            print ("Verano")
    else:  
            print("Otoño")
if hemisferio == "Sur":
    if (mes == 12 and dia >= 21) or (mes <= 3 and (mes < 3 or (mes == 3 and dia <= 20))):
            print ("Verano")
    elif (mes == 3 and dia >= 21) or (mes <= 6 and (mes < 6 or (mes == 6 and dia <= 20))):
            print ("Otoño")
    elif (mes == 6 and dia >= 21) or (mes <= 9 and (mes < 9 or (mes == 9 and dia <= 20))):
            print ("Invierno")
    else:  
            print("Primavera")




