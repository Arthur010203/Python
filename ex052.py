'''# Verificar se um número é primo

numero = int(input('Digite um número para verificar se é primo: '))

# Inicializa o contador de divisores
divisores = 0

# Verifica quantos divisores o número possui
for i in range(1, numero + 1):
      if numero % i == 0:
          divisores += 1

# Condição para número primo
if divisores == 2:
    print(f'O número {numero} é primo.')
else:
    print(f'O número {numero} não é primo.') '''

# Versão do prof

núm = int(input('Digite um número: '))
tot = 0
for c in range(1, núm + 1):
    if núm % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('O número {} foi divisível {} vezes'.format(núm, tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')