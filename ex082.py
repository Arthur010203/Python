'''# Lista principal e listas separadas para pares e ímpares
valores = []
pares = []
impares = []

# Leitura dos valores
while True:
    num = int(input("Digite um número: "))
    valores.append(num)

    # Classifica como par ou ímpar
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

    continuar = input("Que continuar? [S/N] ").strip().upper()
    if continuar != 'S':
        break

# Exibindo os resultados
print("\nRESULTADOS:")
print(f"Lista completa: {valores}")
print(f"Lista de pares: {pares}")
print(f"Lista de ímpares: {impares}")'''

# Versão do Guanabara

num = list()
pares = list()
ímpares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de pares é {ímpares}')