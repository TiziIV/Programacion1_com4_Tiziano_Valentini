# INICIO
# INGRESO DE DATOS POR EL USUARIO (INGRESA LA FECHA)
fecha_hoy = input("INGRESE LA FECHA DE HOY EN EL SIGUIENTE FORMATO(DIA SEMANA, DD/MM): ")

# SEPARAMOS EL STRING EN DISTINTAS VARIABLES PARA TRABAJARLAS
dia_semana, fecha = fecha_hoy.split(",") 
dia_num, mes_num = fecha.split("/")
dia_num = int(dia_num)
mes_num = int(mes_num)

# BANDERA DE ERROR
error = False

# VALIDAMOS EL DIA DE LA SEMANA
dia_semana = dia_semana.capitalize() 
dias_validos = ["Lunes","Martes","Miercoles","Jueves","Viernes"]
if dia_semana not in dias_validos:
    print("ERROR: EL DIA DE LA SEMANA NO ES VÁLIDO")
    error = True

# VALIDAMOS EL NUMERO DEL MES Y QUE EL DIA SEA CORRECTO
dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if mes_num not in range(1,13):
    print("ERROR: EL MES NO ESTÁ EN EL RANGO")
    error = True
else:
    if dia_num < 1 or dia_num > dias_por_mes[mes_num-1]:
        print("ERROR: EL DIA NO CORRESPONDE A UNA FECHA CORRECTA")
        error = True

# SI NO HUBO ERRORES, SE EJECUTAN LOS DEMÁS BLOQUES
if not error:
    # EXAMENES NIVEL INICIAL, INTERMEDIO O AVANZADO
    examen = ["Lunes", "Martes", "Miercoles"]
    if dia_semana in examen:
        tomaron_examen = input("¿TOMARON EXAMEN? SI/NO: ") 
        tomaron_examen = tomaron_examen.capitalize()
        if tomaron_examen == "Si" or tomaron_examen == "si":
            aprobados_examen = int(input("¿CUANTOS APROBARON? "))
            desaprobados_examen = int(input("¿CUANTOS DESAPROBARON? "))
            total_examenes = aprobados_examen + desaprobados_examen
            porcentaje_aprobados = (aprobados_examen / total_examenes) * 100
            print(f"EL PORCENTAJE DE APROBADOS ES DE: {porcentaje_aprobados}%")

    # PRÁCTICA HABLADA
    if dia_semana == "Jueves":
        porcentaje_asistencia = int(input("INGRESE EL PORCENTAJE DE ASISTENCIA: "))
        if porcentaje_asistencia >= 50:  
            print("ASISTIO LA MAYORIA")
        else:
            print("NO ASISTIO LA MAYORIA")

    # INGLÉS PARA VIAJEROS
    if dia_semana == "Viernes":
        if dia_num == 1 and (mes_num == 1 or mes_num == 7):
            print("COMIENZO DE NUEVO CICLO LECTIVO")
            cantidad_alumnos = int(input("INGRESE LA CANTIDAD DE ALUMNOS DEL NUEVO CICLO LECTIVO: "))
            arancel_por_alumno = int(input("INGRESE EL ARANCEL POR ALUMNO: "))
            ingreso_total = cantidad_alumnos * arancel_por_alumno
            print(f"EL INGRESO TOTAL ES {ingreso_total}$")
        else:
            print("NO INICIA EL NUEVO CICLO LECTIVO")
