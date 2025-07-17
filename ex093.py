'''jogador = dict()
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
'''

# Versão do Guanabara

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
for c in range(0, tot):
    partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')