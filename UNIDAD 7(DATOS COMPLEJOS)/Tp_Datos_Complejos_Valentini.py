# EJERCICIO 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precios_frutas['Naranja']=1200
precios_frutas['Manzana']=1500
precios_frutas['Pera']=2300

# EJERCICIO 2

precios_frutas['Banana']=1330
precios_frutas['Manzana']=1700
precios_frutas['Melon']=2800

# EJERCICIO 3
frutas=list(precios_frutas.keys())

# EJERCICIO 4
contactos=[]
for i in range (1):
    nombre=input("INGRESE EL NOMBRE DEL CONTACTO: ").capitalize()
    numero=int(input(f"INGRESE EL NUMERO DE TELEFONO DE {nombre}: "))
    contacto={nombre : numero}
    contactos.append(contacto)
print("")
buscar_contacto=input("INGRESE EL NOMBRE DEL CONTACTO BUSCADO: ").capitalize()
encontrado = False
for contacto in contactos:
    if buscar_contacto in contacto:
        print(f"El número de {buscar_contacto} es {contacto[buscar_contacto]}")
        encontrado = True
        break
if not encontrado:
    print(f"{buscar_contacto} no se encuentra en la lista de contactos.")
print("")

# EJERCICIO 5

frase = input("INGRESE LA FRASE: ").upper()
palabras = frase.split()
palabras_unicas=set(palabras)
recuento_palabras={}
for palabra in palabras:
    if palabra in recuento_palabras:
        recuento_palabras[palabra] += 1
    else:
        recuento_palabras[palabra]=1
print("PALABRAS UNICAS:")
print(palabras_unicas)

print("RECUENTO DE PALABRAS")
print(recuento_palabras)

# EJERCICIO 6

alumnos={}
for i in range (3):
    nombre=input("INGRESE EL NOMBRE DEL ALUMNO: ").capitalize()
    notas=()
    for j in range(3):
        nota=int(input(f"INGRESE LA NOTA {j+1} DE {nombre}: "))
        notas+=(nota,)
    alumnos[nombre] = notas
print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio}")

# EJERCICIO 7

parcial1 = {"Ana", "Juan", "Tizi", "Lucas"}
parcial2 = {"Juan", "Sofía", "Tizi", "Martín"}

ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos)

solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno de los dos:", solo_uno)

al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)

print("")
# EJERCICIO 8

productos={
    "manzana": 120,
    "banana": 200,
    "pera": 180,
    "naranja": 160,
    "uva": 350,
    "tomate": 250,
    "lechuga": 100,
    "zanahoria": 140,
    "papa": 180,
    "cebolla": 150
}

print("--------------MENU--------------")
print("1: CONSULTAR STOCK \n"
"2: AGREGAR UNIDADES \n" \
"3: AGREGAR NUEVO PRODUCTO") 
print("--------------------------------")
opcion=int(input("INGRESE QUE OPCION DESEA REALIZAR: "))
match opcion: 
    case 1:
        producto_a_buscar=input("INGRESE QUE PRODUCTO DESEA BUSCAR: ").lower()
        if producto_a_buscar in productos:
            print(f"El stock de {producto_a_buscar} es {productos[producto_a_buscar]}")
    case 2:
         producto_actualizar=input("INGRESE QUE PRODUCTO DESEA ACTUALIZAR: ").lower()
         if producto_actualizar in productos:
            nuevo_stock=int(input("INGRESE EL NUEVO STOCK: "))
            productos[producto_actualizar] = nuevo_stock
    case 3:
        nuevo_producto=input("INGRESE EL NUEVO PRODUCTO: ").lower()
        stock_nuevo_producto=int(input("INGRESE EL STOCK: "))
        productos[nuevo_producto] = stock_nuevo_producto
    case _:
        print("ERROR: ESTA OPCION NO ESTA EN LOS PARAMETROS")
print("\nDiccionario final de productos:")
print(productos)

print("")

# EJERCICIO 9

agenda = {
    ("lunes", "10:00"): "Clase de Python",
    ("lunes", "14:00"): "Reunión con equipo",
    ("martes", "09:30"): "Entrega de informe",
    ("miércoles", "11:00"): "Llamada con proveedor",
    ("jueves", "16:00"): "Clase de matemáticas",
    ("viernes", "08:00"): "Correr en el parque",
    ("viernes", "15:00"): "Revisión de proyecto"
}

dia_a_buscar=input("INGRESE EL DIA A BUSCAR: ").lower()
hora_a_buscar=input("INGRESE LA HORA(CON ESTOS PARAMETROS 00:00): ")
actividad=(dia_a_buscar, hora_a_buscar)

if actividad in agenda:
    print(f"La actividad es: {agenda[actividad]}")
    
# EJERCICIO 10

paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Colombia": "Bogotá",
    "México": "Ciudad de México",
    "Perú": "Lima",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción",
    "Ecuador": "Quito",
    "Bolivia": "Sucre",
    "Venezuela": "Caracas",
    "España": "Madrid",
    "Francia": "París",
    "Italia": "Roma",
    "Alemania": "Berlín",
    "Portugal": "Lisboa",
    "Japón": "Tokio",
    "China": "Beijing",
    "India": "Nueva Delhi",
    "Australia": "Canberra"
}

nuevo_mapeo={capital: paises_capitales for paises_capitales, capital in paises_capitales.items()}
print(nuevo_mapeo)