'''import random

def jogo_adivinhacao():
    numero_secreto = random.randint(0, 10)
    tentativas = 0

    print("Tente advinhar o número entre 0 e 10!")

    while True:
        try:
            palpite = int(input("Seu palpite: "))
            tentativas += 1

            if palpite == numero_secreto:
                print(f"Parabéns! Você acertou em {tentativas} tentativas.")
                break
            elif palpite < numero_secreto:
                print("Tente um número maior!")
            else:
                print("Tente um número menor!")
        except ValueError:
            print("Por favor, digite um número válido.")
# Chamado a função
jogo_adivinhacao()
'''

# Versão Guanabara

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue advinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite?'))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas '.format(palpites))