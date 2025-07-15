pessoas = []
soma_idade = 0

while True:
    pessoa = {}
    pessoa['nome'] = input('Nome: ').strip()
    pessoa['sexo'] = input('Sexo [M/F]: ').strip().upper()
    while pessoa['sexo'] not in 'MF':
        print('Erro! Digite apenas M ou F.')
        pessoa['sexo'] = input('Sexo [M/F]: ').strip().upper()
    pessoa['idade'] = int(input('Idade: '))
    soma_idade += pessoa['idade']
    pessoas.append(pessoa.copy())

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break

# A) Quantas pessoas foram cadastadas
print(f'\nA) Total de pessoas cadastradas: {len(pessoas)}')

# B) A média de idade
media_idade = soma_idade / len(pessoas)
print(f'B) Média de idade do grupo: {media_idade:.2f} anos')

# C) Lista com todas as mulheres
mulheres = [p['nome'] for p in pessoas if p['sexo'] == 'F']
print(f'C) Mulheres cadastradas: {", ".join(mulheres)if mulheres else "Nenhuma"}')

# D) Lista com todas as pessoas com idade acima da média
acima_media = [p for p in pessoas if p['idade'] > media_idade]
print('D) Pessoas com idade acima da média: ')
for p in acima_media:
    print(f" Nome: {p['nome']}, Sexo: {p['sexo']}, Idade: {p['idade']}")