'''pessoas = []
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
    print(f" Nome: {p['nome']}, Sexo: {p['sexo']}, Idade: {p['idade']}")'''

# Versão do Guanabara
galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
           break
        print('ERRO! Responda apenas S ou N. ')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'B) A média de idade é de {média: 5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO>>')
