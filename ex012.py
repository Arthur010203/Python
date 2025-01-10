preço = float(input('Qual é o preço do produto ? R$'))
valor = preço - (preço * 5 / 100)
print('O produto que valia R${} passa a valer R${} com o desconto de 5%'.format(preço, valor))