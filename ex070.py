'''total_gasto = 0
produtos_mais_1000 = 0
produto_mais_barato = ''
preco_mais_barato = float('inf')

print("===== CADASTROS DE PRODUTOS ====")

while True:
    nome = input("Nome do produto: ").strip()
    preco = float(input("Preço do produto: R$"))

    total_gasto += preco

    if preco > 1000:
        produtos_mais_1000 += 1

    if preco < preco_mais_barato:
        preco_mais_barato = preco
        produto_mais_barato = nome

    continuar = input("Deseja cadastrar outro produto? [S/N]:").strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input("Entrada inválida. Deseja continuar? [S/N]: ").strip().upper()

    if continuar == 'N':
        break

print("\n==== RESUMO DOS PRODUTOS =====")
print(f"A) Total gasto na compra: R${total_gasto:.2f}")
print(f"B) Produtos que custam mais de R$1000: {produtos_mais_1000}")
print(f"C) Produto mais barato: {produto_mais_barato}(R${preco_mais_barato:.2f})")'''

# Versão do Guanabara
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi{total:10.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que  custa R${menor:}')