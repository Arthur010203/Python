'''# Tupla com produtos e preços (nome, preço, nome, preço ...)
produtos = ('Arroz', 8.56,
            'Feijão',22.50,
            'Macarrão', 9.59,
            'Óleo', 7.99,
            'Açucar', 5.29,
            'Sal', 3.49,
            'Café', 38.99,
            'Leite', 5.69
)

# Impressão formatatda em forma de tabela
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

# Iterando pelos elementos da tupla com passo 2
for i in range(0, len(produtos), 2):
    nome = produtos[i]
    preco = produtos[i + 1]
    print(f'{nome:.<30} R$ {preco:>6.2f}')

print('-' * 40)'''

# Versão do Guanabara

listagem  = ('Lápis', 1.75,
             'Borracha', 2,
            'Caderno', 15.90,
             'Estojo', 25,
             'Transferidor', 4.20,
             'Compasso', 9.99,
             'Mochila', 120.32,
             'Canetas', 22.30,
            'Livro', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end= '')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)