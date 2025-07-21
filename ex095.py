'''time = []

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
'''

# Versão do Guanabara
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c + 1}?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca] ["nome"]}:')
        for i, g in enumerate(time[busca] ['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')