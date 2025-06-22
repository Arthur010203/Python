''''# Criando a matriz vazia
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
    print()'''

# Versão do Guanabara
matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l] [c]:^5}]', end='')
    print()

