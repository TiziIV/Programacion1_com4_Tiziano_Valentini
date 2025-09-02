# EJERCICIO 1 (FOR)
# ELEGIMOS NO INCLUIR LA LETRA Ñ
corrimiento = int(input("INGRESE EL CORRIMIENTO DEL ENCRIPTADO: ")) 
# ASIGNAMOS VALOR A CADA LETRA

abecedario = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
encriptado = ""

for i in range(5):
    mensaje = input("INGRESE EL MENSAJE A ENCRIPTAR: ")
    mensaje = mensaje.upper()
    
    for letra in range(len(mensaje)):
        letra = mensaje[letra]  # SEPARA EL TEXTO POR CADA LETRA EN CADA CICLO FOR
        posicion = abecedario.index(letra)  # SACAR POSICION DE CADA LETRA EN LA LISTA ABECEDARIO
        posicion_corrida = posicion + corrimiento  # CALCULAR LA POSICION CON EL CORRIMIENTO EN LA LISTA
        
        if posicion_corrida > 25:
            posicion_corrida = posicion_corrida - 26
        
        letra_corrida = abecedario[posicion_corrida]  # CALCULA A QUE LETRA CORRESPONDE LA POSICION CORRIDA
        encriptado = encriptado + letra_corrida  # JUNTA TODAS LAS LETRAS PARA MOSTRAR EL MENSAJE ENCRIPTADO
    print(encriptado)
    encriptado = ""

# EJERCICIO 2(WHILE)
import random

contador_humano = 0
contador_maquina = 0
#INICIAMOS EL BUCLE
while True:
    #EL USUARIO ELIGE
    seleccion_valida = False
    while not seleccion_valida:
        print("\nSELECCIONE UNA: A/B/C")
        print("A: PIEDRA")
        print("B: PAPEL")
        print("C: TIJERA")
        
        seleccion = input("CUAL ES SU ELECCION: ").upper()
        if seleccion not in ["A", "B", "C"]:
            print("ERROR: SELECCIONO FUERA DE RANGO A/B/C")
        else:
            if seleccion == "A":
                seleccion = "PIEDRA"
            elif seleccion == "B":
                seleccion = "PAPEL"
            else:
                seleccion = "TIJERA"
            seleccion_valida = True

    # SELECCION DE LA COMPUTADORA
    seleccion_computadora = ["PIEDRA","PAPEL","TIJERA"]
    juego = random.choice(seleccion_computadora)
    print(f"TÚ: {seleccion} - COMPUTADORA: {juego}")

    # DETERMINAR RESULTADO
    if seleccion == juego:
        print("EMPATE")
    elif (seleccion == "PIEDRA" and juego == "TIJERA") or \
         (seleccion == "PAPEL" and juego == "PIEDRA") or \
         (seleccion == "TIJERA" and juego == "PAPEL"):
        print("GANASTE")
        contador_humano=contador_humano +1
    else:
        print("PERDISTE")
        contador_maquina=contador_maquina +1
    
    # MOSTRAR PUNTAJE
    print(f"Puntaje -> Humano: {contador_humano} | Computadora: {contador_maquina}")
    
    # PREGUNTAR SI QUIERE SEGUIR JUGANDO
    while True:
        volver_a_iniciar = input("¿DESEA SEGUIR JUGANDO? SI/NO: ").upper()
        if volver_a_iniciar in ["SI", "NO"]:
            break
        print("ERROR: Debe ingresar SI o NO")
    
    if volver_a_iniciar == "NO":
        print("¡Gracias por jugar! Hasta luego.")
        break

