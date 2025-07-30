def ficha(jogador='<desconecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')

# Programa principal
nome = input('Nome do jogador: ').strip()
gols = input('Número de gols: ').strip()

# Tratando os dados
if nome == '':
    nome = '<desconhecido>'

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

ficha(nome, gols )