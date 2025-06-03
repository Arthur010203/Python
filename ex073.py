''''# Tupla com os 20 times em ordem de colocação (exemplo fictício)
brasileirao = (
    'Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo',
    'Bragrantino', 'Athletico-PR', 'Internacional', 'Fortaleza', 'São Paulo',
    'Cuiabá', 'Corinthias', 'Cruzeiro', 'Bahia', 'Santos',
    'Goiás', 'Vasco', 'Coritiba', 'América-MG', 'Chapecoense'
)

# A) Os 5 primeiros colocados
print("A) Os 5 primeiros colocados:")
print(brasileirao[:5])

#B) Os 4 últimos colocados
print("\nB) Os 4 últimos colocados:")
print(brasileirao[-4:])

#C) Times em ordem alfabética
print("\nC) Times em ordem alfabética:")
print(sorted(brasileirao))

# D) Posição da Chapecoense
print("\nD) Posição da Chapecoense na tabela:")
if 'Chapecoense' in brasileirao:
    print(f"Chapecoense está na {brasileirao.index('Chapecoense') + 1}ª posição.")
else:
    print("Chapecoense não está na tabela.")'''

# Versão do Guanabara

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
         'Atlético-GO')
print('-=' * 15)
print(f'Lista de times: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')