'''import random

# Gera 5 números aleatórios entre 1 e 100 e coloca em uma tupla
numeros = tuple(random.randint(1, 100) for _ in range(5))


# Exibe os números gerados
print("Números gerados:", numeros)

# Encontra o menor e o maior número na tupla
menor = min(numeros)
maior = max(numeros)

# Exibe o menor e o maior valor
print("Menor valor:", menor)
print("Maior valor:", maior)    '''

# Versão do Guanabara

from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')

