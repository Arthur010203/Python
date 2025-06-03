'''import random
def jogar_jokenpo():
    opcoes = ["pedra", "papel", "tesoura"]

    print("Bem-vindo ao Jokenpô!")
    print("Escolha uma opção:")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")

    try:
        escolha_usuario = int(input("Digite o número da sua escolha: "))
        if escolha_usuario < 1 or escolha_usuario > 3:
            print("Escolha inválida! Por favor, digite 1, 2 ou 3.")
            return

        escolha_usuario = opcoes[escolha_usuario - 1]  # Converte para texto
        escolha_computador = random.choice(opcoes)  # Computador escolhe aleatoriamente

        print(f"\nVocê escolheu: {escolha_usuario}")
        print(f"O computador escolhou: {escolha_computador}\n")

        # Verifica o vencedor
        if escolha_usuario == escolha_computador:
            print("Empate!")
        elif (escolha_usuario == "pedra" and escolha_computador == "tesoura") or \
                (escolha_usuario == "papel" and escolha_computador == "pedra") or \
                (escolha_usuario == "tesoura" and escolha_computador == "papel"):
            print("Você venceu! 🎉")
        else:
            print("O computador venceu! 😢")

    except ValueError:
        print("Entrada inválida! Por favor, digite um número.")


# Executa o jogo
jogar_jokenpo()'''

#Versão do prof

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')