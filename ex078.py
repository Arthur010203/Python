# Lista para armazenar os valores
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
print(f'O menor valor digitado foi {menor} nas posições: {posicoes_menor}')