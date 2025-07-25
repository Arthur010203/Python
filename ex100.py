import random
# Lista onde os números sorteados serão armazenados
numeros = []

# Função para sortear 5 números aleatórios entre 1 e 10
def sorteia():
    print("Sorteando 5 números: ", end='')
    for _ in range(5):
        n = random.randint(1, 10)
        numeros.append(n)
        print(n, end= '')
    print("\n")

# Função para somar apenas os números pares da lista
def somaPar():
    soma = sum(num for num in numeros if num % 2 == 0)
    print(f"Somando os valores pares de {numeros}, temos {soma}.\n")

# Execução do programa
sorteia()
somaPar()