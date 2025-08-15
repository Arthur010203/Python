
"""import moeda

preco = float(input("Digite o preço: R$ "))

print(f"O dobro de R${preco:.2f} é R${moeda.dobro(preco):.2f}")
print(f"A metade de R${preco:.2f} é R${moeda.metade(preco):.2f}")
print(f"Aumentando 10%, temos R${moeda.aumentar(preco, 10):.2f}")
print(f"Diminuindo 13%, temos R${moeda.diminuir(preco, 13):.2f}")
"""

from ex109 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {(moeda.metade(p,True))}')
print(f'O dobro de {moeda.moeda(p)} é {(moeda.dobro(p,True))}')
print(f'Aumentar 10%, tem-se {(moeda.aumentar(p, 10, True))}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')