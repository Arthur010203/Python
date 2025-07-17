'''from datetime import datetime

# Ano atual automático
ano_atual = datetime.now().year

# Dicionário para armazenar os dados
dados = {}

# Entrada de dados do usuário
dados['nome'] = input("Nome: ")
nascimento = int(input("Ano de nascimento: "))
dados['idade'] = ano_atual - nascimento
dados['ctps'] = int(input("Carteira de trabalho (0 se não tiver):"))

# Se tiver carteira assinada
if dados['ctps'] != 0:
    dados['contratação'] = int(input("Ano de contratação: "))
    dados['salário'] = float(input("Salário: R$ "))
    # Calcula tempo de contribuição e idade de aposentadoria
    tempo_contribuicao = 35
    anos_trabalhados = ano_atual - dados['contratação']
    anos_restantes = tempo_contribuicao - anos_trabalhados
    dados['aposentadoria'] = dados['idade'] + anos_restantes
else:
    dados['aposentadoria'] = 'Sem previsão (sem carteira assinada)'

# Exibe os dados
print("\nCadastro completo:")
for chave, valor in dados.items():
    print(f"{chave.capitalize()}: {valor}")'''

# Versão do Guanabara

from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem):'))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação']+ 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'    - {k} tem o valor {v}')