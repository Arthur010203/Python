def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print('\033[31mErro! Digite um número inteiro válido.\033[m')

# Exemplo de uso:
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')

