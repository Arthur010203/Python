# Versão original
'''import random

n = int(input('Digite um número entre 0 e 5: '))
num = random.randint(0, 5)
print('Você escolheu o numero {}, e o numero sorteado é...{}'.format(n, num))
if n == num:
    print('parabéns você acertou! *-* ')
else:
    print('não foi dessa vez, tente novamente mais tarde')'''

# Versão do Guanabara

from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('🤔🤔🤔🤔🤗')
sleep(3)
if jogador  == computador :
    print('PARABÉNS! Você conseguiu me vencer (￣Д￣!')
else:
    print('GANHEI!  Eu pensei no número {} e não no {}! (ಥ◡ಥ)'.format(computador, jogador))

