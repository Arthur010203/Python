''''#criando o dicionário
aluno = {}

# Lendo os dados

aluno['nome'] = input("Nome do aluno: ")
aluno['media'] = float(input(f"Média de {aluno['nome']}:"))

# Determinando a situação
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

# Exibindo o conteúdo do dicionário
print("\n--- Resultado ---")
for chave, valor in aluno.items():
    print(f"{chave.capitalize()}:{valor}")'''

# Versão do Guanabara

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f'   - {k} é igual a {v}')

