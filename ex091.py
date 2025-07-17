'''import random
from time import sleep
from operator import itemgetter

# Criando o dicionário com os resultados dos dados
jogadores = {
    'Jogador 1': random.randint(1,6),
    'Jogador 2': random.randint(1,6),
    'Jogador 3': random.randint(1,6),
    'Jogador 4': random.randint(1,6)
}

# Mostrando os resultados
print("Resultados dos dados:")
for jogador, resultado in jogadores.items():
    print(f"{jogador} tirou {resultado}")

# Ordenando os jogadores com base nos resultados (do maio para o menor)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

# Exibindo o ranking
print("\nRanking dos jogadores:")
for i, (jogador, resultado) in enumerate(ranking, start=1):
    print(f"{i}°lugar: {jogador} com {resultado}")'''

# Versão do Guanabara

from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'    {i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)
