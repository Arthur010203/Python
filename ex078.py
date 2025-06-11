''''# Lista para armazenar os valores
valores = []

# Leitura de 5 valores numéricos
for i in range(5):
    num = int(input(f'Digite o {i+1}° valor:'))
    valores.append(num)

# Encontrando o maior e o menor valor
maior = max(valores)
menor = min(valores)

# Encontrando as posições do maior e do menor valor
posicoes_maior = [i for i, v in enumerate(valores) if v == maior]
posicoes_menor = [i for i, v in enumerate(valores) if v == menor]

# Exibindo os resultados
print(f'\nVocê digitou os valores: {valores}')
print(f'O maior valor digitado foi {maior} nas posições: {posicoes_maior}')
print(f'O menor valor digitado foi {menor} nas posições: {posicoes_menor}')'''

# Versão do Guanabara

listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end= '')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()