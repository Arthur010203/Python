'''def fatorial(num, show=False):
    """
    Calcula o fatorial de um número.

    Parâmetros:
    num -- número inteiro a ser calculado o fatorial
    show -- (opcional) se True, mostra o processo de cálculo

    Retorna:
    O valor do fatorial de num
    """

    f = 1
    for i in range(num, 0, -1):
        f *= i
        if show:
            print(i, end=' x ' if i > 1 else ' = ')
    return f

# Exemplo de uso:
n = int(input("Digite um número: "))
print(fatorial(n, show=True)) # Coloque show=False se não quiser mostrar o cálculo
'''

# Versão do Guanabara

def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n:  O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f
# Programa Prinicipal
#print(fatorial(5))
help(fatorial)