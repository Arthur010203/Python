jogador = dict()
gols = list()

# Entrada de dados
jogador['nome'] = input("Nome do jogador: ")
total_partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

# Coletando gols por partida
for i in range(total_partidas):
    gol = int(input(f"Quantos gols na partida {i + 1 }?"))
    gols.append(gol)

# Armazenando os dados no dicionário
jogador['gols'] = gols
jogador['total'] = sum(gols)

# Saída formatada
print("\nDados do jogador:")
for chave, valor in jogador.items():
    print(f"{chave.capitalize()}: {valor}")

print("\nDetalhamento das partidas:")
for i, gol in enumerate(jogador['gols']):
    print(f"    => Na partida {i + 1}, fez {gol} gol(s).")

print(f"\nTotal de gols no campeonato: {jogador['total']}")
