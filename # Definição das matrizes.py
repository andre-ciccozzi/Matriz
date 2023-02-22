# Definindo as matrizes
matriz1 = [[3, 1, 3], [6, 5, 5]]
matriz2 = [[100, 50], [50, 100], [50, 50]]

if len(matriz1[0]) != len(matriz2):
    print("Erro")
else:
    # Inicializando a matriz resultante com zeros
    resultado = [[0 for j in range(len(matriz2[0]))] for i in range(len(matriz1))]

    #  multiplicação de matrizes
    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    # Imprimindo a matriz resultante
    for linha in resultado:
        print(linha)


