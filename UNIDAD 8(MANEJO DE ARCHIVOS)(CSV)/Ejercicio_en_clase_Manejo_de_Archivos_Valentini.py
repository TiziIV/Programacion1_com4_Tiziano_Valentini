import csv
import os

#=========FUNCIONES==========

def inicializar_archivo():
    if not os.path.exists("productos.csv"):
        with open("productos.csv", "w", encoding="UTF-8", newline="") as archivo:
            encabezado=["Nombre","Precio"]
            escritor = csv.DictWriter(archivo, fieldnames=encabezado)
            escritor.writeheader()

def cargar_productos():
    try:
        productos=[]
        with open("productos.csv", "r") as archivo:
            lector = csv.DictReader(archivo, fieldnames=["Nombre","Precio"])
            for fila in lector:
                    try:
                        fila['Precio'] = float(fila['Precio'])
                        productos.append(fila)
                    except ValueError:
                        pass
        return productos 
    except FileNotFoundError:
        print("ERROR: EL ARCHIVO NO EXISTE")

def mostrar_productos():
    try:
        productos_mostrar = cargar_productos()
        total=0
        if not productos_mostrar:
            print("NO HAY PRODUCTOS")
        else:
            for prod in productos_mostrar:
                print(f"PRODUCTO: {prod['Nombre']} - PRECIO: ${prod['Precio']}")
                total += prod['Precio']
        print(f"El total acumulado es de {total}")
    except FileNotFoundError:
        print("ERROR")

def agregar_productos():
    try: 
            while True:
                try:
                    nombre=input("INGRESE EL NOMBRE DEL PRODUCTO: ").strip().capitalize()
                    if nombre == "":
                        print("EL NOMBRE NO PUEDE ESTAR VACIO.")
                        raise ValueError
                    precio=float(input("INGRESE EL PRECIO DEL PRODUCTO: "))
                    print("PRODUCTO AGREGADO CORRECTAMENTE.")
                    with open("productos.csv", "a", encoding="UTF-8", newline = "") as archivo:
                        escritor = csv.DictWriter(archivo, fieldnames=['Nombre','Precio'])
                        escritor.writerow({'Nombre':nombre, 'Precio':precio})
                        break
                except ValueError:
                    print("EL VALOR DEL PRECIO DEBE SER UN NUMERO. Y EL NOMBRE NO PUEDE ESTAR VACIO.")
    except FileNotFoundError:
        print("EL ARCHIVO NO EXISTE")

def eliminar_producto():
    productos_nuevos = []
    productos = cargar_productos()
    a_eliminar = input("INGRESE EL NOMBRE DEL PRODUCTO A ELIMINAR: ").strip().capitalize()
    for prod in productos:
        if a_eliminar != prod['Nombre'].capitalize():
            productos_nuevos.append(prod)
        else:
            print("PRODUCTO ELIMINADO")
    try:
        with open("productos.csv", "w", encoding="UTF-8", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=['Nombre', 'Precio'])
            escritor.writeheader()
            escritor.writerows(productos_nuevos)
    except FileNotFoundError:
        print("⚠️ EL ARCHIVO NO EXISTE")


def actualizar_producto():
    productos = cargar_productos()
    a_actualizar = input("INGRESE EL NOMBRE DEL PRODUCTO PARA ACTUALIZAR: ").strip().capitalize()
    actualizado=False
    for prod in productos:
        if a_actualizar == prod['Nombre'].capitalize():
            try: 
                precio_nuevo=float(input("INGRESE EL PRECIO DEL PRODUCTO: "))
                prod['Precio'] = precio_nuevo 
                actualizado=True
                print(f"✅ Precio de '{a_actualizar}' actualizado correctamente.")
            except ValueError:
                print("EL PRECIO DEBE SER UN NUMERO.")
                break
    if not actualizado:
        print("EL PRODUCTO NO EXISTE")
    try:
        with open("productos.csv", "w", encoding="UTF-8", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=['Nombre', 'Precio'])
            escritor.writeheader()
            escritor.writerows(productos)
    except FileNotFoundError:
        print("⚠️ EL ARCHIVO NO EXISTE")



#=====MENU PRINCIPAL======

def main():
    inicializar_archivo()
    while True:
        try:
            print("")
            print("============MENU PRINCIPAL==========")
            print("1. MOSTRAR PRODUCTOS")
            print("2. AGREGAR UN NUEVO PRODUCTO")
            print("3. ELIMINAR UN PRODUCTO")
            print("4. ACTUALIZAR PRECIO")
            print("5. SALIR DEL PROGRAMA")
            print("=====================================")
            print("")

            opcion=int(input("INGRESE LA OPCION QUE DESEA REALIZAR: "))

            match opcion:
                case 1:
                    mostrar_productos()
                case 2:
                    agregar_productos()
                case 3:
                    eliminar_producto()
                case 4:
                    actualizar_producto()
                case 5:
                    print("HASTA LUEGO!")
                    break
                case _:
                    print("INGRESE UNA OPCION VALIDA.")
        except ValueError:
            print("ERROR. TIENE QUE INGRESAR UN NUMERO ENTERO")

if __name__ == "__main__":
    main()
    