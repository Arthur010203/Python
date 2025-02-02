import random


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
jogar_jokenpo()