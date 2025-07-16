time = []

while True:
    jogador = {}
    jogador['nome'] = input('Nome do jogador: ').strip()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    jogador['gols'] = []
    total = 0
    for i in range(partidas):
        gols = int(input(f'   Quantos gols na partida {i + 1}? '))
        jogador['gols'].append(gols)
        total += gols
    jogador['total'] = total

    time.append(jogador.copy())

    continuar = input('Deseja cadastrar outro jogador? [S/N]: ').strip().upper()
    if continuar == 'N':
        break

print('-=' * 30)

# Mostrar o cabeçalho da tabela
print(f'{"Cod":<4}{"Nome":<15}{"Gols":<20}{"Total":<5}')
print('-' * 45)

# Mostrar os dados de todos os jogadores
for i, jogador in enumerate(time):
    print(f'{i:<4}{jogador["nome"]:<15}{str(jogador["gols"]):<20}{jogador["total"]:<5}')

print('-' * 45)

# Consulta de dados individuais
while True:
    busca = int(input('Mostrar dados de qual jogador? (Digite o código ou -1 para sair): '))
    if busca == -1:
        break
    if busca >= len(time):
        print('Erro! Código inválido.')
    else:
        print(f'-- DETALHES DO JOGADOR: {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i + 1} fez {g} gols.')
    print('-' * 45)
