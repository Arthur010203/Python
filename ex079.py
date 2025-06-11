''''# Lista para armazenar os valores únicos
valores = []

while True:
    num = int(input("Digite um valor: "))

    if num not in valores:
        valores.append(num)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor duplicado! Não será adicionado.")

    # Pergunta se o usuário quer continuar
    continuar = input("Quer continuar? [S/N] ").strip().upper()
    if continuar != 'S':
        break

#  Exibindo os valores em ordem crescente
valores.sort()
print(f'\nVocê digitou os seguintes valores únicos em ordem crescente: {valores}')
'''
números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adiconado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 30)
números.sort()
print(f'Você digitou os valores {números}')