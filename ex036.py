# Programa para aprovação de empréstimo bancário

# Solicita os dados do usuário
valor_casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o seu salário: R$ '))
anos = int(input('Em quantos anos deseja pagar? '))

# Calcula o valor da prestação mensal
prestacao_mensal = valor_casa / (anos*12)
limite_prestacao = salario*0.3 #30% do salário

# Verifica se o empréstimo pode ser aprovado
print(f'\nValor da prestação: R$ {prestacao_mensal:.2f}')
if prestacao_mensal <= limite_prestacao:
    print("Empréstimo APROVADO!")
else:
    print('Empréstimo NEGADO! O valor da prestação excede 30% do seu salário.')

