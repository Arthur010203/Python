'''import random
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
somaPar()'''

# Versão do Guanabara
from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

números = list()
sorteia(números)
somaPar(números)
