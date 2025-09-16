# CASO 1
titulos = []      # lista para nombres de libros
ejemplares = []   # lista para cantidades
agotados = [] #lista de agotados
decision = 0
while decision != 9:
    print("BIENVENIDO AL MENU DE LA BIBLIOTECA ESCOLAR\n"
        "OPCIONES:\n"
        "1: INGRESAR LISTADO DE LIBROS\n"
        "2: INGRESAR LISTADO DE EJEMPLARES DISPONIBLES\n"
        "3: VER CATALOGO EN STOCK\n"
        "4: CONSULTAR DISPONIBILIDAD DE UN TITULO ESPECIFICO\n"
        "5: VER CATALOGO DE AGOTADOS\n"
        "6: AGREGAR TITULO\n"
        "7: ACTUALIZAR CATALOGO\n"
        "8: VER CATALOGO COMPLETO\n"
        "9: SALIR\n"
        )
    decision=int(input("QUE DESEA HACER: "))
    if decision in range(0,10):
        if decision == 1:
            print("")
            cantidad = int(input("¿CUANTOS TITULOS QUIERE INGRESAR?: "))
            for i in range(cantidad):
                titulo = input(f"INGRESE EL TÍTULO {i+1}: ")
                if titulo.strip() != "":  # evita vacío o solo espacios
                    titulo = titulo.upper()
                    titulos.append(titulo)
                else:
                    print("ERROR: TITULO VACÍO. VUELVA A INGRESAR.")
            print("")
        elif decision == 2:
            print("")
            if titulos:
                for i in range(len(titulos)):
                    ejemplar = int(input(f"INGRESE LA CANTIDAD DE COPIAS DISPONIBLES PARA {titulos[i]}: "))
                    ejemplares.append(ejemplar)
                    if ejemplar == 0:
                        agotados.append(titulos[i])

            else:
                print("ERROR: LISTA VACÍA INGRESE TITULOS ANTES")
            print("")
        elif decision == 3:
            print("")
            print("--------------------STOCK--------------------")
            for i in range(len(titulos)):
                if ejemplares[i]>0:
                    print(f"{titulos[i]}: {ejemplares[i]} COPIAS")
            print("---------------------------------------------")
            print("")
        elif decision == 4:
            print("")
            busqueda = input("INGRESE EL NOMBRE DEL TITULO BUSCADO: ")
            busqueda = busqueda.upper()
            if busqueda in titulos:
                posicion = titulos.index(busqueda)
                print(f"LA CANTIDAD DE COPIAS DE {titulos[posicion]} ES {ejemplares[posicion]}")
            else:
                print("ERROR: TITULO NO ENCONTRADO")
        elif decision == 5:
            print("--------------------AGOTADOS--------------------")
            for i in range(len(agotados)):
                print(f"{i+1}: {agotados[i]}")
            print("------------------------------------------------")

        # AGREGAR NUEVO LIBRO AL CATALOGO
        elif decision == 6:
            print("")
            nuevo_titulo=input("INGRESE EL NOMBRE DEL NUEVO TITULO: ")
            nuevo_titulo=nuevo_titulo.upper()
            #REVISAR QUE NO ESTE REPETIDO EL TITULO
            if nuevo_titulo in titulos:
                print("ERROR: ESE LIBRO YA SE ENCUENTRA EN EL CATALOGO:")
            else:
                print("")
                copias_nuevo_titulo=int(input(f"INGRESE LAS COPIAS {nuevo_titulo}: "))
                titulos.append(nuevo_titulo)
                ejemplares.append(copias_nuevo_titulo)
                if copias_nuevo_titulo == 0:
                    agotados.append(nuevo_titulo)
            print("")
        #PRESTAMO/DEVOLUCION
        elif decision == 7:
            print("")
            prestamo_devolucion = input("¿QUÉ DESEA HACER?\n1: PRESTAMO\n2: DEVOLUCIÓN\nSeleccione: ")

            if prestamo_devolucion == "1":  # PRESTAMO
                busqueda = input("INGRESE EL NOMBRE DEL TITULO A PRESTAR: ")
                busqueda = busqueda.upper()
                if busqueda in titulos:
                    posicion = titulos.index(busqueda)
                    if ejemplares[posicion] > 0:
                        ejemplares[posicion] -= 1
                        print(f"SE PRESTÓ {busqueda}. QUEDAN {ejemplares[posicion]} COPIAS.")
                        if ejemplares[posicion] == 0 and titulos[posicion] not in agotados:
                            agotados.append(titulos[posicion])
                    else:                                                                       
                        print(f"NO HAY COPIAS DISPONIBLES DE {busqueda}.")
                else:
                    print("ERROR: TITULO NO ENCONTRADO.")

            elif prestamo_devolucion == "2":  # DEVOLUCIÓN
                busqueda = input("INGRESE EL NOMBRE DEL TITULO A DEVOLVER: ")
                total_a_devolver=int(input("INGRESE LA CANTIDAD DE LIBROS A DEVOLVER: "))
                if total_a_devolver > 0:
                    busqueda = busqueda.upper()
                    if busqueda in titulos:
                        posicion = titulos.index(busqueda)
                        ejemplares[posicion] += total_a_devolver
                        print(f"SE DEVOLVIÓ {busqueda}. AHORA HAY {ejemplares[posicion]} COPIAS.")
                        # si estaba en agotados y ahora tiene stock, lo saco
                        if ejemplares[posicion] > 0 and titulos[posicion] in agotados:
                            agotados.remove(titulos[posicion])
                    else:
                        print("ERROR: TITULO NO ENCONTRADO.")
                else:
                    print("ERROR: LA CANTIDAD A DEVOLVER DEBE SER MAYOR A 0.")
        # CATALOGO COMPLETO
        elif decision == 8:
            print("")
            print("--------------------CATALOGO--------------------")
            for i in range(len(titulos)):
                print(f"{titulos[i]}")
            catalogo_cantidad=(len(titulos))
            print("------------------------------------------------")
            print("")
    else:
        print("ERROR: FUERA DE LAS OPCIONES POSIBLES")