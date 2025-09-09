import random
# EJERCICIO BINGO
print("BIENVENIDOS AL BINGO")
bingo_completo = False
contador=0
# CREAMOS EL CARTON 5X5
numeros = random.sample(range(1, 51), 25)
carton = [numeros[i:i+5] for i in range(0, 25, 5)]
for filas in carton:
# MOSTRAMOS EL CARTON
    print(filas)
# EMPEZAMOS EL BINGO
numero_bingo = []
while not bingo_completo: 
    numero_bingo = random.randint(1,50)
    print(f"SE SORTE EL NUMERO {numero_bingo}")
    encontrado=False
    for i in range(5):
        for j in range(5):
            if carton[i][j] == numero_bingo:
                carton[i][j] = 0
                print("¡LO TENES!")
                encontrado = True
    if not encontrado:
        print("EL NUMERO NO ESTA EN TU CARTON")
    # MOSTRAR CARTON ACTUALIZADO
    for fila in carton:
        print(fila)
    if all(num == 0 for fila in carton for num in fila): 
        print("¡¡¡BINGO!!!")
        bingo_completo = True

