# Lista principal e listas separadas para pares e ímpares
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
print(f"Lista de ímpares: {impares}")