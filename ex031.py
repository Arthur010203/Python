d = float(input('Qual é a distância da viagem em Km ? '))
p1 = 0.50
p2 = 0.45
if d <= 200:
    print('O preço da passagem ficou {} R$'.format(d*p1))
else:
    print('O preço da passagem ficou {} R$'.format(d*p2))