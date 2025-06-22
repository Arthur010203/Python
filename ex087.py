'''# Criando a matriz vazia
matriz = [[], [], []]

# Variáveis auxiliares
soma_pares = 0
soma_terceira_coluna = 0
maior_segunda_linha = 0

# Entrada de dados
for linha in range(3):
    for coluna in range(3):
        valor = int(input(f"Digite um valor para [{linha}, {coluna}]: "))
        matriz[linha].append(valor)

        # Soma dos pares
        if valor % 2 == 0:
            soma_pares += valor

# Mostrando a matriz formatada
print("\nMatriz 3x3:")
for linha in matriz:
    for valor in linha:
        print(f"[ {valor:^5} ]", end=' ')
    print()

# Soma da terceira coluna
for linha in range(3):
    soma_terceira_coluna += matriz[linha][2]

# Maior valor da segunda linha (índice 1)
maior_segunda_linha = max(matriz[1])

# Resultados
print(f"\nA) Soma de todos os valores pares: {soma_pares}")
print(f"B) Soma dos valores da terceira coluna: {soma_terceira_coluna}")
print(f"C) Maior valor da segunda linha: {maior_segunda_linha}")'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0 , 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}.')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')