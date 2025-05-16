'''print("==== CAIXA ELETRÔNICO ====")

# Solicita o valor a ser sacado
valor = int(input("Informe o valor a ser sacado: R$ "))

# Inicializa as cédulas disponíveis
cedulas = [50, 20, 10, 1]

# Calcula e exibe quantas cédullas de cada valor serão entregues
for cedula in cedulas:
    quantidade = valor // cedula
    valor = valor % cedula
    if quantidade > 0:
        print(f"{quantidade} cédula(s) de R$ {cedula} ")

print("=== FIM DA OPERAÇÃO ===")'''

# Versão do Guanabara

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valoar você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
         print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break

print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')

