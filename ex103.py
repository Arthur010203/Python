'''def ficha(jogador='<desconecido>', gols=0):
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

ficha(nome, gols )'''

# Versão do Guanabara

def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')

# Programa principal
n = str(input("Nome do Jogador: "))
g = str(input("Número de Gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
