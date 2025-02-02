def calcular_valor_final(preco, condicao):
    if condicao == 1: # À vista dinheiro/ cheque
        desconto =  preco * 0.10
        valor_final = preco - desconto
        print(f'Valor a ser pago : R$ {valor_final:.2f} (10% de desconto)')
    elif condicao == 2: # À vista no cartão
        desconto = preco * 0.05
        valor_final = preco - desconto
        print(f'Valor a ser pago : R$ {valor_final:.2f} (5% de desconto')
    elif condicao == 3: # Em até 2x no cartão
        valor_final = preco
        print(f'Valor a ser pago: R$ {valor_final:.2f} (sem juros)')
    elif condicao == 4: # 3x ou mais no cartão
        juros = preco * 0.20
        valor_final = preco + juros
        print(f'Valor a ser pago: R$ {valor_final:.2f} (20 % de juros) ')
    else:
        print('Condição de pagamento inválida!')

# Esemplo de uso
preco_normal = float(input('Digite o preço normal do produto: R$ '))
print('Escolha a condição de pagamento: ')
print('1 - À vista dinheiro /cheque (10% de desconto)')
print('2 - À vista no cartão (5% de desconto')
print('3 - Em até 2x no cartão (preço normal)')
print('4 - 3x ou mais no cartão (20% de juros)')
condicao = int(input('Digite o número da condição: '))

calcular_valor_final(preco_normal, condicao)