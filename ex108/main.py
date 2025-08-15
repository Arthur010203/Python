
"""import moeda

preco = float(input("Digite o preço: R$ "))

print(f"O dobro de R${preco:.2f} é R${moeda.dobro(preco):.2f}")
print(f"A metade de R${preco:.2f} é R${moeda.metade(preco):.2f}")
print(f"Aumentando 10%, temos R${moeda.aumentar(preco, 10):.2f}")
print(f"Diminuindo 13%, temos R${moeda.diminuir(preco, 13):.2f}")
"""

from ex108 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {p} é {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentar 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')