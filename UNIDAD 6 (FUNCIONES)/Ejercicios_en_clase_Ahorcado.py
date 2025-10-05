# --- JUEGO DEL AHORCADO ---
import random

# FUNCION PARA ELEGIR PALABRA RANDOM
def palabra_ahorcado(lista):
    return random.choice(lista)

# FUNCION PARA MOSTRAR PALABRA CON GUIONES
def guiones_para_palabra(palabra):
    palabra_oculta = ""
    for letra in palabra:
        if letra == " ":
            palabra_oculta += " "
        else:
            palabra_oculta += "_"
    return palabra_oculta

# LISTA DE PALABRAS POSIBLES
palabras_posibles = [
    "ANUEL AA", "BAD BUNNY", "RAUW ALEJANDRO", "JHAYCO", "MORA", "DUKI",
    "DADDY YANKEE", "DON OMAR", "MYKE TOWERS", "JBALVIN", "OZUNA", "EMILIA"
]

# SELECCIONA UNA PALABRA AL AZAR
palabra_seleccionada = palabra_ahorcado(palabras_posibles)
palabra_oculta = guiones_para_palabra(palabra_seleccionada)

intentos = 6  # cantidad máxima de errores
letras_usadas = []  # para evitar repetir letras

print("-----BIENVENIDO AL JUEGO DEL AHORCADO-----")
print("--LA TEMÁTICA ES CANTANTES DE REGGAETON--")

# BUCLE PRINCIPAL DEL JUEGO
while "_" in palabra_oculta and intentos > 0:
    print("\nPalabra: ", palabra_oculta)
    print("Letras usadas:", ", ".join(letras_usadas))
    print(f"Te quedan {intentos} intentos.")
    
    letra = input("Ingresa una letra: ").upper()

    # VERIFICAR SI SE USO LA LETRA
    if letra in letras_usadas:
        print("⚠️ Ya usaste esa letra, probá otra.")
        continue
    letras_usadas.append(letra)

    # ACTUALIZAR PALABRA OCULTA
    nueva_palabra_oculta = ""
    acierto = False
    for i in range(len(palabra_seleccionada)):
        if palabra_seleccionada[i] == letra:
            nueva_palabra_oculta += letra
            acierto = True
        else:
            nueva_palabra_oculta += palabra_oculta[i]

    palabra_oculta = nueva_palabra_oculta

    if acierto:
        print("✅ ¡Adivinaste una letra correctamente!")
    else:
        intentos -= 1
        print("❌ Letra incorrecta.")

# FINAL DEL JUEGO
if "_" not in palabra_oculta:
    print(f"\n🎉 ¡FELICITACIONES! Adivinaste la palabra: {palabra_seleccionada}")
else:
    print(f"\n💀 Te quedaste sin intentos. La palabra era: {palabra_seleccionada}")
