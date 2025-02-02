# Solicita um número inteiro ao usuário
num = int(input("Digite um número inteiro: "))

# Mostra as opções de conversão
print('Escolha a base para conversão:')
print('[1] Converter para Binário')
print('[2] Converter para Octal')
print('[3] Converter para Hexadecimal')

# Lê a opção escolhida
opcao = int(input('Sua opção: '))

#Realiza a conversão e exibe o resultado
if opcao == 1:
    print(f"O número {num} em binário é {bin(num)[2:]}")
elif opcao == 2:
    print(f'O número {num} em octal é {oct(num)[2:]}')
elif opcao == 3:
    print(f'O número {num} em hexadecimal é {hex(num)[2:].upper()}')
else:
    print('Opção inválida! Escolha 1, 2 ou 3.')