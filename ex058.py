import random

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
