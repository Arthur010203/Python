
'''def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print('\033[31mErro! Digite um número inteiro válido.\033[m')

# Exemplo de uso:
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')'''

# Versão do Guanabara

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')