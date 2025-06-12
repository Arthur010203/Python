# Criando a matriz vazia
matriz = [[], [], []]

# Preenchendo a matriz com valores do teclado
for linha in range(3):
    for coluna in range(3):
        valor = int(input(f"Digite um valor para [{linha}, {coluna}]: "))
        matriz[linha].append(valor)

# Mostrando a matriz formatada
print("\nMatriz 3x3:")
for linha in matriz:
    for valor in linha:
        print(f"[ {valor:^5} ]", end =' ')
    print()