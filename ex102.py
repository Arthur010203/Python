def fatorial(num, show=False):
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
