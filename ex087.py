# Criando a matriz vazia
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
print(f"C) Maior valor da segunda linha: {maior_segunda_linha}")