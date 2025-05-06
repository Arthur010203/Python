import random

vitorias = 0

print("==== JOGO DO PAR ÍMPAR =====")

while True:
    jogador_num = int(input("Escolha um número: "))
    jogador_escolha = input("Par ou Ímpar? [P/I] ").strip().upper()

    while jogador_escolha not in ['P', 'I']:
        jogador_escolha = input("Escolha inválida. Digite 'P' para Par ou 'I' para Ímpar: ").strip()

    computador_num = random.randint(0, 10)
    total = jogador_num + computador_num
    resultado = 'P' if total % 2 == 0 else 'I'

    print(f"Você jogou {jogador_num} e o computador {computador_num}. Total = {total} ->", end='')
    print("DEU PAR" if resultado == 'P' else "DEU ÍMPAR")

    if jogador_escolha == resultado:
        print("Você VENCEU!\n")
        vitorias += 1
    else:
        print("Você PERDEU!")
        break

print(f"Fim de jogo. Você teve {vitorias} vitórias(s) consecutiva(s).")